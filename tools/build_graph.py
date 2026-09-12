#!/usr/bin/env python3
"""构建知识图谱 —— 输出 graph/graph.json 与 graph/graph.html。

参照 LLM Wiki 规范的"两遍构建"：

  第一遍（确定性）：解析所有页面的 [[双链]] → 边标记为 EXTRACTED
  第二遍（推断）：找出共享来源 / 标签高度重合、但在双链上没有直连的页面
                  → 边标记为 INFERRED，带 confidence 分数

社区检测用**标签传播（label propagation）**近似替代 Louvain —— 这样不依赖
networkx，纯标准库即可运行。结果只作"主题聚类"的粗略参考，不等价于 Louvain。

graph.html 是**零依赖**的：不加载任何 CDN，用 canvas 自己算力导向布局，
断网也能打开。支持拖拽节点、悬停高亮邻居、滚轮缩放。

用法：
    python3 tools/build_graph.py
    python3 tools/build_graph.py --open        # 生成后用默认浏览器打开
    python3 tools/build_graph.py --no-inferred # 只保留确定性边
"""

from __future__ import annotations

import argparse
import json
import random
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

from wiki_lib import (
    C,
    GRAPH_DIR,
    iter_pages,
    page_name,
    read_page,
    rel_within_wiki,
    relative,
)

#: 各页面类型对应的配色（浅色主题）。深色主题下由 CSS 覆写。
TYPE_COLORS = {
    "source": "#2563eb",
    "entity": "#7c3aed",
    "concept": "#059669",
    "synthesis": "#d97706",
}

#: 共享来源的 Jaccard 相似度低于此值就不连边
INFERRED_MIN_SCORE = 0.5


# ------------------------------------------------------------------ 建图


def collect_nodes(pages) -> list[dict]:
    nodes: list[dict] = []
    for path in pages:
        fm, _ = read_page(path)
        name = page_name(path)
        nodes.append(
            {
                "id": name,
                "label": str(fm.get("title") or name),
                "type": str(fm.get("type") or "unknown"),
                "tags": fm.get("tags") or [],
                "sources": fm.get("sources") or [],
                "path": rel_within_wiki(path),
                "updated": str(fm.get("last_updated") or ""),
            }
        )
    return nodes


def pass_one_extracted(pages) -> list[dict]:
    """第一遍：确定性解析双链。"""
    existing = {page_name(p) for p in pages}
    seen: set[tuple[str, str]] = set()
    edges: list[dict] = []

    for path in pages:
        source = page_name(path)
        _, body = read_page(path)
        for raw in __import__("re").findall(r"\[\[([^\[\]]+?)\]\]", body):
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            if not target or target not in existing or target == source:
                continue
            key = tuple(sorted((source, target)))
            if key in seen:
                continue
            seen.add(key)
            edges.append({"source": source, "target": target, "kind": "EXTRACTED", "confidence": 1.0})
    return edges


def pass_two_inferred(nodes: list[dict], edges: list[dict]) -> list[dict]:
    """第二遍：推断双链没覆盖的隐含关系（共享来源的重合度）。"""
    by_id = {n["id"]: n for n in nodes}
    linked = {tuple(sorted((e["source"], e["target"]))) for e in edges}
    inferred: list[dict] = []

    ids = sorted(by_id)
    for i, a in enumerate(ids):
        for b in ids[i + 1 :]:
            if tuple(sorted((a, b))) in linked:
                continue
            sa, sb = set(by_id[a]["sources"]), set(by_id[b]["sources"])
            if not sa or not sb:
                continue
            union = sa | sb
            score = len(sa & sb) / len(union) if union else 0.0
            if score >= INFERRED_MIN_SCORE:
                inferred.append(
                    {
                        "source": a,
                        "target": b,
                        "kind": "INFERRED",
                        "confidence": round(score, 2),
                        "reason": f"共享来源 {sorted(sa & sb)}",
                    }
                )
    return sorted(inferred, key=lambda e: -e["confidence"])


