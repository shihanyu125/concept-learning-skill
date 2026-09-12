---
title: "Karpathy 的 llm-wiki 原始材料"
type: source
tags: [llm-wiki, karpathy, gist, knowledge-management]
sources: [karpathy-llm-wiki-gist]
date: 2026-09-12
source_file: raw/karpathy-llm-wiki-gist.md
last_updated: 2026-09-13
---

# Karpathy 的 llm-wiki 原始材料

## Summary

对 Karpathy 公开材料（GitHub gist `llm-wiki` + 配套 X 长帖）的二手整理。核心洞察是一个计算机类比：**RAG 像"解释器"（每次执行都重新解析），我们要的是"编译器"（先把知识编译成可直接执行的结构）**。由此提出三层架构（raw / wiki / schema）与三个核心操作（ingest / query / lint）。

> ⚠️ **来源性质**：本页依据 gist 原文转述与多篇二手报道整理，**不是一手原文**。个别日期与数字在报道间存在出入，已在下方标出。

## Key Claims

- **编译器 vs 解释器**：RAG 每次提问都从零重新发现知识，不积累；LLM Wiki 先把资料编译成一层持续存在的知识层，再在上面查询。
- **三层架构与归属**：

  | 层 | 内容 | 谁负责 |
  |---|---|---|
  | Raw sources | 文章、论文、图片、数据、代码仓库。**不可变，LLM 只读不改** | 你 |
  | The wiki | LLM 生成的 Markdown 目录（摘要/实体/概念/对比/综合） | LLM 完全拥有 |
  | The schema | `CLAUDE.md` / `AGENTS.md`，规定组织方式与工作流 | 你 + LLM 共同演进 |

- **第三层（schema）最关键也最易被忽略**：没有它，命名、页面结构、引用习惯都会漂。
- **index.md 与 log.md 分工**：前者管空间（"这里都有什么"），后者管时间（"最近发生了什么"）；log 用统一前缀便于 `grep "^## \["` 解析。
- **一份来源会牵动 10–15 个既有 wiki 页面**——这是"编织"而非"追加"。
- **Query 的产出要回存进 wiki**——这是知识复利的关键，传统聊天里的发现会消失在历史记录中。
- **Lint 检查项**：矛盾、过时声明、孤儿页、缺独立页面的重要概念、缺失交叉引用、数据空白。
- **规模与边界**：Karpathy 自称在单一主题上积累约 100 篇文章、40 万字，且未直接写过一个字；在该规模下不一定需要复杂 RAG 基础设施——**但这是有前提的**，前提是他的资料已被编译成有结构的知识层。
- **human owns verification**：wiki 可以交给 LLM 维护，但验证责任在人。
- **它不只是方案，也是一种分发方式**：Karpathy 有意把它写成**克制的 idea file**，留出空间让对方自己的 Agent 结合场景落地。
- **已知瓶颈（社区）**：页面超几百页后 grep 变慢；结构会不受控地漂移。应对方向有 Binder（数据先行、渲染成 Markdown）与 Knowledge Engine（Markdown 层 + 内存层双层检索）。

## Key Quotes

> **Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.**

> **You rarely ever write or edit the wiki manually — it is the domain of the LLM.**

> **human owns verification.**

> 他为什么写成 gist：在 LLM agent 时代，不一定非要先分享一个完整 app 或一份完整代码，也可以先把思路写成一个相对抽象的 **idea file**，再交给对方的 Agent 去结合自己的场景落地。

## Connections

- [[LLMWiki]] — 本文对应的概念页，含完整机制
- [[AndrejKarpathy]] — 材料作者
- [[RetrievalAugmentedGeneration]] — 本文的核心对照对象（解释器 vs 编译器）
- [[Context]] — wiki 作为"外置知识层"，避免每次重灌上下文
- [[ProgressiveDisclosure]] — `index.md` 先读目录再钻页面，正是同一机制
- [[Agent]] — 整套系统由 Agent 驱动
- [[LlmWikiAgent]] — 参照该模式的公开实现

## Contradictions

**与既有页的张力（已标记，非错误）**：[[llm-wiki-pattern]]（参考实现 README 侧）把 `graph/` 与 `tools/` 描述为模式的标准组成部分；而 Karpathy 原始 gist 的**核心三层只有 raw / wiki / schema**，图谱与脚本属于后续实现的扩展。两者不冲突，但**层次不同**——读的时候注意区分"模式本体"与"某个实现的附加件"。

**待核实项**：
- gist 发布日期在报道间为 4 月 3 / 4 / 5 日，未统一
- gist 浏览量"1600 万+"为报道转述，未核实
- "100 篇文章 / 40 万字"为 Karpathy 自述规模，未独立核实
