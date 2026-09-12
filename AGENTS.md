# LLM Wiki — Schema & Workflow Instructions

> 本仓库采用 **LLM Wiki 模式**（Andrej Karpathy 提出的思路）：`raw/` 里放原始资料，AI 读完自动写出一套互相链接的持久化 wiki。
> wiki 由 AI 维护，你只负责丢资料和提问。规范参考开源实现：`SamurAIGPT/llm-wiki-agent`。

## 目录布局

```
raw/          # 不可变的原始资料（只读，不要改）——把要学的文档丢这里
wiki/         # 由 AI 维护的内容层
  index.md    # 所有页面的目录，每次 ingest 后更新
  log.md      # 只追加的操作日志
  overview.md # 跨所有来源的"活的"综述
  health-report.md  # 由 tools/health.py 生成的体检报告（脚本覆盖重写，不入 index 五段）
  lint-report.md    # 由 tools/lint.py 生成的体检报告（脚本覆盖重写，不入 index 五段）
  sources/    # 每份原始资料一页摘要（kebab-case.md）
  entities/   # 人物、公司、项目、产品（TitleCase.md）
  concepts/   # 概念、框架、方法、理论（TitleCase.md）
  syntheses/  # 回答过的提问，回填成页面（kebab-case.md）
graph/        # 自动生成的知识图谱
  graph.json  # 节点/边数据
  graph.html  # 浏览器里打开即可交互的可视化
tools/        # 无依赖的 Python 脚本
  health.py      # 结构体检（零 LLM 调用）
  lint.py        # 内容体检（确定性部分）
  build_graph.py # 生成知识图谱
```

## 页面格式（强制）

`wiki/` 下**每个** `.md` 页面都必须以此 frontmatter 开头：

```yaml
---
title: "页面标题"
type: source | entity | concept | synthesis
tags: []
sources: []       # 该页内容所依据的来源 slug 列表
last_updated: YYYY-MM-DD
---
```

补充约定：

- `title` 用中文自然标题，加引号，避免冒号被 YAML 误解析。
- `type` 只能取上面四个值之一。`index.md` / `log.md` / `overview.md` 是**元页面**，统一用 `type: synthesis` 并带 `meta` 标签；`health-report.md` / `lint-report.md` 是**脚本生成物**，同样用 `synthesis` + `meta`，但不列入 `index.md` 的五个段。
- `sources` 语义：非 source 页面填"内容来自哪些来源页面"的 slug 列表（如 `[agent, llm-context]`）；source 页面自身即来源，填自身 slug。
- source 页面额外允许两个字段：`date`（资料日期）、`source_file`（原始文件路径）。
- `last_updated` 用 `YYYY-MM-DD`，每次实质修改该页都要更新。
- 页面之间用 `[[双链]]`（wikilinks）互相引用，链接目标写**页面文件名去掉 `.md` 的部分**，例如 `[[Agent]]`、`[[ConceptLearner]]`。
- 禁止出现指向不存在页面的断链——写完新页必须回头补链。

## 命令（自然语言即可）

| 你说 | AI 做什么 |
|---|---|
| `ingest raw/xxx.md` | 读原始资料 → 写 source 页 → 更新 index/overview → 建/更 entity 与 concept 页 → 记 log |
| `query: 主要讲了什么？` | 读 index 找相关页 → 综合回答 → 问你要不要存成 synthesis 页 |
| `health` | 跑 `python3 tools/health.py`（快速，零成本） |
| `lint` | 内容质量检查：孤儿页、断链、矛盾、缺口 |
| `build graph` | 跑 `python3 tools/build_graph.py`，生成 graph.json + graph.html |

## Ingest 工作流

1. 完整读入原始文件（非 Markdown 先转成 Markdown）
2. 读 `wiki/index.md` 和 `wiki/overview.md`，掌握当前 wiki 状态
3. 写 `wiki/sources/<slug>.md`（slug = 原文件名的 kebab-case）
4. 更新 `wiki/index.md` 的 Sources 段
5. 必要时修订 `wiki/overview.md`
6. 为文中关键的人物/公司/项目建或更新 `entities/` 页
7. 为关键概念/方法建或更新 `concepts/` 页
8. 若与既有页内容冲突，在两侧页面的 `## 矛盾 / Contradictions` 段落标出
9. 追加 `wiki/log.md`：`## [YYYY-MM-DD] ingest | <标题>`
10. 收尾校验：检查断链、确认新页都已进 index、输出变更摘要

## Query / Lint / Build 工作流

- **Query**：读 index → 读相关页 → 带 `[[双链]]` 引用作答 → 询问是否回填为 `syntheses/` 页。
- **Lint**：查孤儿页（无入链）、断链、跨页矛盾、过期摘要、缺失的 entity/concept 页（被 3 个以上页面提到却没有自己的页面）、数据缺口（wiki 答不出的问题 → 建议补哪些资料）。
  - **`tools/lint.py` 只覆盖其中的确定性子集**（断链 / 孤儿页 / frontmatter / 缺页候选）。**矛盾、过时声明、缺失交叉引用必须由 Agent 通读一遍**——脚本在报告里会明确列出这几项"未执行"。
  - **「缺页候选」会漏报**（实测 MCP 被 3 个页面提到却没报出）。判据只数反复出现的候选词，对缩写与"用来定义主角的对照概念"不敏感，需人工再数一遍。
  - `tools/health.py` 的「日志覆盖」**只查 source 页有没有 ingest 记录**，`lint` / `graph` / `health` 三类操作是否漏记要自己比对。
  - 人工清单另见 `wiki/overview.md` 与项目记忆里登记的 7 项交叉验证。
- **Build graph**：两遍构建。第一遍确定性解析所有 `[[wikilinks]]` → 标 `EXTRACTED`；第二遍语义推断隐含关系 → 标 `INFERRED`（带置信度）。用社区检测按主题聚类，输出 `graph/graph.json` + `graph/graph.html`。

## 命名约定

- source / synthesis 页：`kebab-case.md`
- entity / concept 页：`TitleCase.md`（如 `Agent.md`、`VectorDatabase.md`）
- 同一实体的命名必须唯一且稳定，否则双链会断裂

## index.md 格式

固定包含五个段，缺段会被 `tools/lint.py` 报出来：

```markdown
## Overview
## Sources
## Entities
## Concepts
## Syntheses
```

## log.md 格式

每条以 `## [YYYY-MM-DD] <operation> | <title>` 开头，便于 grep：

```
grep "^## \[" wiki/log.md | tail -10
```

`<operation>` 取值范围：`ingest` / `query` / `health` / `lint` / `graph` / `scaffold`

## 铁律

1. `raw/` 是**只读**的——AI 只读不写，不修改、不删除、不重命名里面的文件。
2. `wiki/` 完全由 AI 维护，人不要手工改（改了就失去一致性）。
3. 每写完一个页面，都要保证它至少被 `index.md` 收录，并尽量被至少一个别的页面用 `[[双链]]` 引用到。
4. 不确定的信息标"待核实"，不要伪造来源。