def detect_communities(nodes: list[dict], edges: list[dict], max_passes: int = 20) -> dict[str, int]:
    """Louvain 第一层：贪心模块度优化（纯标准库实现，不依赖 networkx）。

    只做第一层（节点级聚合），不做社区折叠后的第二层——对 wiki 这个规模
    （几十到几百页）已经足够，且结果可复现。

    边权：EXTRACTED 记 1.0，INFERRED 记其 confidence。
    """
    ids = sorted(n["id"] for n in nodes)
    adjacency: dict[str, dict[str, float]] = {u: {} for u in ids}
    for edge in edges:
        u, v = edge["source"], edge["target"]
        if u == v or u not in adjacency or v not in adjacency:
            continue
        weight = 1.0 if edge["kind"] == "EXTRACTED" else float(edge.get("confidence", 0.5))
        adjacency[u][v] = adjacency[u].get(v, 0.0) + weight
        adjacency[v][u] = adjacency[v].get(u, 0.0) + weight

    degree = {u: sum(adjacency[u].values()) for u in ids}
    total_weight = sum(degree.values()) / 2.0
    if total_weight == 0:
        return {u: 0 for u in ids}

    community = {u: index for index, u in enumerate(ids)}
    community_degree = {index: degree[u] for index, u in enumerate(ids)}

    for _ in range(max_passes):
        moved = False
        for u in ids:
            current = community[u]
            weight_to: dict[int, float] = {}
            for v, weight in adjacency[u].items():
                cv = community[v]
                weight_to[cv] = weight_to.get(cv, 0.0) + weight

            ki = degree[u]
            community_degree[current] -= ki

            best, best_gain = current, None
            for candidate in sorted(set(weight_to) | {current}):
                k_in = weight_to.get(candidate, 0.0)
                gain = k_in - community_degree.get(candidate, 0.0) * ki / (2.0 * total_weight)
                if best_gain is None or gain > best_gain:
                    best, best_gain = candidate, gain

            community_degree[best] = community_degree.get(best, 0.0) + ki
            if best != current:
                community[u] = best
                moved = True
        if not moved:
            break

    ordered = sorted(set(community.values()))
    remap = {label: index for index, label in enumerate(ordered)}
    return {u: remap[community[u]] for u in ids}


# ------------------------------------------------------------------ HTML

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LLM Wiki · 知识图谱</title>
<style>
  :root{
    --bg:#f6f7f9; --panel:#ffffff; --ink:#1f2937; --sub:#6b7280;
    --line:#e5e7eb; --accent:#2563eb; --dim:#9ca3af;
  }
  @media (prefers-color-scheme: dark){
    :root{
      --bg:#111318; --panel:#1a1d24; --ink:#e8eaed; --sub:#9aa0aa;
      --line:#2b3038; --accent:#7aa2f7; --dim:#6b7280;
    }
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;
       background:var(--bg);color:var(--ink);overflow:hidden}
  #canvas{display:block;width:100vw;height:100vh;cursor:grab}
  #canvas.dragging{cursor:grabbing}
  .panel{position:fixed;background:var(--panel);border:1px solid var(--line);
         border-radius:12px;padding:14px 16px;box-shadow:0 6px 24px rgba(0,0,0,.08);font-size:13px}
  #title{top:16px;left:16px;min-width:200px}
  #title h1{font-size:15px;font-weight:700;margin-bottom:6px}
  #title .meta{color:var(--sub);line-height:1.7}
  #legend{bottom:16px;left:16px;line-height:1.9}
  #legend .row{display:flex;align-items:center;gap:8px}
  #legend .dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
  #legend .line{width:22px;height:0;border-top:2px solid var(--dim);flex-shrink:0}
  #legend .line.dash{border-top-style:dashed}
  #info{top:16px;right:16px;max-width:290px;display:none}
  #info h2{font-size:14px;margin-bottom:6px}
  #info .type{display:inline-block;font-size:11px;padding:2px 8px;border-radius:999px;
              color:#fff;margin-bottom:8px}
  #info .kv{color:var(--sub);margin:3px 0;line-height:1.6;word-break:break-all}
  #info ul{margin:6px 0 0 16px;color:var(--sub);line-height:1.7}
  #hint{bottom:16px;right:16px;color:var(--sub)}
