---
title: "ProgressiveDisclosure（渐进式披露）"
type: concept
tags: [context-management, agent-skill, mechanism]
sources: [skill, concept-relationship]
last_updated: 2026-09-13
---

# ProgressiveDisclosure（渐进式披露）

## 定义

**渐进式披露 = 按需、分层地加载信息**，而不是一次性把所有内容都塞进 [[Context]]。

它是 [[Skill]] 能够"平时不占地方、用时才展开"的底层机制，本质是对稀缺资源（上下文窗口）的一种节约策略。

## 核心机制：三层加载

| 层 | 加载什么 | 目的 |
|---|---|---|
| 第 1 层 | 所有技能的 `name` + `description` | 判断"该用哪个" |
| 第 2 层 | 命中技能的 `SKILL.md` 全文 | 拿到完整指令 |
| 第 3 层 | 该技能引用的附加文件 | 只在真正需要时读 |

## 为什么重要

对照 [[Context]] 的三条推论：上下文**空间有限**，塞太多无关内容会挤掉关键信息。渐进式披露把"要不要读、读多少"的决定权延后到真正需要的那一刻，从而：

- **省空间**：不相关的能力不占窗口
- **提准确率**：窗口里留下的都是相关材料，模型"看得清重点"
- **可扩展**：可以装很多 Skill 而不炸掉上下文

## 使用边界

- 依赖 AI 对 `name` / `description` 的正确判断——**元数据写得差，该加载时不加载**。
- 并不适合"必须全量上下文才能判断"的任务；这类场景下分层反而可能漏掉关键信息。

## 关联

- [[Skill]] — 渐进式披露最主要的应用
- [[Context]] — 它要节约的资源
- [[ContextManagement]] — 补位的一环：内容**已经进了窗口之后**怎么办（本页管"别乱吃"，它管"吃多了怎么消化"）
- [[Token]] — 节约上下文，省的就是 token
- [[Agent]] — Agent 每个循环都在消耗上下文，因此受益
- [[LLMWiki]] — wiki 的 index.md 也是同一思路：先看目录，再决定读哪页
- 来源页：[[skill]]、[[concept-relationship]]

## 来源

- Anthropic 工程博客《Equipping agents for the real world with Agent Skills》系统阐述了该机制
- 见 [[Anthropic]]、[[Skill]]
