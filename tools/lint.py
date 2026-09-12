#!/usr/bin/env python3
"""wiki 内容体检 — 确定性部分。

LLM Wiki 规范把 lint 定义为"内容质量检查"。其中**能确定性地算出来的部分**由本脚本负责：

  1. 断链        —— [[双链]] 指向了不存在的页面
  2. 孤儿页      —— 没有任何来自其他页面的入链（不含 index/log/overview 的链接）
  3. 格式违规    —— frontmatter 缺字段、type 取值非法、last_updated 格式不对
  4. 缺页候选    —— 被多个页面提及却始终没有独立页面的名字（按提及次数排序）

**不含**的部分（需要语义理解，由 Agent 完成，不是脚本能干的）：
  - 跨页面的**矛盾**（两页对同一件事说法不一致）
  - 被新来源取代的**过时声明**
  - 应该建链却漏建的**缺失交叉引用**
  - 可以通过外部搜索填补的**数据空白**

用法：
    python3 tools/lint.py
    python3 tools/lint.py --save        # 另存到 wiki/lint-report.md
    python3 tools/lint.py --json
    python3 tools/lint.py --min-mentions 2   # "缺页候选"的最低提及次数

退出码：0 = 无问题；1 = 发现问题。
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date

from wiki_lib import (
    C,
    GENERATED_PAGES,
    INDEX_PATH,
    META_PAGES,
    REQUIRED_FIELDS,
    VALID_TYPES,
    WIKI_DIR,
    build_link_map,
    extract_wikilinks,
    inbound_counts,
    iter_pages,
    page_name,
    read_page,
    rel_within_wiki,
)

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def check_broken_links(pages) -> tuple[list[dict], Counter]:
    """找出指向不存在页面的双链。

    用 wiki_lib.extract_wikilinks 而不是就地写正则——它会先剥掉代码块与
    行内代码，免得把「页面之间用 `[[双链]]` 引用」这类**举例**误判成断链。
    """
    existing = {page_name(p) for p in pages}
    mentions: Counter = Counter()
    issues: list[dict] = []

    for path in pages:
        _, body = read_page(path)
        for name in extract_wikilinks(body):
            mentions[name] += 1
            if name not in existing:
                issues.append({"page": page_name(path), "path": rel_within_wiki(path), "target": name})

    return issues, mentions


def check_orphans(pages) -> list[dict]:
    """找出没有入链的页面（排除元页面与脚本生成的报告页）。"""
    link_map = build_link_map(pages)
    counts = inbound_counts(link_map, exclude_meta=True)
    skip = META_PAGES | GENERATED_PAGES
    return sorted(
        (
            {"page": name, "path": rel_within_wiki(p)}
            for p in pages
            if (name := page_name(p)) not in skip and counts.get(name, 0) == 0
        ),
        key=lambda item: item["page"],
    )


def check_frontmatter(pages) -> list[dict]:
    """检查 frontmatter 是否符合规范。"""
    issues: list[dict] = []
    for path in pages:
        fm, _ = read_page(path)
        rel = rel_within_wiki(path)

        if not fm:
            issues.append({"page": page_name(path), "path": rel, "detail": "缺少 YAML frontmatter"})
            continue

        for field in REQUIRED_FIELDS:
            if field not in fm:
                issues.append({"page": page_name(path), "path": rel, "detail": f"缺少字段 `{field}`"})

        page_type = fm.get("type")
        if page_type and page_type not in VALID_TYPES:
            issues.append(
                {
                    "page": page_name(path),
                    "path": rel,
                    "detail": f"type 取值非法：`{page_type}`（应为 {'/'.join(VALID_TYPES)} 之一）",
                }
            )

        updated = fm.get("last_updated", "")
        if updated and not _DATE_RE.match(str(updated)):
            issues.append(
                {"page": page_name(path), "path": rel, "detail": f"last_updated 格式应为 YYYY-MM-DD，当前为 `{updated}`"}
            )

        for list_field in ("tags", "sources"):
            value = fm.get(list_field)
            if value is None:
                continue
            if not isinstance(value, list):
                issues.append(
                    {
                        "page": page_name(path),
                        "path": rel,
                        "detail": f"`{list_field}` 应为列表，当前为 `{value}`",
                    }
                )
    return issues


def build_report(min_mentions: int) -> dict:
    pages = iter_pages()
    broken, mentions = check_broken_links(pages)
    orphans = check_orphans(pages)
    fm_issues = check_frontmatter(pages)

    existing = {page_name(p) for p in pages}
    missing_pages = [
        {"name": name, "mentions": count}
        for name, count in mentions.most_common()
        if name not in existing and count >= min_mentions
    ]

    problem_count = len(broken) + len(orphans) + len(fm_issues)
    return {
        "generated_at": date.today().isoformat(),
        "tool": "tools/lint.py",
        "page_count": len(pages),
        "problem_count": problem_count,
        "broken_links": broken,
        "orphan_pages": orphans,
        "frontmatter_issues": fm_issues,
        "missing_page_candidates": missing_pages,
        "semantic_checks": "未执行：矛盾 / 过时声明 / 缺失交叉引用 / 数据空白 —— 需由 Agent 语义检查",
    }


def render(report: dict) -> str:
    lines = [C.bold("LLM Wiki · 内容体检（lint · 确定性部分）")]
    lines.append(C.dim(f"生成时间 {report['generated_at']} · 共 {report['page_count']} 个页面"))
    lines.append("")

    lines.append(C.bold(f"1. 断链：{len(report['broken_links'])} 处"))
    for item in report["broken_links"]:
        lines.append(C.red(f"   ✗ {item['path']} 中的 [[{item['target']}]] 无对应页面"))
    if not report["broken_links"]:
        lines.append(C.green("   ✓ 所有双链都指向真实存在的页面"))
    lines.append("")

    lines.append(C.bold(f"2. 孤儿页：{len(report['orphan_pages'])} 处"))
    for item in report["orphan_pages"]:
        lines.append(C.yellow(f"   ⚠ {item['path']} 没有任何其他页面链接到它"))
    if not report["orphan_pages"]:
        lines.append(C.green("   ✓ 每个页面都有入链"))
    lines.append("")

    lines.append(C.bold(f"3. 格式违规：{len(report['frontmatter_issues'])} 处"))
    for item in report["frontmatter_issues"]:
        lines.append(C.red(f"   ✗ {item['path']} — {item['detail']}"))
    if not report["frontmatter_issues"]:
        lines.append(C.green("   ✓ 所有页面的 frontmatter 都符合规范"))
    lines.append("")

    candidates = report["missing_page_candidates"]
    lines.append(C.bold(f"4. 缺页候选：{len(candidates)} 个"))
    if candidates:
        for item in candidates:
            lines.append(f"   ⚠ {item['name']}（被提及 {item['mentions']} 次，但还没有自己的页面）")
    else:
        lines.append(C.green("   ✓ 没有反复被提及却缺页的名字"))
    lines.append("")

    lines.append(C.dim(f"说明：{report['semantic_checks']}"))
    lines.append("")

    if report["problem_count"]:
        lines.append(C.yellow(f"结论：发现 {report['problem_count']} 个确定性问题。"))
    else:
        lines.append(C.green("结论：确定性检查全部通过。"))
    return "\n".join(lines)


def render_markdown(report: dict) -> str:
    lines = [
        "---",
        'title: "Lint Report"',
        "type: synthesis",
        "tags: [meta, lint-report]",
        "sources: []",
        f"last_updated: {report['generated_at']}",
        "---",
        "",
        "# Lint Report — 内容体检（确定性部分）",
        "",
        f"生成时间：{report['generated_at']} · 由 `tools/lint.py` 生成 · 共 {report['page_count']} 个页面",
        "",
        f"**问题总数：{report['problem_count']}**",
        "",
        f"## 1. 断链（{len(report['broken_links'])}）",
        "",
    ]
    lines += (
        [f"- `{i['path']}` 中的 `[[{i['target']}]]` 无对应页面" for i in report["broken_links"]] or ["- 无"]
    )

    lines += ["", f"## 2. 孤儿页（{len(report['orphan_pages'])}）", ""]
    lines += [f"- `{i['path']}` 没有入链" for i in report["orphan_pages"]] or ["- 无"]

    lines += ["", f"## 3. 格式违规（{len(report['frontmatter_issues'])}）", ""]
    lines += [f"- `{i['path']}` — {i['detail']}" for i in report["frontmatter_issues"]] or ["- 无"]

    lines += ["", f"## 4. 缺页候选（{len(report['missing_page_candidates'])}）", ""]
    lines += (
        [f"- `{i['name']}` 被提及 {i['mentions']} 次但无独立页面" for i in report["missing_page_candidates"]]
        or ["- 无"]
    )

    lines += [
        "",
        "## 未覆盖的检查项",
        "",
        f"{report['semantic_checks']}",
        "",
        "---",
        "",
        "> 本文件由脚本生成，可重新运行 `python3 tools/lint.py --save` 覆盖。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="wiki 内容体检（确定性部分）")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    parser.add_argument("--save", action="store_true", help="另存到 wiki/lint-report.md")
    parser.add_argument("--min-mentions", type=int, default=3, help="缺页候选的最低提及次数")
    args = parser.parse_args()

    report = build_report(args.min_mentions)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render(report))

    if args.save:
        target = WIKI_DIR / "lint-report.md"
        target.write_text(render_markdown(report), encoding="utf-8")
        if not args.json:
            print()
            print(C.dim(f"已保存到 wiki/lint-report.md"))

    return 1 if report["problem_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
