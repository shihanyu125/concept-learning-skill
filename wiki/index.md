---
title: "Wiki Index"
type: synthesis
tags: [meta, index]
sources: []
last_updated: 2026-09-15
---

# Wiki Index

> 本 wiki 所有页面的目录。**每次摄取（ingest）后必须更新。**
> 用法：提问时先读这一页定位相关页面，再钻进具体页面——不要一上来就翻遍全库。

## Overview

- [Overview](overview.md) — 跨所有来源的"活的"综述，随每次摄取修订

## Sources

- [概念学习资料：Agent（智能体）](sources/agent.md) — Agent = 增强型 LLM，叠加检索/工具/记忆；关键在"下一步由谁决定"（原始资料：[raw/agent.html](../raw/agent.html)）
- [概念学习资料：大模型的上下文](sources/llm-context.md) — 上下文窗口的定义、token 计量、截断行为（原始资料：[raw/llm-context.html](../raw/llm-context.html)）
- [概念学习资料：Skill（技能包）](sources/skill.md) — Skill 的文件夹结构、YAML 元数据与渐进式披露（原始资料：[raw/skill.html](../raw/skill.html)）
- [概念学习资料：向量数据库](sources/vector-database.md) — 按"意思有多接近"检索的数据库，RAG 的地基（原始资料：[raw/vector-database.html](../raw/vector-database.html)）
- [概念关系说明：Agent、上下文、Skill 三者关系](sources/concept-relationship.md) — 不解释单个概念，而是把三者串成闭环（原始资料：[raw/concept-relationship.md](../raw/concept-relationship.md) ｜ [网页版](../raw/concept-relationship.html)）
- [概念学习资料：LLM Wiki](sources/llm-wiki-learning-material.md) — 本仓库自身组织模式的九段式学习资料，concept-learner 第 6 份产出（原始资料：[raw/llm-wiki.html](../raw/llm-wiki.html)）
- [LLM Wiki 模式](sources/llm-wiki-pattern.md) — 本仓库所安装模式的目录布局与四条工作流
- [Karpathy 的 llm-wiki 原始材料](sources/karpathy-llm-wiki-gist.md) — 编译器 vs 解释器、三层架构、规模与边界（含待核实标注）
- [概念学习资料：普莫时代（PUMO）](sources/pumo-era.md) — 2025 年提出的最新时代环境框架：极化、难以想象、质变、过热（原始资料：[raw/pumo-era.md](../raw/pumo-era.md)）

## Entities

- [Anthropic](entities/Anthropic.md) — Claude 的开发方；Agent/Workflow、Skill、Context 三个主题的主要来源
- [OpenAI](entities/OpenAI.md) — GPT 与 Agents SDK 的开发方；来源方之一
- [Pinecone](entities/Pinecone.md) — 向量数据库代表厂商
- [AndrejKarpathy](entities/AndrejKarpathy.md) — LLM Wiki 模式的提出者
- [LlmWikiAgent](entities/LlmWikiAgent.md) — 开源参考实现 `SamurAIGPT/llm-wiki-agent`，本仓库的规范参照
- [ConceptLearner](entities/ConceptLearner.md) — 本仓库里真实存在的概念学习 Skill，是 [[Skill]] 的活例子
- [WorkBuddy](entities/WorkBuddy.md) — 本 wiki 所在的 Agent 平台；记忆分层、自动化、模型档位三个主题的共同载体

## Concepts

