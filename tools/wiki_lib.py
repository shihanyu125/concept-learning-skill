"""LLM Wiki 公共工具库。

被 tools/ 下的脚本共用：定位目录、解析 frontmatter、抽取双链。
只用 Python 标准库，无需安装任何依赖。

用法（在仓库根目录）：
    python3 tools/health.py
"""

from __future__ import annotations

import re
from pathlib import Path

# ---------------------------------------------------------------- 目录定位

TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent
RAW_DIR = REPO_ROOT / "raw"
WIKI_DIR = REPO_ROOT / "wiki"
GRAPH_DIR = REPO_ROOT / "graph"
INDEX_PATH = WIKI_DIR / "index.md"
LOG_PATH = WIKI_DIR / "log.md"
OVERVIEW_PATH = WIKI_DIR / "overview.md"

#: 元页面：目录、日志、综述。它们被排除在"孤儿页"统计之外
#: （因为 index.md 会链接几乎所有页面，若计入则永远找不到孤儿）。
META_PAGES = {"index", "log", "overview"}

#: 由脚本生成的报告页。它们是**诊断产物**而非知识内容：
#: 不该被 index.md 收录，也不该被算作孤儿页。
GENERATED_PAGES = {"health-report", "lint-report"}

#: frontmatter 必须包含的字段
REQUIRED_FIELDS = ("title", "type", "tags", "sources", "last_updated")

#: type 的合法取值
VALID_TYPES = ("source", "entity", "concept", "synthesis")

#: index.md 必须包含的段落标题
INDEX_SECTIONS = ("Overview", "Sources", "Entities", "Concepts", "Syntheses")

