---
title: "LlmWikiAgent（参考实现）"
type: entity
tags: [project, open-source, reference-implementation, llm-wiki]
sources: [llm-wiki-pattern]
last_updated: 2026-09-13
---

# LlmWikiAgent

## 是什么

开源项目 `SamurAIGPT/llm-wiki-agent`（MIT 许可），本仓库所安装的 [[LLMWiki]] 模式的**规范参照实现**。

它自身就是一个 coding agent 的 [[Skill]]：把它克隆下来，用 Agent 打开，往 `raw/` 丢资料，然后说"ingest"即可——无需 API Key，无需配置 Python。

## 它的关键设计

### 1. 配置文件是核心

`CLAUDE.md` / `AGENTS.md` 这类 schema 文件告诉 Agent 如何维护 wiki——页面格式、命名约定、四条工作流。**这是整套机制最关键的一个文件**，本仓库的 `AGENTS.md` 即由它改写而来。

### 2. 两遍建图

- 第一遍：**确定性**解析所有 `[[wikilinks]]` → 边标 `EXTRACTED`
- 第二遍：**语义推断**双链没覆盖的隐含关系 → 边标 `INFERRED`（带置信度）或 `AMBIGUOUS`
- 再用社区检测（Louvain）按主题聚类
- 带 SHA256 缓存，只重新处理变更过的页面
- 输出自包含的 `graph.html`（vis.js）

### 3. Health 与 Lint 分离

| | health | lint |
|---|---|---|
| 范围 | 结构完整性 | 内容质量 |
| LLM 调用 | 零 | 有（语义分析） |
| 成本 | 免费 | 消耗 token |
| 频率 | 每次会话 | 每 10–15 次摄取 |
| 检查项 | 空文件、index 同步、log 同步 | 孤儿页、断链、矛盾、缺口 |

### 4. 它提供的脚本

`tools/health.py`、`tools/lint.py`、`tools/build_graph.py`、`tools/ingest.py`、`tools/query.py`、`tools/heal.py`（自修复：自动找出并补建缺失的结构性概念与实体页）、`tools/pdf2md.py`、`tools/file_to_md.py`。

### 5. 支持 21 种格式

`.md .pdf .docx .pptx .xlsx .xls .html .htm .txt .csv .json .xml .rst .rtf .epub .ipynb .yaml .yml .tsv .wav .mp3` —— 非 Markdown 通过 markitdown 自动转换。

## 与本仓库的差异

本仓库只安装了**结构 + 规范 + 三个零依赖脚本**（`health.py` / `lint.py` / `build_graph.py`），未安装依赖 LLM 或第三方库的 `ingest.py` / `query.py` / `heal.py`——这三个在 Agent 环境里由 Agent 本身承担，不需要额外脚本。

## 关联

- [[LLMWiki]] — 它实现的模式
- [[Skill]] — 它本身是一个 Skill
- [[AndrejKarpathy]] — 模式的提出者
- 来源页：[[llm-wiki-pattern]]

## 待补

- `tools/heal.py` 的自修复策略（怎么判断"缺失的结构性概念"）值得单独摄一份资料进来
- `tools/ingest.py` 的提示词设计（如何从一份长文档里决定该建哪些实体/概念页）是好问题，目前 wiki 答不出
