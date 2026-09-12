---
title: "Workflow（工作流）"
type: concept
tags: [orchestration, control-flow, contrast-concept]
sources: [agent]
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

## 关联

- [[Agent]] — 最主要的对照概念
- [[ConceptLearner]] — 一个更接近"固定流程"的能力包：把学习步骤固化成可复用流程，这正是 Skill 与 Workflow 思路的交汇处
- 来源页：[[agent]]

## 来源

- Anthropic《Building Effective Agents》——对 Agent 与 Workflow 的区分是该文反复强调的核心
- 见 [[Anthropic]]、[[Agent]]