</style>
</head>
<body>
<canvas id="canvas"></canvas>

<div class="panel" id="title">
  <h1>LLM Wiki · 知识图谱</h1>
  <div class="meta" id="stats"></div>
</div>

<div class="panel" id="legend">
  <div class="row"><span class="dot" style="background:#2563eb"></span>source 来源页</div>
  <div class="row"><span class="dot" style="background:#7c3aed"></span>entity 实体页</div>
  <div class="row"><span class="dot" style="background:#059669"></span>concept 概念页</div>
  <div class="row"><span class="dot" style="background:#d97706"></span>synthesis 综合页</div>
  <div class="row"><span class="line"></span>EXTRACTED 双链</div>
  <div class="row"><span class="line dash"></span>INFERRED 推断</div>
</div>

<div class="panel" id="info"></div>
<div class="panel" id="hint">拖拽节点 · 滚轮缩放 · 悬停高亮邻居</div>

<script>
const GRAPH = __GRAPH_DATA__;
const TYPE_COLORS = __TYPE_COLORS__;

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let W = 0, H = 0, DPR = Math.min(window.devicePixelRatio || 1, 2);

function resize(){
  W = window.innerWidth; H = window.innerHeight;
  canvas.width = W * DPR; canvas.height = H * DPR;
  canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
}
window.addEventListener('resize', resize);

// ---- 建索引
const nodes = GRAPH.nodes.map((n, i) => Object.assign({}, n, {x: 0, y: 0, vx: 0, vy: 0, degree: 0}));
const byId = {}; nodes.forEach(n => byId[n.id] = n);
const links = GRAPH.edges.filter(e => byId[e.source] && byId[e.target]);
const neighbors = {}; nodes.forEach(n => neighbors[n.id] = new Set());
links.forEach(e => {
  byId[e.source].degree++; byId[e.target].degree++;
  neighbors[e.source].add(e.target); neighbors[e.target].add(e.source);
});

// ---- 初始布局：按社区分扇区摆在圆周上（确定性，避免每次打开都不一样）
function seedLayout(){
  const communities = {};
  nodes.forEach(n => { (communities[n.community] = communities[n.community] || []).push(n); });
  const keys = Object.keys(communities).sort((a,b) => a - b);
  const R = Math.min(W, H) * 0.34;
  let angle = -Math.PI / 2;
  keys.forEach(k => {
    const group = communities[k];
    const span = (Math.PI * 2) / keys.length;
    group.forEach((n, i) => {
      const a = angle + span * (i / Math.max(group.length, 1));
      const r = R * (0.72 + 0.28 * (i % 2));
      n.x = W / 2 + Math.cos(a) * r;
      n.y = H / 2 + Math.sin(a) * r;
    });
    angle += span;
  });
}

