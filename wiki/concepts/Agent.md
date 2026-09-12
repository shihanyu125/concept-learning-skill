---
title: "Agent（智能体）"
type: concept
tags: [ai-agent, llm, autonomy, core-concept]
sources: [agent, concept-relationship, llm-wiki-pattern]
last_updated: 2026-09-13
---

# Agent（智能体）

## 定义

Agent 是**能自己拿主意、自己动手做事的 AI 程序**。它不是一个新模型，而是"被增强的大语言模型"：在 LLM 之上叠加三种能力——

| 能力 | 作用 |
|---|---|
| 检索 Retrieval | 去外部查资料、查数据，不只靠脑内参数 |
| 工具 Tools | 调用外部工具：搜网页、跑代码、查库、发邮件 |
| 记忆 Memory | 跨步骤保持状态连贯 |

## 核心机制

Agent 的运行是一个**循环**：观察当前情况 → 决定下一步 → 调用工具 → 把结果放回上下文 → 再决定下一步，直到目标达成。每一轮循环，上下文都在被读写——所以 [[Context]] 的容量直接决定 Agent 能"记住"多少、"看清"多少。

## 最重要的边界：Agent ≠ Workflow

判断标准只有一条：**下一步由谁决定**。

- 流程由代码预先写死 → [[Workflow]]（有轨列车，轨道提前铺好）
- 流程由模型动态决定 → Agent（自动驾驶，按路况变路线）

推论：不是"会调用工具"就叫 Agent。流程写死的自动化脚本也调工具，但那是 Workflow。

## 使用边界

- **不是越自主越好。** 能用简单方案解决就不要上 Agent：任务简单、步骤固定时，一次普通 LLM 调用或 Workflow 更便宜、更稳、更好排查。
- Agent 适合**目标开放、步骤无法提前枚举**的任务。
- 代价：不确定、可能陷入无效循环、更费 token、难排查。

## 关联

- [[Workflow]] — 最核心的对照概念
- [[Context]] — Agent 的"工作台"与决策原料
- [[Skill]] — 让通用 Agent 按需变成专业 Agent
- [[RetrievalAugmentedGeneration]] — "检索"能力的主要落地方式
- [[VectorDatabase]] — 检索常见的地基
- [[LLMWiki]] — 一个由 Agent 驱动、而非脚本驱动的知识系统实例
- 来源页：[[agent]]、[[concept-relationship]]、[[llm-wiki-pattern]]

## 来源

- Anthropic《Building Effective Agents》(2024-12)
- OpenAI Agents SDK 文档（Quickstart / Define agents）
- 见 [[Anthropic]]、[[OpenAI]]
