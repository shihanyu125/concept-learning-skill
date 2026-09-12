#!/usr/bin/env python3
"""wiki 结构体检 — 零 LLM 调用，免费，可以每次会话都跑。

检查三项（对应 LLM Wiki 规范里的 health 职责，只管结构、不管内容质量）：

  1. 空页 / 残页 —— 只有 frontmatter 没有正文，或正文过短（rate-limit 损坏的典型症状）
  2. 目录同步   —— index.md 里列的页面 vs 磁盘上实际存在的页面，两个方向都要查
  3. 日志覆盖   —— 每个 sources/*.md 是否在 log.md 里有对应的 ingest 记录

用法：
    python3 tools/health.py              # 打印报告
    python3 tools/health.py --json       # 机器可读输出
    python3 tools/health.py --save       # 另存到 wiki/health-report.md
    python3 tools/health.py --min-body 120   # 自定义"正文过短"的阈值

退出码：0 = 无问题；1 = 发现问题。
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from difflib import SequenceMatcher

from wiki_lib import (
    C,
    GENERATED_PAGES,
    INDEX_PATH,
    INDEX_SECTIONS,
    LOG_PATH,
    WIKI_DIR,
    iter_pages,
    page_name,
    read_log_entries,
    read_page,
    rel_within_wiki,
    relative,
)

#: 正文短于这个字符数（去掉空白后）就算"残页"
DEFAULT_MIN_BODY = 80

#: 标题相似度达到这个比例就认为"日志里记过这件事"
TITLE_SIMILARITY = 0.7


def _similar(a: str, b: str) -> bool:
    """标题模糊匹配：短的包含在长的里，或者相似度足够高。"""
    if not a or not b:
        return False
    if a in b or b in a:
        return True
    return SequenceMatcher(None, a, b).ratio() >= TITLE_SIMILARITY


def check_stub_pages(min_body: int) -> list[dict]:
    """找出空页 / 残页。"""
    issues: list[dict] = []
    for path in iter_pages():
        _, body = read_page(path)
        stripped = re.sub(r"\s+", "", body)
        if not stripped:
            issues.append(
                {
                    "page": page_name(path),
                    "path": rel_within_wiki(path),
                    "detail": "正文完全为空（只剩 frontmatter）",
                    "chars": 0,
                }
            )
        elif len(stripped) < min_body:
            issues.append(
                {
                    "page": page_name(path),
                    "path": rel_within_wiki(path),
                    "detail": f"正文过短（{len(stripped)} 个非空白字符，阈值 {min_body}）",
                    "chars": len(stripped),
                }
            )
    return issues


def check_index_sync() -> dict:
    """检查 index.md 与磁盘上实际文件是否双向一致。"""
    # index.md 与 log.md 是元页面，本来就不该（也不必）被自己收录；
    # health-report / lint-report 是脚本生成的诊断产物，同样不进目录。
    # overview.md 则应当在 index 的 Overview 段里出现，所以不排除。
    self_referential = {"index", "log"} | GENERATED_PAGES
    disk_pages = {page_name(p) for p in iter_pages()} - self_referential

    if not INDEX_PATH.exists():
        return {
            "index_exists": False,
            "missing_from_index": sorted(disk_pages),
            "listed_but_absent": [],
            "missing_sections": list(INDEX_SECTIONS),
        }

    text = INDEX_PATH.read_text(encoding="utf-8")
    # index.md 用标准 Markdown 链接；也容忍 [[双链]] 写法
    listed = set(re.findall(r"\]\(([^)]+?)\.md\)", text))
    listed = {name.split("/")[-1] for name in listed}
    listed |= set(re.findall(r"\[\[([^\[\]|#]+)", text))
    listed = {name.strip() for name in listed}

    missing_sections = [
        section for section in INDEX_SECTIONS if not re.search(rf"^##\s+{section}\s*$", text, re.M)
    ]
    return {
        "index_exists": True,
        "missing_from_index": sorted(disk_pages - listed),
        "listed_but_absent": sorted(listed - disk_pages),
        "missing_sections": missing_sections,
    }


def check_log_coverage() -> list[dict]:
    """每个 source 页都要有一条对应的 ingest 日志。

    日志里的标题常常是页面标题的简写，所以用模糊匹配而不是字符串相等。
    """
    entries = read_log_entries()
    ingests = [re.sub(r"\s+", "", e["title"]) for e in entries if e["operation"] == "ingest"]

    issues: list[dict] = []
    sources_dir = WIKI_DIR / "sources"
    if not sources_dir.is_dir():
        return issues

    for path in sorted(sources_dir.glob("*.md")):
        _, body = read_page(path)
        title_match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
        headline = title_match.group(1).strip() if title_match else page_name(path)
        normalized = re.sub(r"\s+", "", headline)

        if any(_similar(normalized, title) for title in ingests):
            continue
        issues.append(
            {
                "page": page_name(path),
                "path": rel_within_wiki(path),
                "detail": f"log.md 里找不到对应的 ingest 记录（期望标题含「{headline}」）",
            }
        )
    return issues


def build_report(min_body: int) -> dict:
    stubs = check_stub_pages(min_body)
    index = check_index_sync()
    log_issues = check_log_coverage()

    problems = (
        len(stubs)
        + len(index["missing_from_index"])
        + len(index["listed_but_absent"])
        + len(index["missing_sections"])
        + len(log_issues)
    )
    return {
        "generated_at": date.today().isoformat(),
        "tool": "tools/health.py",
        "llm_calls": 0,
        "page_count": len(list(iter_pages())),
        "problem_count": problems,
        "stub_pages": stubs,
        "index_sync": index,
        "log_coverage": log_issues,
    }


def render(report: dict) -> str:
    lines: list[str] = []
    lines.append(C.bold("LLM Wiki · 结构体检（health）"))
    lines.append(C.dim(f"生成时间 {report['generated_at']} · LLM 调用 {report['llm_calls']} 次 · 共 {report['page_count']} 个页面"))
    lines.append("")

    # 1. 空页 / 残页
    lines.append(C.bold(f"1. 空页 / 残页：{len(report['stub_pages'])} 处"))
    if report["stub_pages"]:
        for item in report["stub_pages"]:
            lines.append(C.red(f"   ✗ {item['path']} — {item['detail']}"))
    else:
        lines.append(C.green("   ✓ 无空页，所有页面都有正文"))
    lines.append("")

    # 2. 目录同步
    index = report["index_sync"]
    problems = len(index["missing_from_index"]) + len(index["listed_but_absent"]) + len(index["missing_sections"])
    lines.append(C.bold(f"2. 目录同步：{problems} 处"))
    if not index["index_exists"]:
        lines.append(C.red("   ✗ wiki/index.md 不存在"))
    else:
        if index["missing_from_index"]:
            for name in index["missing_from_index"]:
                lines.append(C.red(f"   ✗ 磁盘上存在但 index.md 未收录：{name}"))
        if index["listed_but_absent"]:
            for name in index["listed_but_absent"]:
                lines.append(C.red(f"   ✗ index.md 列出了但磁盘上没有：{name}"))
        if index["missing_sections"]:
            lines.append(C.red(f"   ✗ index.md 缺少段落：{', '.join(index['missing_sections'])}"))
        if not problems:
            lines.append(C.green("   ✓ index.md 与实际文件完全一致，五个段落齐全"))
    lines.append("")

    # 3. 日志覆盖
    lines.append(C.bold(f"3. 日志覆盖：{len(report['log_coverage'])} 处"))
    if report["log_coverage"]:
        for item in report["log_coverage"]:
            lines.append(C.red(f"   ✗ {item['detail']}"))
    else:
        lines.append(C.green(f"   ✓ 全部 source 页都有对应的 ingest 记录（{relative(LOG_PATH)}）"))
    lines.append("")

    if report["problem_count"]:
        lines.append(C.yellow(f"结论：发现 {report['problem_count']} 个结构问题，建议先修复再跑 lint。"))
    else:
        lines.append(C.green("结论：结构完整，可以安全地进行后续操作。"))
    return "\n".join(lines)


def render_markdown(report: dict) -> str:
    index = report["index_sync"]
    lines = [
        "---",
        'title: "Health Report"',
        "type: synthesis",
        "tags: [meta, health-report]",
        "sources: []",
        f"last_updated: {report['generated_at']}",
        "---",
        "",
        "# Health Report — 结构体检",
        "",
        f"生成时间：{report['generated_at']} · 由 `tools/health.py` 生成（零 LLM 调用）· 共 {report['page_count']} 个页面",
        "",
        f"**问题总数：{report['problem_count']}**",
        "",
        "## 1. 空页 / 残页",
        "",
    ]
    if report["stub_pages"]:
        lines += [f"- `{i['path']}` — {i['detail']}" for i in report["stub_pages"]]
    else:
        lines.append("- 无")

    lines += ["", "## 2. 目录同步", ""]
    if index["missing_from_index"]:
        lines += [f"- 磁盘上存在但 index.md 未收录：`{n}`" for n in index["missing_from_index"]]
    if index["listed_but_absent"]:
        lines += [f"- index.md 列出了但磁盘上没有：`{n}`" for n in index["listed_but_absent"]]
    if index["missing_sections"]:
        lines.append(f"- index.md 缺少段落：{', '.join(index['missing_sections'])}")
    if not (index["missing_from_index"] or index["listed_but_absent"] or index["missing_sections"]):
        lines.append("- 无")

    lines += ["", "## 3. 日志覆盖", ""]
    if report["log_coverage"]:
        lines += [f"- `{i['path']}` — {i['detail']}" for i in report["log_coverage"]]
    else:
        lines.append("- 无")

    lines += ["", "---", "", "> 本文件由脚本生成，可随时重新运行 `python3 tools/health.py --save` 覆盖。", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="wiki 结构体检（零 LLM 调用）")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    parser.add_argument("--save", action="store_true", help="另存到 wiki/health-report.md")
    parser.add_argument("--min-body", type=int, default=DEFAULT_MIN_BODY, help="正文过短的阈值（字符数）")
    args = parser.parse_args()

    report = build_report(args.min_body)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render(report))

    if args.save:
        target = WIKI_DIR / "health-report.md"
        target.write_text(render_markdown(report), encoding="utf-8")
        if not args.json:
            print()
            print(C.dim(f"已保存到 {relative(target)}"))

    return 1 if report["problem_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