// ---- 力导向模拟
function simulate(steps){
  const k = Math.sqrt((W * H) / Math.max(nodes.length, 1)) * 0.55;
  for (let s = 0; s < steps; s++){
    // 斥力
    for (let i = 0; i < nodes.length; i++){
      const a = nodes[i];
      for (let j = i + 1; j < nodes.length; j++){
        const b = nodes[j];
        let dx = a.x - b.x, dy = a.y - b.y;
        let d2 = dx*dx + dy*dy;
        if (d2 < 1) { d2 = 1; dx = Math.random() - 0.5; dy = Math.random() - 0.5; }
        const d = Math.sqrt(d2);
        const force = (k * k) / d;
        const fx = (dx / d) * force * 0.02, fy = (dy / d) * force * 0.02;
        a.vx += fx; a.vy += fy; b.vx -= fx; b.vy -= fy;
      }
    }
    // 弹簧
    links.forEach(e => {
      const a = byId[e.source], b = byId[e.target];
      let dx = b.x - a.x, dy = b.y - a.y;
      const d = Math.max(Math.sqrt(dx*dx + dy*dy), 1);
      const rest = (e.kind === 'EXTRACTED' ? 105 : 165);
      const force = (d - rest) / d * 0.06;
      const fx = dx * force, fy = dy * force;
      a.vx += fx; a.vy += fy; b.vx -= fx; b.vy -= fy;
    });
    // 向心 + 阻尼 + 位移限制
    let maxStep = 0;
    nodes.forEach(n => {
      if (n.fixed) { n.vx = n.vy = 0; return; }
      n.vx += (W / 2 - n.x) * 0.0016;
      n.vy += (H / 2 - n.y) * 0.0016;
      n.vx *= 0.86; n.vy *= 0.86;
      const step = Math.sqrt(n.vx*n.vx + n.vy*n.vy);
      const cap = 30;
      if (step > cap) { n.vx = n.vx / step * cap; n.vy = n.vy / step * cap; }
      n.x += n.vx; n.y += n.vy;
      maxStep = Math.max(maxStep, step);
    });
    if (s > 60 && maxStep < 0.12) break;
  }
}

// ---- 视图变换
let view = {scale: 1, ox: 0, oy: 0};
const toScreen = (x, y) => ({x: x * view.scale + view.ox, y: y * view.scale + view.oy});
const toWorld = (x, y) => ({x: (x - view.ox) / view.scale, y: (y - view.oy) / view.scale});

let hovered = null, dragging = null, panning = null;

function radius(n){ return 6 + Math.min(n.degree, 8) * 1.4; }

function styleOf(name, key, fallback){
  const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  return v || fallback;
}

function draw(){
  const ink = styleOf('--ink', '#1f2937');
  const dim = styleOf('--dim', '#9ca3af');

  ctx.save();
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  ctx.clearRect(0, 0, W, H);

  const active = hovered ? neighbors[hovered.id] : null;

  // 边
  links.forEach(e => {
    const a = byId[e.source], b = byId[e.target];
    const pa = toScreen(a.x, a.y), pb = toScreen(b.x, b.y);
    const isNear = hovered && (e.source === hovered.id || e.target === hovered.id);
    ctx.beginPath();
    ctx.moveTo(pa.x, pa.y); ctx.lineTo(pb.x, pb.y);
    ctx.setLineDash(e.kind === 'INFERRED' ? [5, 5] : []);
    if (isNear){
      ctx.strokeStyle = TYPE_COLORS[hovered.type] || ink;
      ctx.lineWidth = 2.2; ctx.globalAlpha = 1;
    } else {
      ctx.strokeStyle = dim;
      ctx.lineWidth = e.kind === 'EXTRACTED' ? 1.3 : 1;
      ctx.globalAlpha = hovered ? 0.16 : (e.kind === 'EXTRACTED' ? 0.5 : 0.3);
    }
    ctx.stroke();
  });
  ctx.setLineDash([]);
  ctx.globalAlpha = 1;

  // 节点
  nodes.forEach(n => {
    const p = toScreen(n.x, n.y);
    const r = radius(n) * Math.max(view.scale, 0.6);
    const dimmed = hovered && n.id !== hovered.id && !active.has(n.id);
    ctx.globalAlpha = dimmed ? 0.2 : 1;

    ctx.beginPath();
    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
    ctx.fillStyle = TYPE_COLORS[n.type] || '#999';
    ctx.fill();
    if (n === hovered){
      ctx.lineWidth = 2.5; ctx.strokeStyle = ink; ctx.stroke();
    }

    if (!dimmed){
      ctx.font = (n === hovered ? '600 ' : '') + '12px -apple-system, "PingFang SC", sans-serif';
      ctx.fillStyle = ink;
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      const label = n.label.length > 26 ? n.label.slice(0, 25) + '…' : n.label;
      ctx.fillText(label, p.x, p.y + r + 4);
    }
    ctx.globalAlpha = 1;
  });

  ctx.restore();
}

