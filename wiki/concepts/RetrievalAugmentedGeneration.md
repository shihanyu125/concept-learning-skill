---
title: "RetrievalAugmentedGeneration（RAG / 检索增强生成）"
type: concept
tags: [rag, retrieval, grounding, pattern]
sources: [vector-database, llm-wiki-pattern]
last_updated: 2026-09-13
---

# RetrievalAugmentedGeneration（RAG）

## 定义

**RAG = 先检索、再生成**：回答前先从外部资料里找出相关片段，把它们作为参考资料喂给模型，让模型基于这些材料作答——而不是只靠模型参数里的"记忆"。

目的：让 AI 能准确回答它"没背过"的、只存在于你自己文件里的内容。

## 核心机制

标准流程（见 [[VectorDatabase]]）：

1. 把你的文档切成小段
2. 每段转成向量，存进向量数据库
3. 你提问时，先把问题转成向量
4. 去数据库里找"最相关"的几段（Top-K）
5. 把这几段作为参考资料拼进 [[Context]]，让模型据此作答

## 使用边界

- **依赖检索质量**：检索没找对，回答就跟着错——"垃圾进，垃圾出"。
- **占用上下文**：塞进来的片段和其他内容争抢窗口，所以片段数量要权衡。
- **不积累**：每次提问都要重新检索、重新推导，知识不会被沉淀下来。（这正是 [[LLMWiki]] 想改进的地方）

## RAG vs LLM Wiki

| RAG | LLM Wiki |
|---|---|
| 每次提问都从头推导知识 | 一次性编译好，之后持续维护 |
| 检索单位是原始文本块 chunk | 检索单位是结构化 wiki 页面 |
| 没有交叉引用 | 交叉引用预先建好 |
| 矛盾通常在提问时才（可能）暴露 | 矛盾在摄取时就标出 |
| 不积累 | 每份新资料都让 wiki 更丰富 |

**这不是"谁取代谁"**：资料更新极频繁、强时效的场景，RAG 的"现查现用"有优势；资料相对稳定、需要跨来源综合的场景，编译式 wiki 更省成本。

## 关联

- [[VectorDatabase]] — RAG 的地基
- [[Agent]] — RAG 是 Agent"检索"能力的主要实现
- [[Context]] — RAG 的落点是往上下文里塞材料
- [[LLMWiki]] — 明确以 RAG 为对照对象
- [[why-compile-not-retrieve]] — 深入分析这一组对照的边界：为什么"先编译"更好、以及在什么条件下这个结论不成立
- 来源页：[[vector-database]]、[[llm-wiki-pattern]]

## 来源

- Pinecone 官方文档（向量检索）
- 参考实现 `SamurAIGPT/llm-wiki-agent` README 中的 RAG 对照表
- 见 [[Pinecone]]、[[LlmWikiAgent]]
