---
title: "Skill（Agent Skill / 技能包）"
type: concept
tags: [agent-skill, skill-md, reuse, core-concept]
sources: [skill, concept-relationship]
last_updated: 2026-09-13
---

# Skill（技能包）

## 定义

Skill 是一个**打包好的专业能力文件夹**——里面装着指令、脚本、资源。AI 平时"全能但泛泛"，遇到相关任务才打开对应 Skill，让自己临时变成这个领域的专家。

结构上：核心是 **`SKILL.md`**，顶部必须有 YAML 元数据（至少 `name` + `description`），旁边可以带脚本与资源文件。

## 核心机制：渐进式披露

见 [[ProgressiveDisclosure]]。三层按需加载：

1. 启动时只预读所有技能的 `name` + `description` —— 用来判断"该用哪个"
2. 确定相关后，读该技能的 `SKILL.md` 全文
3. 需要时，再读它引用的附加文件

这样平时不占地方，用时才展开。**省的是 [[Context]]。**

## 四大特点

- 可组合（composable）—— 多个 Skill 可协同
- 可移植（portable）—— 换个环境照样用
- 高效（efficient）—— 按需加载，不浪费上下文
- 可含可执行代码（powerful）—— 不只是一段说明文字

## 使用边界（易混淆点）

- **Skill ≠ 模型**：它不是新的 AI，而是"装在 AI 上、让它更擅长某件事"的说明书和工具包。
- **Skill ≠ 一次性提示词**：提示词是一段话、用完即散；Skill 是结构化、可复用、可迭代、可分享的能力包。
- **`description` 写模糊会导致不触发**：Skill 依赖 AI 自己判断何时加载，元数据质量决定它是否生效。

## 关联

- [[ConceptLearner]] — 本仓库真实存在的 Skill 实体，是活例子
- [[ProgressiveDisclosure]] — Skill 的核心机制
- [[Context]] — Skill 服务的对象
- [[Agent]] — Skill 让通用 Agent 临时变专业
- [[LLMWiki]] — 参考实现本身就是一个 coding agent skill
- 来源页：[[skill]]、[[concept-relationship]]

## 来源

- Anthropic《Introducing Agent Skills》(2025-10)
- Anthropic 工程博客《Equipping agents for the real world with Agent Skills》
- Claude Code 文档《Extend Claude with skills》
- 见 [[Anthropic]]