// ---- 交互
function pick(mx, my){
  let best = null, bestDist = Infinity;
  nodes.forEach(n => {
    const p = toScreen(n.x, n.y);
    const d = Math.hypot(p.x - mx, p.y - my);
    const hit = Math.max(radius(n) * view.scale, 0.6) + 6;
    if (d < hit && d < bestDist){ best = n; bestDist = d; }
  });
  return best;
}

canvas.addEventListener('mousemove', ev => {
  const mx = ev.clientX, my = ev.clientY;
  if (dragging){
    const w = toWorld(mx, my);
    dragging.x = w.x; dragging.y = w.y; dragging.vx = dragging.vy = 0;
    draw(); return;
  }
  if (panning){
    view.ox += mx - panning.x; view.oy += my - panning.y;
    panning.x = mx; panning.y = my;
    draw(); return;
  }
  const hit = pick(mx, my);
  if (hit !== hovered){
    hovered = hit;
    canvas.style.cursor = hit ? 'pointer' : 'grab';
    showInfo(hit);
    draw();
  }
});

canvas.addEventListener('mousedown', ev => {
  const hit = pick(ev.clientX, ev.clientY);
  if (hit){ dragging = hit; hit.fixed = true; canvas.classList.add('dragging'); }
  else { panning = {x: ev.clientX, y: ev.clientY}; canvas.style.cursor = 'grabbing'; }
});

window.addEventListener('mouseup', () => {
  if (dragging){ dragging.fixed = false; dragging = null; }
  panning = null;
  canvas.classList.remove('dragging');
  canvas.style.cursor = 'grab';
});

canvas.addEventListener('wheel', ev => {
  ev.preventDefault();
  const factor = ev.deltaY < 0 ? 1.12 : 1 / 1.12;
  const before = toWorld(ev.clientX, ev.clientY);
  view.scale = Math.min(Math.max(view.scale * factor, 0.25), 4);
  const after = toWorld(ev.clientX, ev.clientY);
  view.ox += (after.x - before.x) * view.scale;
  view.oy += (after.y - before.y) * view.scale;
  view.ox = ev.clientX - before.x * view.scale;
  view.oy = ev.clientY - before.y * view.scale;
  draw();
}, {passive: false});

const infoEl = document.getElementById('info');
function showInfo(n){
  if (!n){ infoEl.style.display = 'none'; return; }
  const rows = [];
  rows.push('<span class="type" style="background:' + (TYPE_COLORS[n.type] || '#999') + '">' + n.type + '</span>');
  rows.push('<h2>' + n.label + '</h2>');
  rows.push('<div class="kv">文件：' + n.path + '</div>');
  if (n.updated) rows.push('<div class="kv">更新：' + n.updated + '</div>');
  if (n.tags.length) rows.push('<div class="kv">标签：' + n.tags.join(' · ') + '</div>');
  const nb = Array.from(neighbors[n.id]);
  if (nb.length){
    rows.push('<div class="kv">相连页面（' + nb.length + '）：</div><ul>');
    nb.sort().forEach(id => rows.push('<li>' + (byId[id] ? byId[id].label : id) + '</li>'));
    rows.push('</ul>');
  }
  infoEl.innerHTML = rows.join('');
  infoEl.style.display = 'block';
}

// ---- 启动
resize();
seedLayout();
simulate(420);
view.ox = 0; view.oy = 0; view.scale = 1;

