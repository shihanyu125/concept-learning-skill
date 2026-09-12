---
title: "Wiki Log"
type: synthesis
tags: [meta, log]
sources: []
last_updated: 2026-09-13
---

# Wiki Log

> **只追加**的操作记录。每条以 `## [YYYY-MM-DD] <operation> | <title>` 开头，便于命令行解析：
>
> ```
> grep "^## \[" wiki/log.md | tail -10
> ```
>
> `<operation>` 取值：`scaffold` / `ingest` / `query` / `health` / `lint` / `graph`

## [2026-09-13] scaffold | 安装 LLM Wiki 结构

- 在本仓库根目录安装 LLM Wiki 模式（参照 `SamurAIGPT/llm-wiki-agent`）
- 建立 `raw/`、`wiki/`（含 index / log / overview 与 sources / entities / concepts / syntheses）、`graph/`、`tools/`
- 写入规范文件 `AGENTS.md`（页面格式、命名约定、四条工作流）
- 写入原始资料：`raw/llm-wiki-pattern.md`、`raw/karpathy-llm-wiki-gist.md`

## [2026-09-13] ingest | 概念学习资料：Agent（智能体）

- 来源：`learning-materials/agent.html`
- 新建 source 页 `sources/agent.md`
- 新建 concept 页 `concepts/Agent.md`、`concepts/Workflow.md`
- 新建 entity 页 `entities/Anthropic.md`、`entities/OpenAI.md`

## [2026-09-13] ingest | 概念学习资料：大模型的上下文

- 来源：`learning-materials/llm-context.html`
- 新建 source 页 `sources/llm-context.md`
- 新建 concept 页 `concepts/Context.md`、`concepts/ProgressiveDisclosure.md`

## [2026-09-13] ingest | 概念学习资料：Skill（技能包）

- 来源：`learning-materials/skill.html`
- 新建 source 页 `sources/skill.md`
- 新建 concept 页 `concepts/Skill.md`
- 新建 entity 页 `entities/ConceptLearner.md`

## [2026-09-13] ingest | 概念学习资料：向量数据库

- 来源：`learning-materials/vector-database.html`
- 新建 source 页 `sources/vector-database.md`
- 新建 concept 页 `concepts/VectorDatabase.md`、`concepts/RetrievalAugmentedGeneration.md`
- 新建 entity 页 `entities/Pinecone.md`
- 待办：原资料"我的理解与核查笔记"一节仍为空白模板，待补充后回填

## [2026-09-13] ingest | 概念关系说明：Agent、上下文、Skill 三者关系

- 来源：`learning-materials/concept-relationship.md`
- 新建 source 页 `sources/concept-relationship.md`
- 新建 synthesis 页 `syntheses/agent-context-skill-relationship.md`

## [2026-09-13] ingest | LLM Wiki 模式

- 来源：`raw/llm-wiki-pattern.md`
- 新建 source 页 `sources/llm-wiki-pattern.md`
- 新建 concept 页 `concepts/LLMWiki.md`
- 新建 entity 页 `entities/LlmWikiAgent.md`

## [2026-09-13] ingest | Karpathy 的 llm-wiki 原始材料

- 来源：`raw/karpathy-llm-wiki-gist.md`
- 新建 source 页 `sources/karpathy-llm-wiki-gist.md`
- 新建 entity 页 `entities/AndrejKarpathy.md`
- 新建 synthesis 页 `syntheses/why-compile-not-retrieve.md`
- 修订 `concepts/LLMWiki.md`：补入"编译器 vs 解释器"、三层归属表、规模边界与已知瓶颈
- 标记矛盾/差异：Karpathy 原始 gist 的核心三层为 raw/wiki/schema，`graph/` 与 `tools/` 属实现层扩展

## [2026-09-13] graph | 首次构建知识图谱

- 运行 `tools/build_graph.py`，输出 `graph/graph.json` 与 `graph/graph.html`

## [2026-09-13] health | 首次结构体检

- 运行 `tools/health.py`，结果见 `wiki/health-report.md`
