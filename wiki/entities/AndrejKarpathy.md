---
title: "AndrejKarpathy"
type: entity
tags: [person, ai-researcher, source-provider]
sources: [karpathy-llm-wiki-gist, llm-wiki-pattern]
last_updated: 2026-09-13
---

# AndrejKarpathy

## 是什么

AI 研究者、工程师，**[[LLMWiki]] 模式的提出者**。本仓库整套结构的思想来源。

## 与本站的关系

他发布了一份名为 `llm-wiki` 的 GitHub gist（约 2026 年 4 月上旬，**日期待核实**）及配套 X 长帖，提出用 LLM 持续编译维护个人知识库的做法。本仓库就是把这套思路落地的一次实践。

## 他提出的关键观点

1. **编译器 vs 解释器**：RAG 像解释器（每次重新解析），我们真正需要的是编译器（预先编译成可执行结构）。
2. **三层架构**：raw sources（你负责、不可变）/ wiki（LLM 完全拥有）/ schema（共同演进）。
3. **`CLAUDE.md` / `AGENTS.md` 是关键配置层**：没有它，命名与结构会漂。
4. **index.md 管空间，log.md 管时间**。
5. **验证责任在人**："human owns verification."
6. **idea file 是一种新的分发方式**：不必先交付完整 app，先交付一份克制的思路，让对方自己的 Agent 去落地。
7. **下一步方向**（他仍在探索）：用合成数据微调，把知识"记进权重"，而不只是放在上下文窗口里。

## 金句

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

> You rarely ever write or edit the wiki manually — it is the domain of the LLM.

## 自述的使用方式（值得对照）

- 原始资料放 `raw/`：文章、论文、代码仓库、数据集、图片
- 网页用 Obsidian Web Clipper 转 Markdown 存入
- 图片尽量下载到本地，方便 LLM 直接引用
- 把 Obsidian 当 IDE 式前端，同时看原始资料、编译后的 wiki 和派生输出
- 派生输出不限于文本：也可以是 Marp 幻灯片、matplotlib 图
- **偏好一次只 ingest 一份来源，并且亲自参与**——看摘要、看更新、再决定强调什么。不是无人值守的流水线

## 关联

- [[LLMWiki]] — 他提出的模式
- [[LlmWikiAgent]] — 该模式的一个公开实现
- [[RetrievalAugmentedGeneration]] — 他明确对照的对象
- [[ProgressiveDisclosure]] — 与 index.md 的设计思路相通
- 来源页：[[karpathy-llm-wiki-gist]]、[[llm-wiki-pattern]]

## 待补

- 原始 gist 的确切发布日与原始链接（目前只掌握 X 长帖链接与二手转述）
- 他在其他场合对"知识编译"的进一步论述
