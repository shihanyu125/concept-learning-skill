---
title: "WorkBuddy"
type: entity
tags: [entity, product, agent-platform]
sources: [, skill]
last_updated: 2026-09-13
---

# WorkBuddy

## 是什么

**WorkBuddy 是这套 wiki 所在的 AI Agent 工作平台。**

本仓库的 `raw/` `wiki/` `graph/` `tools/` 就是在一个 WorkBuddy 工作区里搭建起来的——摄取、体检、建图、提交这些操作都由它执行。

它同时是三个主题的**共同载体**：记忆系统（[[Memory]]）、自动化（[[Automation]]）、选模型策略（[[ModelRouting]]）都是这个平台的**内置机制**，而不是凭空出现的抽象概念。把它单独立页，是为了让这三个概念有个可追溯的落点。

## 在本仓库里留下的实际痕迹

| 路径 | 用途 | 相关页面 |
|---|---|---|
| `~/.workbuddy/MEMORY.md` | **用户级**本地记忆：跨所有项目的偏好与规则 | [[Memory]] |
| `<项目>/.workbuddy/memory/` | **工作区**记忆：项目日志（`YYYY-MM-DD.md`）与长期结论（`MEMORY.md`） | [[Memory]] |
| `~/.workbuddy/skills/` | 用户级 [[Skill]] 存放位置 | [[Skill]] |
| `<项目>/.workbuddy/skills/` | 项目级 Skill 存放位置（本仓库的 [[ConceptLearner]] 就在这里） | [[Skill]] |
| `~/.workbuddy/SOUL.md`、`IDENTITY.md`、`USER.md` | 身份与用户画像文件 | — |

三层记忆里有两层直接落在 WorkBuddy 的目录约定上——这也是为什么"记忆"在别的 AI 产品里常是个模糊说法，在这里却能落到具体路径。

## 与相邻实体的区别

- **WorkBuddy** —— 平台 / 产品（跑 Agent 的地方）
- [[Anthropic]]、[[OpenAI]] —— 模型与 API 的提供方（提供"脑子"）
- [[LlmWikiAgent]] —— 一套方法的开源实现（提供"做法"），不是平台

三者层次不同，容易混在一起谈。

## 关联

- [[Memory]] — 三层记忆里的用户级与工作区两层由它的目录约定落地
- [[Skill]] — 个人级 / 项目级两个存放位置
- [[Automation]] — 内置的定时任务机制
- [[ModelRouting]] — 内置的模型档位选择
- [[ConceptLearner]] — 装在本仓库 `.workbuddy/skills/` 下的项目级 Skill
- 来源页：[[]]、[[skill]]

## 待补充

- **平台的完整能力清单** —— 本页只记了本仓库实际用到的部分（记忆、技能、自动化、模型档位），其余能力未覆盖。
- **背后的模型与切换方式** —— WorkBuddy 接的是哪些模型、怎么切换，来源未涉及；因此 [[ModelRouting]] 的三档取向目前无法对应到具体型号。

## 来源

- `raw/2026-09-12--.md`（三层记忆的路径、自动化与模型档位的存在）
- `raw/skill.html` 及其概念页 [[Skill]]（个人级 / 项目级存放位置）
- 本仓库实际结构观测：`.workbuddy/skills/concept-learner/`、`.workbuddy/memory/`、`~/.workbuddy/skills/`
- 说明：本页是**从仓库实际证据反推**的实体页，不是某份资料的直接产物；来源中未出现的能力一律未写。
