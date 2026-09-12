---
title: "Agent、上下文、Skill 三者是什么关系？"
type: synthesis
tags: [cross-concept, agent, context, skill, analysis]
sources: [concept-relationship, agent, llm-context, skill]
last_updated: 2026-09-13
---

# Agent、上下文、Skill 三者是什么关系？

> 回答的问题：这三个概念各自是什么角色？它们怎么协作？为什么缺一不可？

## 一句话回答

**[[Agent]] 是干活的"人"，[[Context]] 是它眼前的"工作台"，[[Skill]] 是它抽屉里"随用随取的工具手册"。**

## 各自的定位

| 概念 | 一句话定位 | 角色 |
|---|---|---|
| [[Agent]] | 能自己拿主意、自己动手做事的 AI 程序 | 执行者 / 决策者 |
| [[Context]] | 模型一次性"能看到"的全部内容的容量 | 工作记忆 / 工作台 |
| [[Skill]] | 打包好的、按需加载的专业能力文件夹 | 可复用的知识包 |

## 闭环是怎么转起来的

```
Skill ──按需加载──▶ Context ──提供决策原料──▶ Agent
  ▲                                            │
  └────────── Agent 在执行中调用新 Skill ◀──────┘
```

1. **[[Skill]] 把专业知识按需"装进" [[Context]]** —— 靠 [[ProgressiveDisclosure]]，平时不占地方
2. **[[Context]] 把"装了什么"提供给 [[Agent]]** 做决策
3. **[[Agent]] 据此更专业地行动**，并在执行中继续读写上下文

## 为什么缺一不可

| 缺了谁 | 会怎样 |
|---|---|
| 缺 Agent | 工具包和工作台都在，但没人动手 |
| 缺 Context | Agent 没有工作台，看不到目标、历史和工具结果，寸步难行 |
| 缺 Skill | Agent 是"全能但泛泛"的通用助手，每次都要从头教一遍 |

## 两条最关键的因果链

**① [[Context]] → [[Agent]] 的能力上限**

上下文**大小** = Agent 的眼界；上下文**内容** = Agent 的判断质量；窗口**满**了会遗忘 —— 这是长任务里 Agent 表现下滑的常见原因。所以"精简地喂信息"不是优化技巧，而是硬约束。

**② [[Skill]] → [[Context]] 的成本控制**

Skill 的存在意义之一就是**不让上下文被一次性塞满大段指令**。有无 Skill 的对照：

| 维度 | 没有 Skill | 有 Skill |
|---|---|---|
| 接到新任务 | 每次从头说明流程 | 直接调用现成 Skill |
| 专业程度 | 泛泛、不精 | 按需临时"变专业" |
| 上下文占用 | 一次性塞大段指令 | 渐进式披露，按需加载 |
| 知识沉淀 | 用完即散 | 固化成文件，可复用可迭代 |
| 结果一致性 | 每次可能不一样 | 流程固定，更稳定可复现 |

## 延伸阅读

- 单个概念：[[Agent]]、[[Context]]、[[Skill]]
- 机制：[[ProgressiveDisclosure]]、[[Workflow]]
- 相关应用：[[RetrievalAugmentedGeneration]]、[[VectorDatabase]]、[[LLMWiki]]
- 原始材料：[[concept-relationship]]、[[agent]]、[[llm-context]]、[[skill]]
