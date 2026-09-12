---
title: "Skill（Agent Skill / 技能包）"
type: concept
tags: [agent-skill, skill-md, reuse, core-concept]
sources: [skill, concept-relationship, ]
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
- **Skill ≠ 一次性提示词**：提示词是一段话、用完即散；Skill 是结构化、可复用、可迭代、可分享的能力包。完整分界见 [[Prompt]]——判据有三条：**进入窗口的时机 / 结构 / 由谁触发**。
- **Skill ≠ 记忆**：这是最容易混的一对。**记忆是"信息"**（你是谁、你的项目是什么规矩，随项目变化），**Skill 是"流程"**（这类任务该怎么做，可跨项目复用）。同一份经验，写进记忆还是做成技能，看它更偏事实还是更偏步骤。详见 [[Memory]] 的"记忆 ≠ 技能"。
- **`description` 写模糊会导致不触发**：Skill 依赖 AI 自己判断何时加载，元数据质量决定它是否生效。

## 存放在哪：个人级 / 项目级

Skill 不是"装进模型"里的，而是**放在文件系统上**，按生效范围分两级：

| 层级 | 生效范围 | 本机实例（实际观测） |
|---|---|---|
| 个人级 | 所有项目都能用 | `~/.workbuddy/skills/concept-learner/` |
| 项目级 | 只在某个项目内生效 | `<项目>/.workbuddy/skills/concept-learner/`（本仓库里就有） |

这也解释了四大特点里的**可移植（portable）**：既然它就是一个文件夹，拷到别处就能用。

两级存放位置与 [[Memory]] 的"用户级 / 工作区"分层是同一套归属逻辑，同属 [[WorkBuddy]] 的目录约定。

分级说法来自本文所引 Claude Code 文档《Extend Claude with skills》；上表的路径是本机实际观测结果，与官方目录约定是否严格一一对应**待核实**。

## 关联

- [[Prompt]] — 最主要的对照概念：**你的一次性说明 vs AI 可自行取用的常备说明书**
- [[agent-context-skill-relationship]] — 综合页：Skill 在 Agent / 上下文 / Skill 三角中的定位，以及"省空间"这条因果链
- [[Memory]] — 另一组对照：**流程 vs 信息**（Skill 回答"怎么做"，记忆回答"你是谁"）
- [[Automation]] — 常配套使用：流程沉淀在 Skill，调度登记在 Automation
- [[Workflow]] — 三者常并列：Skill 的知识、Workflow 的流程、Automation 的时机
- [[ConceptLearner]] — 本仓库真实存在的 Skill 实体，是活例子
- [[ProgressiveDisclosure]] — Skill 的核心机制
- [[Context]] — Skill 服务的对象
- [[Agent]] — Skill 让通用 Agent 临时变专业
- [[LLMWiki]] — 参考实现本身就是一个 coding agent skill
- [[WorkBuddy]] — 个人级 / 项目级两个存放位置所属的平台
- 来源页：[[skill]]、[[concept-relationship]]、[[]]

## 来源

- Anthropic《Introducing Agent Skills》(2025-10)
- Anthropic 工程博客《Equipping agents for the real world with Agent Skills》
- Claude Code 文档《Extend Claude with skills》
- `raw/2026-09-12--.md` — "记忆 ≠ 技能"的对照
- 见 [[Anthropic]]
