---
title: "概念学习资料：LLM Wiki（concept-learner 第 6 份产出）"
type: source
tags: [llm-wiki, learning-material, meta]
sources: [llm-wiki-learning-material]
date: 2026-09-13
source_file: raw/llm-wiki.html
last_updated: 2026-09-14
---

# 概念学习资料：LLM Wiki（concept-learner 第 6 份产出）

## Summary

用 `concept-learner` Skill 生成的第 6 份概念学习资料（九段式：学习目标 / 核心问题 / 一句话解释 / 核心机制 / 应用场景 / 易混淆与边界 / 自测题 / 可核查来源 / 本人核查笔记），对象是本仓库自身的组织模式 [[LLMWiki]]。内容以 [[karpathy-llm-wiki-gist]] 与 [[llm-wiki-pattern]] 两份既有材料为准，未引入新事实；与前 5 份资料同款版式、不同配色，产出形式就此统一。

## Key Claims（该资料的要点复述）

- **一句话解释**：原始资料只进不改地放 `raw/`，由 AI 自动编译成互相链接、带矛盾标注的持久化 wiki——人只管收集资料，不管整理；每加一份新资料，wiki 变得更厚而不是更乱。
- **类比**：RAG 是「解释器 / 开卷考试临时翻书」，LLM Wiki 是「编译器 / 提前把书读薄、编成自己的一本」。
- **核心机制**：三层架构（raw 归你、wiki 归 AI、schema 共同演进）；ingest（编织不是追加）/ query（答案回存复利）/ lint 三操作；纯文本 + git 版本历史 + Obsidian 可读。
- **易混淆与边界**：≠ RAG 替代品（对照关系）；≠ 笔记软件（Obsidian 是 IDE，wiki 是代码库，人几乎不手写）；准入判据是「会不会反复用到 + 有没有可靠来源」，不限主题；规模有前提；human owns verification。

## Key Quotes

> 传统工具让你**搜索自己的笔记**——你得先整理好，之后才能翻出来。LLM Wiki 让你**只收集资料**——整理与连接交给 AI。

## Connections

- [[LLMWiki]] — 该资料对应的 concept 页（本仓库的活样本）
- [[karpathy-llm-wiki-gist]]、[[llm-wiki-pattern]] — 资料内容的两个一手依据（本页未新增事实）
- [[ConceptLearner]] — 生成该资料的 Skill，与 [[Skill]] 页互为印证
- [[Agent]]、[[Context]]、[[RetrievalAugmentedGeneration]] — 资料中作为对照出现的概念

## Contradictions

无新增矛盾：本页是学习资料的摘要，其事实全部来自既有 source 页，未引入与既有页冲突的表述。

## 来源说明

- 原始资料（点开即读）：[raw/llm-wiki.html](../../raw/llm-wiki.html)（副本；原件 [learning-materials/llm-wiki.html](../../learning-materials/llm-wiki.html)，md5 `68c14456035af308e3a3397d2e7ac926`）
- 该资料自身的可核查外链：Karpathy X 长帖、`SamurAIGPT/llm-wiki-agent`（MIT）
