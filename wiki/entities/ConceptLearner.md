---
title: "ConceptLearner（概念学习 Skill）"
type: entity
tags: [project, agent-skill, this-repo, example]
sources: [skill, agent, llm-context, vector-database, concept-relationship]
last_updated: 2026-09-13
---

# ConceptLearner

## 是什么

本仓库 `shihanyu125/concept-learning-skill` 里的那个真实存在的 [[Skill]]：输入任意一个概念名称，自动生成结构化的个人学习资料。

它是本 wiki 中 [[Skill]] 一页的**活例子**——不是抽象讲解，而是"确实这么做过一遍"的产物。

## 它生成的资料结构

固定七个部分：

1. 学习目标（学完能做到什么）
2. 核心问题（带着什么问题去读）
3. 一句话解释（+ 生活类比）
4. 核心机制 / 组成
5. 一个具体应用场景
6. 容易混淆的点 / 使用边界
7. 自测题 + 可核查的资料来源 + 学习者本人的理解与核查笔记

## 已产出

放在 `learning-materials/` 下，共四份，均已作为来源页登记进本 wiki：

- [[agent]] ｜ [[llm-context]] ｜ [[skill]] ｜ [[vector-database]]

另有一份跨概念的 [[concept-relationship]]（Agent、上下文、Skill 三者的关系）。

## 为什么它值得被记进 wiki

它把"如何学透一个概念"这套**一次性的方法**固化成可反复调用的流程——这正是 [[Skill]] 与 [[Workflow]] 思路的交汇处：

- 像 [[Workflow]]：步骤是固定写好的（七段式结构），因此结果稳定可复现
- 像 [[Skill]]：能力被封装成可复用、可迭代、可分享的文件包

## 关联

- [[Skill]]、[[Workflow]]、[[ProgressiveDisclosure]]
- [[agent]]、[[llm-context]]、[[skill]]、[[vector-database]]、[[concept-relationship]]

## 待补

- 仓库 README 里记录的"踩坑与解决"经验尚未进 wiki，可作为一条 source 摄进来
- 该 Skill 的 `SKILL.md` 元数据写法（`name` / `description` 具体如何写）尚未记录，而这是它能不能被触发的关键
