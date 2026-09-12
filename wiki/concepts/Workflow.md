---
title: "Workflow（工作流）"
type: concept
tags: [orchestration, control-flow, contrast-concept]
sources: [agent, ]
last_updated: 2026-09-13
---

# Workflow（工作流）

## 定义

**Workflow 是流程由代码预先写死、按固定步骤执行的自动化方案。**

它与 [[Agent]] 构成一组核心对照。判断标准只有一条：**下一步由谁决定？**

| | 工作流 Workflow | 智能体 Agent |
|---|---|---|
| **控制权在谁** | 代码（预先写死流程） | 模型（自己动态决定） |
| **类比** | 有轨列车，轨道提前铺好 | 自动驾驶汽车，按路况变路线 |
| **优点** | 稳定、可预测、易调试、省钱 | 灵活，能应对开放的复杂任务 |
| **缺点** | 只能处理固定流程 | 不确定、可能无效循环、更费 token、难排查 |

## 使用边界

- **不是"会调用工具"就算 Agent**：很多自动化脚本也调工具，但流程写死了，那是 Workflow。
- **能用简单方案就不要上 Agent**：任务简单、步骤固定、结果可预测时，Workflow 或一次普通 LLM 调用更好。
- Workflow 并非"低级方案"——**可预测、可调试、成本低**是它的真实优势，工程上往往优先选它。

## 与自动化的区别（易混）

[[Automation]] 和 Workflow 都会给人"到点、按规矩自动发生"的印象，但**管的是两件事**：

| | 管什么 | 例子 |
|---|---|---|
| [[Automation]] | **何时跑**（触发时机） | "每天早上 9 点"、"每周一三五" |
| Workflow | **怎么跑**（执行流程） | 步骤一 → 步骤二 → 步骤三，写死在代码里 |

一条自动化任务内部完全可以执行一段 Workflow（定时触发一段固定流程）；而 Workflow 本身**不关心自己什么时候被触发**。**可以叠加，不互相替代。**

## 关联

- [[Agent]] — 最主要的对照概念
- [[Automation]] — 近邻：一个管触发时机，一个管执行流程
- [[Skill]] — 三者常被并列讨论：Skill 沉淀"怎么做"的知识、Workflow 定义"怎么跑"的流程、Automation 登记"何时跑"
- [[ConceptLearner]] — 一个更接近"固定流程"的能力包：把学习步骤固化成可复用流程，这正是 Skill 与 Workflow 思路的交汇处
- 来源页：[[agent]]、[[]]

## 来源

- Anthropic《Building Effective Agents》——对 Agent 与 Workflow 的区分是该文反复强调的核心
- `raw/2026-09-12--.md` — "自动化 vs Workflow"的对照（属类比推论，非该文原文直述）
- 见 [[Anthropic]]、[[Agent]]
