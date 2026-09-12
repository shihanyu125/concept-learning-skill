---
title: "概念学习资料：Agent（智能体）"
type: source
tags: [concept-material, ai-agent, learning-notes]
sources: [agent]
date: 2026-09-04
source_file: raw/agent.html
last_updated: 2026-09-13
---

# 概念学习资料：Agent（智能体）

> **来源说明**：本页依据的事实来源是 `raw/agent.html`（事实来源层，只读）。
> 该文件同时也在 `learning-materials/agent.html`——那是**作品输出区**，内容可能被继续修订；两处内容经 md5 校验一致（`c51bd38ada5bbb63506492f572c79324`）。
> 引用时以 `raw/` 为准。

## Summary

一份由概念学习 Skill 生成、经学习者本人核查修改的概念资料。核心结论：Agent 是"能自己拿主意、自己动手做事"的 AI 程序，其内核是被增强的大语言模型——在模型之上叠加**检索、工具、记忆**三种能力。理解 Agent 的关键不在"会不会用工具"，而在"下一步由谁决定"。

## Key Claims

- Agent = 被增强的 LLM，增强的三项能力是：检索（Retrieval）、工具（Tools）、记忆（Memory）。
- Agent 与 Workflow 的本质区别是**控制权归属**：Workflow 的流程由代码预先写死，Agent 由模型动态决定。
- 不是"会调用工具"就叫 Agent——流程写死的自动化脚本属于 Workflow。
- 不是"越自主越好"：能用简单方案解决就不要上 Agent；任务简单、步骤固定时，一次普通 LLM 调用或 Workflow 更划算。
- Agent 适合"目标开放、步骤无法提前枚举"的任务。

## Key Quotes

> **生活类比：** 普通 AI 像一位"只会给你建议的顾问"——你问它"怎么订机票"，它告诉你步骤，但不动手。Agent 则像一位"能直接替你办事的助理"。（原资料）

> 我以前把 AI 都看成差不多的东西……而 Agent 是另一回事：它能在我的授权下，自己去访问文件、调用工具，把很多原本需要"懂电脑的专业人士"才能完成的事，从头到尾帮我办完。（学习者批注）

## Connections

- [[Agent]] — 本文对应的概念页，含完整机制与边界
- [[Workflow]] — 全文最核心的一组对照：控制权在代码还是在模型
- [[Context]] — 上下文是 Agent 决策的"原料"，决定它一次能看清多少
- [[Skill]] — Skill 是让通用 Agent 按需"变专业"的能力包
- [[RetrievalAugmentedGeneration]] — "检索"能力的典型落地方式
- [[VectorDatabase]] — 检索能力常见的地基
- [[Anthropic]] — 本文主要依据其《Building Effective Agents》一文
- [[OpenAI]] — 本文另一来源，其 Agents SDK 文档定义了 Agent 的构成

## Contradictions

暂无。与既有页面的表述一致。

## 学习者的疑问（待后续资料回答）

现实里那些"自动回复客服""自动整理邮件"的功能，到底该怎么判断它算 Workflow 还是 Agent？
