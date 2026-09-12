---
title: "Wiki Index"
type: synthesis
tags: [meta, index]
sources: []
last_updated: 2026-09-13
---

# Wiki Index

> 本 wiki 所有页面的目录。**每次摄取（ingest）后必须更新。**
> 用法：提问时先读这一页定位相关页面，再钻进具体页面——不要一上来就翻遍全库。

## Overview

- [Overview](overview.md) — 跨所有来源的"活的"综述，随每次摄取修订

## Sources

- [概念学习资料：Agent（智能体）](sources/agent.md) — Agent = 增强型 LLM，叠加检索/工具/记忆；关键在"下一步由谁决定"
- [概念学习资料：大模型的上下文](sources/llm-context.md) — 上下文窗口的定义、token 计量、截断行为
- [概念学习资料：Skill（技能包）](sources/skill.md) — Skill 的文件夹结构、YAML 元数据与渐进式披露
- [概念学习资料：向量数据库](sources/vector-database.md) — 按"意思有多接近"检索的数据库，RAG 的地基
- [概念关系说明：Agent、上下文、Skill 三者关系](sources/concept-relationship.md) — 不解释单个概念，而是把三者串成闭环
- [LLM Wiki 模式](sources/llm-wiki-pattern.md) — 本仓库所安装模式的目录布局与四条工作流
- [Karpathy 的 llm-wiki 原始材料](sources/karpathy-llm-wiki-gist.md) — 编译器 vs 解释器、三层架构、规模与边界（含待核实标注）

## Entities

- [Anthropic](entities/Anthropic.md) — Claude 的开发方；Agent/Workflow、Skill、Context 三个主题的主要来源
- [OpenAI](entities/OpenAI.md) — GPT 与 Agents SDK 的开发方；来源方之一
- [Pinecone](entities/Pinecone.md) — 向量数据库代表厂商
- [AndrejKarpathy](entities/AndrejKarpathy.md) — LLM Wiki 模式的提出者
- [LlmWikiAgent](entities/LlmWikiAgent.md) — 开源参考实现 `SamurAIGPT/llm-wiki-agent`，本仓库的规范参照
- [ConceptLearner](entities/ConceptLearner.md) — 本仓库里真实存在的概念学习 Skill，是 [[Skill]] 的活例子

## Concepts

- [Agent（智能体）](concepts/Agent.md) — 能自己拿主意、自己动手做事的 AI 程序
- [Context（上下文）](concepts/Context.md) — 模型单次请求能看到的全部内容及其上限
- [Skill（技能包）](concepts/Skill.md) — 打包好的专业能力文件夹，按需加载
- [ProgressiveDisclosure（渐进式披露）](concepts/ProgressiveDisclosure.md) — 按需分层加载，节约上下文的核心策略
- [Workflow（工作流）](concepts/Workflow.md) — 流程由代码写死；Agent 的对照面
- [VectorDatabase（向量数据库）](concepts/VectorDatabase.md) — 按语义相似度检索的数据库
- [RetrievalAugmentedGeneration（RAG）](concepts/RetrievalAugmentedGeneration.md) — 先检索、再生成；与 LLM Wiki 形成对照
- [LLMWiki（LLM Wiki 模式）](concepts/LLMWiki.md) — 编译式知识库：先编译，再查询

## Syntheses

- [Agent、上下文、Skill 三者是什么关系？](syntheses/agent-context-skill-relationship.md) — 三者的定位、闭环与两条关键因果链
- [为什么要「先编译」而不是「每次检索」？](syntheses/why-compile-not-retrieve.md) — 编译式 wiki 与 RAG 的差异、边界与不可让渡的原则
