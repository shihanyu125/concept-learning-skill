---
title: "LLM Wiki 模式（The LLM Wiki Pattern）"
type: source
tags: [llm-wiki, karpathy, methodology, meta]
sources: [llm-wiki-pattern]
date: 2026-09-12
source_file: raw/llm-wiki-pattern.md
last_updated: 2026-09-13
---

# LLM Wiki 模式（The LLM Wiki Pattern）

## Summary

本仓库所采用的整套方法的说明。核心主张：把原始资料丢进 `raw/`，让 AI 读完后自己写出一套互相链接的 wiki——人只负责"喂资料"和"提问"，不负责"写笔记"。每加一份新资料，wiki 变得更厚而不是更乱。

## Key Claims

- 与传统"搜索自己的笔记"的工具相反：你不是先整理好笔记再检索，而是只收集原始资料，由 AI 编译成结构化、有交叉引用、有矛盾标注、有综合结论的 wiki。
- 与 RAG 的关键差异：RAG 每次提问都从头推导知识、检索单位是原始文本块、无交叉引用、不积累；LLM Wiki 一次性编译并持续维护、检索单位是结构化页面、交叉引用预先建好、矛盾在摄取时就标出。
- 目录布局固定为 `raw/`（只读源）、`wiki/`（AI 维护的内容层，含 index/log/overview 与 sources/entities/concepts/syntheses 四个子目录）、`graph/`（知识图谱）、`tools/`（独立脚本）。
- 每个页面都带 YAML frontmatter（title / type / tags / sources / last_updated），页面之间用 `[[双链]]` 引用——双链既是给人读的，也是图谱的边。
- 四条工作流：摄取（Ingest）、提问（Query）、体检（Health / Lint）、建图（Build graph）。
- Health 与 Lint 有明确分工：Health 查结构完整性、零 LLM 调用、可每次会话跑；Lint 查内容质量、要花 token、建议每 10–15 次摄取跑一次。顺序是先 Health 后 Lint。
- 建图分两遍：第一遍确定性解析所有双链（边标 `EXTRACTED`），第二遍语义推断隐含关系（边标 `INFERRED` 带置信度，或 `AMBIGUOUS`）。
- 关键性质：纯文本、无服务器无数据库、天然带 git 版本历史、可作为 Obsidian vault 直接浏览。

## Key Quotes

> 你只管收集原始资料，AI 负责把它编译成结构化、有交叉引用、有矛盾标注、有综合结论的 wiki。**每加一份新资料，整个 wiki 变得更厚，而不是变得更乱。**

> Most knowledge tools make you search your own notes. This one reads everything you've collected and writes a structured wiki that compounds over time.（参考实现 README）

> 我原先以为"记笔记"这件事必须自己动手，AI 顶多帮我把某一段话写漂亮。这套模式让我意识到：**可以把"整理与连接"这件事外包出去**。（学习者批注）

## Connections

- [[LLMWiki]] — 本文对应的概念页
- [[AndrejKarpathy]] — 该模式的提出者
- [[LlmWikiAgent]] — 本仓库所参照的开源实现
- [[LlmWikiAgent]] — 其两遍建图（EXTRACTED / INFERRED）是本仓库 `tools/build_graph.py` 的参照
- [[Agent]] — 整套模式由一个 Agent（而非脚本流水线）驱动
- [[Skill]] — 参考实现本身就是一个 coding agent skill
- [[Context]] — 该模式要解决的正问题之一：不把全部原始资料重灌进上下文
- [[RetrievalAugmentedGeneration]] — 该模式明确对比并试图超越的对象

## Contradictions

**潜在张力（值得留意）**：[[LLMWiki]] 主张"一次性编译、之后持续维护"，而 [[RetrievalAugmentedGeneration]] 的常见实践是"每次查询现检索"。两者不是对错关系，而是适用场景不同——资料更新极频繁、且需要严格时效性的场景，RAG 的"现查现用"仍有优势；资料相对稳定、需要跨来源综合的场景，编译式 wiki 更省成本。此处记为**待观察**，暂不判定为矛盾。
