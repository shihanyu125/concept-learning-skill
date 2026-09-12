---
title: "概念学习资料：Skill（技能包）"
type: source
tags: [concept-material, agent-skill, learning-notes]
sources: [skill]
date: 2026-09-04
source_file: learning-materials/skill.html
last_updated: 2026-09-13
---

# 概念学习资料：Skill（技能包）

## Summary

说明 Skill 是什么、靠什么机制"按需"生效。核心结论：Skill 是一个打包好的专业能力文件夹（核心是带 YAML 元数据的 `SKILL.md`，旁边可带脚本与资源），AI 平时泛泛全能，遇到相关任务才加载它，临时变成该领域专家。

## Key Claims

- Skill = 一个文件夹，核心文件 `SKILL.md` 里写指令，可附带脚本和资源。
- `SKILL.md` 顶部必须有 YAML 元数据，至少包含 `name` 和 `description`——这是技能的"名片"，AI 靠它判断"什么时候该用这个技能"。
- **渐进式披露（progressive disclosure）**：分三层按需加载——先读全部技能的 name+description → 确定相关后读该技能 `SKILL.md` 全文 → 需要时再读它引用的附加文件。
- 四大特点：可组合（composable）、可移植（portable）、高效（efficient）、可含可执行代码（powerful）。
- Skill ≠ 模型本身：它不是新的 AI，而是"装在 AI 上、让它更擅长某件事"的说明书和工具。
- Skill ≠ 一次性提示词：提示词是"一段话、用完就散"；Skill 是结构化、可复用、可迭代、可分享的能力包。
- 使用边界：Skill 依赖 AI 自己判断何时加载，`description` 写模糊了就可能导致该触发时不触发。

## Key Quotes

> **生活类比：** Skill 就像给**新员工的一套「入职手册 + 工具包」**……当任务涉及 Excel，它就翻开「Excel 技能包」，照里面的说明和工具操作，瞬间变成 Excel 高手。平时这套手册收在柜子里，不占地方。（原资料）

> 提示词就像"随口说的一句话"，说一次就没了……而 Skill 就像"做好的一套模板工具"，把「怎么学透一个概念」的整套方法固定下来。（学习者批注）

## Connections

- [[Skill]] — 本文对应的概念页
- [[ConceptLearner]] — 本仓库里那个真实存在的 Skill 实体，是本文的活例子
- [[ProgressiveDisclosure]] — Skill 省上下文的核心机制
- [[Context]] — Skill 通过渐进式披露为上下文让路
- [[Agent]] — Skill 让通用 Agent 在需要时临时变专业
- [[Anthropic]] — 本文三项来源均出自其官方公告、工程博客与文档

## Contradictions

暂无。

## 学习者的疑问（待后续资料回答）

Skill 和"提示词"之间到底有没有一条明确的界线？比如我把一段很长的提示词存成一个文件，算不算也是一种 Skill？
