---
title: "OpenAI"
type: entity
tags: [company, ai-lab, source-provider]
sources: [agent, llm-context]
last_updated: 2026-09-13
---

# OpenAI

## 是什么

AI 公司，GPT 系列模型与 Agents SDK 的开发者，本 wiki 中 [[Agent]] 与 [[Context]] 两个页面的主要来源方之一。

## 提供的核心材料

| 主题 | 文档 |
|---|---|
| [[Agent]] | Agents SDK 文档《Quickstart》——用代码定义并运行一个 Agent、逐步加入工具与多 Agent 协作的最小示例 |
| [[Agent]] | Agents SDK 文档《Agent definitions》——说明 **Agent = 模型 + 指令 + 工具 / 护栏 / 交接** 的核心构成 |
| [[Context]] | 文档《Conversation state》之 Managing the context window ——定义上下文窗口、token 计量、截断行为，并给出 128k 示例 |

## 值得记住的一点

**Agent 的构成式**：模型 + 指令 + 工具（+ 护栏、交接）。这与 [[Anthropic]] 的"增强型 LLM（检索 / 工具 / 记忆）"说法互为印证——两家用不同切法描述同一件事。

## 关联

- [[Anthropic]] — 另一家主要来源方
- [[Agent]]、[[Context]]

## 待补

可补充：RAG 相关的官方最佳实践文档、Responses API 与上下文管理的关系——目前 wiki 中 [[RetrievalAugmentedGeneration]] 的来源只有 [[Pinecone]] 一家，缺少模型厂商侧的一手材料。