- [Agent（智能体）](concepts/Agent.md) — 能自己拿主意、自己动手做事的 AI 程序
- [Context（上下文）](concepts/Context.md) — 模型单次请求能看到的全部内容及其上限
- [Token（词元）](concepts/Token.md) — 上下文的计量单位；"还剩多少余量"就是靠它算的
- [ContextManagement（上下文管理）](concepts/ContextManagement.md) — 窗口满了之后怎么办：编辑 / 压缩 / 外置
- [ToolUse（工具调用）](concepts/ToolUse.md) — 让模型从"只会说"变成"真能动手"的那座桥
- [MCP（Model Context Protocol）](concepts/MCP.md) — AI 接外部世界的"通用插座"；host/client/server 三角色 + tools/resources/prompts 三原语
- [Memory（记忆）](concepts/Memory.md) — 让 AI 跨步骤保持连贯；分云端 / 用户级 / 工作区三层
- [Skill（技能包）](concepts/Skill.md) — 打包好的专业能力文件夹，按需加载；分个人级与项目级存放
- [Prompt（提示词）](concepts/Prompt.md) — 一次性输入，用完即散；与 Skill 的分界在于"谁决定它何时进入上下文"
- [ProgressiveDisclosure（渐进式披露）](concepts/ProgressiveDisclosure.md) — 按需分层加载，节约上下文的核心策略
- [Workflow（工作流）](concepts/Workflow.md) — 流程由代码写死；Agent 的对照面
- [Automation（自动化）](concepts/Automation.md) — 让任务到点自己跑：一次性 vs 周期性，以及六条设计原则
- [ModelRouting（选模型策略）](concepts/ModelRouting.md) — 按"任务需要多少推理"选档位，而不是一律上最强
- [VectorDatabase（向量数据库）](concepts/VectorDatabase.md) — 按语义相似度检索的数据库
- [RetrievalAugmentedGeneration（RAG）](concepts/RetrievalAugmentedGeneration.md) — 先检索、再生成；与 LLM Wiki 形成对照
- [LLMWiki（LLM Wiki 模式）](concepts/LLMWiki.md) — 编译式知识库：先编译，再查询
- [PumoEra（普莫时代 / PUMO）](concepts/PumoEra.md) — 2025 年提出的时代环境框架：极化、难以想象、质变、过热；首个传播学线概念
- [KnowledgeEquity（知识公平）](concepts/KnowledgeEquity.md) — 公共知识库中被记录与呈现的机会不均等；维基偏差会传导成 AI 偏差
- [PseudoEnvironment（拟态环境）](concepts/PseudoEnvironment.md) — 我们活在媒介转述的世界里；李普曼 1922
- [Stereotype（刻板成见）](concepts/Stereotype.md) — 先有图样再看世界，滤镜决定你能看见什么；李普曼 1922
- [PublicOpinion（舆论 / 公众舆论）](concepts/PublicOpinion.md) — 舆论是"头脑里的图景"而非民意；附《公众舆论》公版原文逐字核验；李普曼 1922
- [LasswellFormula（拉斯韦尔 5W 模式与三功能）](concepts/LasswellFormula.md) — 传播学的研究地图：谁→说什么→渠道→对谁→效果；1948
- [Gatekeeping（守门人）](concepts/Gatekeeping.md) — 信息到你面前前总有"采购员"把关；卢因 1947
- [TwoStepFlow（两级传播与意见领袖）](concepts/TwoStepFlow.md) — 媒介先说服身边更懂的人，再由他影响你；有限效果论起点
- [OpinionLeader（意见领袖）](concepts/OpinionLeader.md) — 在某件具体事上"身边人会去问"的那个人；与守门人、KOL 的分工
- [PersuasionResearch（劝服研究 / 耶鲁学派）](concepts/PersuasionResearch.md) — 用实验拆解"怎么说才更说服人"；霍夫兰 1953
- [UsesAndGratifications（使用与满足）](concepts/UsesAndGratifications.md) — 别问媒介对你做了什么，问你对媒介做了什么；卡茨 1974
- [AgendaSetting（议程设置）](concepts/AgendaSetting.md) — 媒介不能决定你怎么想，但很能决定你想什么；1972
- [SpiralOfSilence（沉默的螺旋）](concepts/SpiralOfSilence.md) — 怕孤立使少数派闭嘴、多数声浪越滚越大；1980
- [CultivationTheory（培养理论）](concepts/CultivationTheory.md) — 电视不改变你一时想法，它把你"泡"出世界观；格伯纳
- [BiasOfCommunication（传播的偏向）](concepts/BiasOfCommunication.md) — 文明用什么媒介就长成什么形状；英尼斯 1951
- [MediumIsTheMessage（媒介即讯息）](concepts/MediumIsTheMessage.md) — 改变社会的是媒介本身，不是它运送的内容；麦克卢汉 1964
- [EncodingDecoding（编码 / 解码）](concepts/EncodingDecoding.md) — 传者装意义、观者按立场拆；三种解码姿态；霍尔 1973
- [CultureIndustry（文化工业）](concepts/CultureIndustry.md) — 文化被流水线化成罐头：包装不同、配方一致；法兰克福学派 1947
- [CommunicationStudies（传播学：学科定义与研究对象）](concepts/CommunicationStudies.md) — 研究社会信息系统及其运行规律的科学；人内→大众传播的谱系
- [SocialInformationSystem（社会信息系统）](concepts/SocialInformationSystem.md) — 学科对象的说明书：开放性、双重偶然性、两类故障、自我修复
- [CommonMeaningSpace（共同意义空间）](concepts/CommonMeaningSpace.md) — 传播成立的前提：没有共同地面就"传而不通"
- [TypesOfCommunication（传播的类型与层次）](concepts/TypesOfCommunication.md) — 人内 / 人际 / 群体 / 组织 / 大众：传播不是单个动作，而是层层放大的系统
- [GoldenAgeOfCommunication（传播学的黄金三十年）](concepts/GoldenAgeOfCommunication.md) — 为何诞生于 20 世纪初的美国：技术/政治/经济/社会/学术五条件
- [SpiritualIntercourse（精神交往理论）](concepts/SpiritualIntercourse.md) — 马克思、恩格斯：物质交往决定精神交往；用时间消灭空间
- [InternationalCommunication（国际传播）](concepts/InternationalCommunication.md) — 以国家为主体的跨国界传播：两个方向、三个特征、普莫时代的韧性

## Syntheses

- [Agent、上下文、Skill 三者是什么关系？](syntheses/agent-context-skill-relationship.md) — 三者的定位、闭环与两条关键因果链
- [为什么要「先编译」而不是「每次检索」？](syntheses/why-compile-not-retrieve.md) — 编译式 wiki 与 RAG 的差异、边界与不可让渡的原则
- [四大奠基人与施拉姆（人物—出身—理论对照）](syntheses/communication-studies-founding-figures.md) — 传播学史的人物线：谁是谁、谁属于哪个学科、合起来干了什么