const counts = {};
GRAPH.nodes.forEach(n => counts[n.type] = (counts[n.type] || 0) + 1);
document.getElementById('stats').innerHTML =
  '节点 <b>' + GRAPH.nodes.length + '</b> · 边 <b>' + GRAPH.edges.length + '</b><br>' +
  'EXTRACTED <b>' + GRAPH.edges.filter(e => e.kind === 'EXTRACTED').length + '</b> · ' +
  'INFERRED <b>' + GRAPH.edges.filter(e => e.kind === 'INFERRED').length + '</b><br>' +
  '社区 <b>' + new Set(GRAPH.nodes.map(n => n.community)).size + '</b> · 构建于 ' + GRAPH.built_at;

draw();
</script>
</body>
</html>
"""


def render_html(graph: dict) -> str:
    data = json.dumps(graph, ensure_ascii=False)
    return (
        HTML_TEMPLATE.replace("__GRAPH_DATA__", data)
        .replace("__TYPE_COLORS__", json.dumps(TYPE_COLORS, ensure_ascii=False))
    )


# ------------------------------------------------------------------ 主流程


def main() -> int:
    parser = argparse.ArgumentParser(description="构建 wiki 知识图谱")
    parser.add_argument("--open", action="store_true", help="生成后用默认浏览器打开 graph.html")
    parser.add_argument("--no-inferred", action="store_true", help="跳过第二遍推断，只保留双链边")
    args = parser.parse_args()

    random.seed(20260912)  # 布局可复现
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    pages = iter_pages()
    if not pages:
        print(C.red("wiki/ 下没有找到任何页面，先写内容再建图。"))
        return 1

    nodes = collect_nodes(pages)
    extracted = pass_one_extracted(pages)
    inferred = [] if args.no_inferred else pass_two_inferred(nodes, extracted)
    edges = extracted + inferred

    communities = detect_communities(nodes, edges)
    for node in nodes:
        node["community"] = communities[node["id"]]
        node["degree"] = sum(1 for e in edges if node["id"] in (e["source"], e["target"]))

    graph = {
        # 时间只精确到「日」：分钟级时间戳会让每次重建都产生无意义的 git 差异
        # （内容一字未变、只有时间变了），也与 health/lint 报告的时间精度保持一致。
        "built_at": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d"),
        "builder": "tools/build_graph.py",
        "method": {
            "pass1": "确定性解析 [[双链]] → EXTRACTED",
            "pass2": f"共享来源 Jaccard ≥ {INFERRED_MIN_SCORE} 推断 → INFERRED",
            "clustering": "Louvain 第一层（贪心模块度优化，纯标准库实现）",
        },
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "extracted": len(extracted),
            "inferred": len(inferred),
            "communities": len(set(communities.values())),
        },
        "nodes": nodes,
        "edges": edges,
    }

    json_path = GRAPH_DIR / "graph.json"
    html_path = GRAPH_DIR / "graph.html"
    json_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    html_path.write_text(render_html(graph), encoding="utf-8")

    stats = graph["stats"]
    print(C.bold("LLM Wiki · 知识图谱构建完成"))
    print(f"  节点 {C.green(str(stats['nodes']))} 个 · 边 {C.green(str(stats['edges']))} 条"
          f"（EXTRACTED {stats['extracted']} / INFERRED {stats['inferred']}）")
    print(f"  社区 {stats['communities']} 个 · 聚类算法：Louvain 第一层（贪心模块度优化）")
    print()
    print(C.bold("  度数最高的枢纽页面："))
    for node in sorted(nodes, key=lambda n: -n["degree"])[:5]:
        print(C.dim(f"    {node['degree']:>3}  {node['path']}"))
    print()
    print(f"  已写入 {relative(json_path)}")
    print(f"  已写入 {relative(html_path)}")

    if args.open:
        webbrowser.open(html_path.as_uri())
        print(C.dim("  已在默认浏览器中打开。"))
    else:
        print(C.dim("  打开方式：在 Finder 里双击 graph/graph.html，或加 --open 参数。"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
