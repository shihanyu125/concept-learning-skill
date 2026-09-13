---
title: "概念关系说明：Agent、上下文、Skill 三者之间的关系"
type: source
tags: [concept-material, cross-concept, learning-notes]
sources: [concept-relationship]
date: 2026-09-04
source_file: raw/concept-relationship.md
last_updated: 2026-09-13
---

# 概念关系说明：Agent、上下文、Skill 三者之间的关系

> **来源说明**：本页依据的事实来源是 `raw/concept-relationship.md`（事实来源层，只读）。
> 该文件同时也在 `learning-materials/concept-relationship.md`——那是**作品输出区**，内容可能被继续修订；两处内容经 md5 校验一致（`32e5ead78fa07f4de1507fcfb7c68cc0`）。
> 同一份内容另有**网页版**，已一并存入 `raw/concept-relationship.html`（md5 `4aa97b7285dad64d351c8bf62749c915`）——两版内容相同，只是格式不同；本页摘要的编写依据是 `.md` 版。
> 引用时以 `raw/` 为准。
> 原始资料（点开即读）：[raw/concept-relationship.md](../../raw/concept-relationship.md) ｜ [raw/concept-relationship.html](../../raw/concept-relationship.html) ｜ [learning-materials/concept-relationship.md](../../learning-materials/concept-relationship.md) ｜ [learning-materials/concept-relationship.html](../../learning-materials/concept-relationship.html)

## Summary

不解释单个概念，而是把三个概念**串起来**：Agent 是执行者，上下文是工作台，Skill 是抽屉里随用随取的工具手册。三者构成闭环——Skill 把专业知识按需装进上下文，上下文把"装了什么"提供给 Agent 做决策，Agent 据此更专业地行动。

## Key Claims

- 三者定位：Agent = 执行者 / 决策者；上下文 = 工作记忆 / 工作台；Skill = 可复用的知识包。
- 上下文是 Agent 决策的"原料"。三个推论：上下文**大小** = Agent 的眼界；上下文**内容** = Agent 的判断质量；窗口满时会遗忘，这是长任务里 Agent 表现下滑的常见原因。
- Skill 把"一次性经验"变成"可反复调用的方法"，靠渐进式披露实现三个效果：沉淀（流程固化成文件）、省空间（平时只预读 name+description）、可复用（同一 Skill 服务多个相似任务）。
- 有无 Skill 的 Agent 差异对照：

| 对比维度 | 没有 Skill 的 Agent | 有 Skill 的 Agent |
|---|---|---|
| 接到新任务 | 每次都要从头说明流程、要求 | 直接调用现成的 Skill |
| 专业程度 | 泛泛、不精 | 按需临时"变专业" |
| 上下文占用 | 要一次性塞进大段指令 | 渐进式披露，按需加载，省空间 |
| 知识沉淀 | 用完即散，不积累 | 固化成文件，可复用、可迭代 |
| 结果一致性 | 每次执行可能不一样 | 流程固定，更稳定、可复现 |

## Key Quotes

> **Agent 是干活的「人」，上下文是它眼前的「工作台」，Skill 是它抽屉里「随用随取的工具手册」。**

> 上下文决定了 Agent 能"看到多少、看清多少"，因此也决定了它"想得对不对、做得好不好"。（原资料）

## Connections

- [[Agent]]、[[Context]]、[[Skill]] — 本文论述的三个对象
- [[ProgressiveDisclosure]] — Skill"省空间"的机制来源
- [[agent-context-skill-relationship]] — 本文在 wiki 里对应的综合分析页
- [[LLMWiki]] — 同一设计哲学的另一体现：把知识编译到外部结构，减少临时拼凑

## Contradictions

暂无。本页是跨页综合，若与单个概念页出现冲突，应以各自的原始来源为准。
