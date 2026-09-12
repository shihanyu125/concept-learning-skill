---
title: "Overview — 跨来源综述"
type: synthesis
tags: [meta, overview, synthesis]
sources: [agent, llm-context, skill, vector-database, concept-relationship, llm-wiki-pattern, karpathy-llm-wiki-gist]
last_updated: 2026-09-13
---

# Overview — 跨来源综述

> 本页是**跨所有来源的"活的"综述**，随每次摄取修订。它回答的不是"某一页说了什么"，而是"把这些页放在一起看，整体图景是什么"。

## 这个 wiki 目前在收集什么

一句话：**都在回答同一个问题——怎么让 AI 不只是"聊得好"，而是"真能干活、且越干越省力"。**

已摄取 7 份来源，可归为三条线：

### 线一：AI 的"做事能力"从哪来

- [[Agent]] 是这条线的中心：能自己拿主意、自己动手做事，靠 [[RetrievalAugmentedGeneration|检索]]、工具、记忆三项增强。
- 它的边界由 [[Workflow]] 划出：**下一步由谁决定**——代码写死是 Workflow，模型动态决定才是 Agent。
- 一个反复被强调的工程立场：**能用简单方案就不要上 Agent**。

### 线二：为什么"记不住"是核心约束

- [[Context]] 是硬约束：窗口有限、超出即截断、窗口内信息被平等对待（不会自动"记住重点"）。
- [[ProgressiveDisclosure]] 是最重要的应对策略：按需分层加载，而不是一次全塞。
- 这条约束解释了很多设计：为什么 [[Skill]] 要"平时只预读名片"、为什么 [[RetrievalAugmentedGeneration]] 要控制片段数量、为什么 [[LLMWiki]] 要先把知识编译到外部。

### 线三：怎么让知识"沉淀下来"而不是每次重来

- [[VectorDatabase]] + [[RetrievalAugmentedGeneration]]：把外部知识按需搬进上下文——但**每次提问都要重新推导，不积累**。
- [[LLMWiki]]：反过来，**先把知识编译成结构化的持久层**，再在上面查询；提问的产出还能回存，形成复利。
- 这条线的思想源头是 [[AndrejKarpathy]] 的 gist：**RAG 像解释器，编译式 wiki 像编译器**。
- 本仓库已有的 [[ConceptLearner]] 是同一哲学在另一层面的体现：把"学透一个概念"的方法固化成可复用流程。

## 三条线怎么接在一起

```
        ┌──────────── 约束层 ────────────┐
        │  [[Context]] 有限 ← 这是一切设计的起点 │
        └───────────────┬────────────────┘
                        │
        ┌───────────────┴────────────────┐
        │                                │
   省着用（[[ProgressiveDisclosure]]）   搬进来（[[RetrievalAugmentedGeneration]]）
        │                                │
   [[Skill]] 按需加载             [[VectorDatabase]] 按语义找
        │                                │
        └───────────────┬────────────────┘
                        ▼
                  [[Agent]] 据此行动
                        │
                        ▼
        沉淀成 [[LLMWiki]]（编译式，可复利）
```

## 目前 wiki 的整体判断

1. **最有价值的三个概念页**：[[Agent]]、[[Context]]、[[Skill]]——它们构成了理解其余一切的基础设施。
2. **最值得注意的一组对照**：[[Workflow]] vs [[Agent]]（控制权归属）、[[RetrievalAugmentedGeneration|RAG]] vs [[LLMWiki]]（解释器 vs 编译器）。这两组对照的共同点是：**都不是谁取代谁，而是适用场景不同**。
3. **贯穿全部来源的一条原则**：**human owns verification**。wiki 可以交给 AI 维护，但验证责任在人——这也是本 wiki 给所有不确定信息标"待核实"的原因。

## 已知的空白（下次摄取该补什么）

按价值排序：

1. **MCP（Model Context Protocol）** —— 与 [[Skill]] 强相关，目前 wiki 完全没有页面。见 [[Anthropic]]。
2. **向量数据库的选型与竞品** —— 目前只有 [[Pinecone]] 一家、单一视角（该页来源还是厂商自家文档）。见 [[VectorDatabase]]。
3. **RAG 的模型厂商侧一手材料** —— [[RetrievalAugmentedGeneration]] 目前缺 [[OpenAI]]/[[Anthropic]] 的官方最佳实践。
4. **"多 Agent 协作"** —— [[Agent]] 页面只提及未展开。
5. **本仓库自身的经验** —— `README.md` 里的踩坑记录、[[ConceptLearner]] 的 `SKILL.md` 元数据写法，都还没进 wiki。
6. **三个悬而未决的学习者疑问**（分别记在三个 source 页里）：如何判断一个产品算 Workflow 还是 Agent；"能记住偏好"的 AI 靠长期记忆还是重灌上下文；Skill 与提示词的边界在哪。

## 修订记录

- **2026-09-13** 首次成稿。摄取 7 份来源，建立 8 个概念页、6 个实体页、2 个综合页。