_FRONTMATTER_RE = re.compile(r"^\ufeff?\s*---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
_WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
#: 围栏代码块与行内代码——里面的 [[...]] 只是举例，不算真链接
_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


# ---------------------------------------------------------------- 文件遍历


def iter_pages() -> list[Path]:
    """返回 wiki/ 下所有 .md 页面（按路径排序）。"""
    if not WIKI_DIR.is_dir():
        return []
    return sorted(p for p in WIKI_DIR.rglob("*.md") if p.is_file())


def page_name(path: Path) -> str:
    """页面标识：文件名去掉 .md。双链就指向这个名字。"""
    return path.stem


def relative(path: Path) -> str:
    """相对仓库根目录的路径，用于报告显示。"""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def rel_within_wiki(path: Path) -> str:
    """相对 wiki/ 的路径，用于 index.md 里的 Markdown 链接。"""
    try:
        return str(path.relative_to(WIKI_DIR))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------- frontmatter

#: 允许的简易 YAML 写法：
#:   key: value
#:   key: "带引号的值"
#:   key: []            空列表
#:   key: [a, b]        行内列表
#:   key:               块状列表（后续若干 "- item" 行）
#:   key:               块状标量（后续若干缩进行，拼成一段文本）
def _unescape_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def _split_inline_list(value: str) -> list[str]:
    return [_unescape_scalar(item) for item in value.split(",") if item.strip()]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """解析页面开头的 YAML frontmatter。

    返回 (frontmatter 字典, 正文)。没有 frontmatter 时返回 ({}, 原文)。
    只实现 wiki 用到的 YAML 子集，不引入 PyYAML 依赖。
    """
    text = text.lstrip("\ufeff")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    block = match.group(1)
    body = text[match.end():]
    data: dict = {}

    lines = block.split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1

        # 跳过空行与注释
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        # 顶层键必须有缩进以外的前缀 "key:"
        if ":" not in raw:
            continue
        key, _, rest = raw.partition(":")
        key = key.strip()
        rest = rest.strip()
        if not key:
            continue

        if rest == "":  # 可能是块状列表或块状标量，也可能为空
            items: list[str] = []
            scalar_lines: list[str] = []
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    i += 1
                    if items or scalar_lines:
                        break
                    continue
                if ":" in nxt and not nxt.lstrip().startswith("-"):
                    break
                stripped = nxt.strip()
                if stripped.startswith("-"):
                    items.append(_unescape_scalar(stripped[1:]))
                    i += 1
                elif nxt.startswith((" ", "\t")):
                    scalar_lines.append(stripped)
                    i += 1
                else:
                    break
            if items:
                data[key] = items
            elif scalar_lines:
                data[key] = " ".join(scalar_lines)
            else:
                data[key] = ""
        elif rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            data[key] = _split_inline_list(inner) if inner else []
        else:
            data[key] = _unescape_scalar(rest)

    return data, body


def read_page(path: Path) -> tuple[dict, str]:
    """读取页面，返回 (frontmatter, 正文)。"""
    return parse_frontmatter(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- 双链


def strip_code(text: str) -> str:
    """去掉围栏代码块与行内代码。

    文档里经常出现「页面之间用 `[[双链]]` 互相引用」这种**举例说明**，
    那不是真链接，不该被当成断链或图谱的边。
    """
    return _INLINE_CODE_RE.sub(" ", _FENCE_RE.sub(" ", text))


def extract_wikilinks(text: str) -> list[str]:
    """抽出页面里的所有 [[双链]]（已排除代码块与行内代码里的示例）。

    兼容 Obsidian 的别名与锚点写法：[[Page|显示文字]] -> Page，[[Page#小节]] -> Page。

    表格里写别名必须转义竖线（`[[Page\\|别名]]`），否则会把表格列切开；
    转义后按 "|" 切分会残留一个结尾反斜杠，所以要再 rstrip 一次，
    否则 `Page\\` 会被当成不存在的页面、误报成断链。
    """
    names: list[str] = []
    for raw in _WIKILINK_RE.findall(strip_code(text)):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        target = target.rstrip("\\").strip()
        if target:
            names.append(target)
    return names


def build_link_map(pages: list[Path]) -> dict[str, set[str]]:
    """返回 {页面名: 它指向的页面名集合}。"""
    return {page_name(p): set(extract_wikilinks(read_page(p)[1])) for p in pages}


def inbound_counts(link_map: dict[str, set[str]], exclude_meta: bool = True) -> dict[str, int]:
    """统计每页的入链数。

    exclude_meta=True 时不计来自 index/log/overview 的链接——
    否则 index.md 会链到几乎每一页，孤儿页永远统计不出来。
    """
    counts = {name: 0 for name in link_map}
    for source, targets in link_map.items():
        if exclude_meta and source in META_PAGES:
            continue
        for target in targets:
            if target in counts:
                counts[target] += 1
    return counts


# ---------------------------------------------------------------- 日志


def read_log_entries() -> list[dict]:
    """解析 log.md 里的条目。

    约定格式：`## [YYYY-MM-DD] <operation> | <title>`
    """
    if not LOG_PATH.exists():
        return []
    pattern = re.compile(r"^##\s*\[(\d{4}-\d{2}-\d{2})\]\s*([a-zA-Z_-]+)\s*\|\s*(.+?)\s*$")
    entries: list[dict] = []
    for line in LOG_PATH.read_text(encoding="utf-8").split("\n"):
        match = pattern.match(line.strip())
        if match:
            entries.append(
                {"date": match.group(1), "operation": match.group(2), "title": match.group(3)}
            )
    return entries


# ---------------------------------------------------------------- 输出着色


class C:
    """终端颜色。仅在 TTY 下生效。"""

    _ON = None

    @classmethod
    def _enabled(cls) -> bool:
        import sys

        return sys.stdout.isatty()

    @classmethod
    def _wrap(cls, code: str, text: str) -> str:
        if not cls._enabled():
            return text
        return f"\033[{code}m{text}\033[0m"

    @classmethod
    def red(cls, t: str) -> str:
        return cls._wrap("31", t)

    @classmethod
    def green(cls, t: str) -> str:
        return cls._wrap("32", t)

    @classmethod
    def yellow(cls, t: str) -> str:
        return cls._wrap("33", t)

    @classmethod
    def bold(cls, t: str) -> str:
        return cls._wrap("1", t)

    @classmethod
    def dim(cls, t: str) -> str:
        return cls._wrap("2", t)
