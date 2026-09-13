---
title: "概念学习资料：向量数据库（Vector Database）"
type: source
tags: [concept-material, vector-database, rag, learning-notes]
sources: [vector-database]
date: 2026-09-04
source_file: raw/vector-database.html
last_updated: 2026-09-13
---

# 概念学习资料：向量数据库（Vector Database）

> **来源说明**：本页依据的事实来源是 `raw/vector-database.html`（事实来源层，只读）。
> 该文件同时也在 `learning-materials/vector-database.html`——那是**作品输出区**，内容可能被继续修订；两处内容经 md5 校验一致（`98f2bc4e1fa5b89cd7697fb635756772`）。
> 原始资料（点开即读）：[raw/vector-database.html](../../raw/vector-database.html) ｜ [learning-materials/vector-database.html](../../learning-materials/vector-database.html)
> 引用时以 `raw/` 为准。

## Summary

说明向量数据库与普通数据库的区别、向量与相似度搜索的原理，以及它为何是 AI 检索能力的地基。核心结论：普通数据库按"字面精确匹配"查，向量数据库按"意思有多接近"查。

## Key Claims

- 向量（Vector / Embedding）：用模型把一段文字或一张图片转成一组数字（如 1536 个），这组数字"代表"它的含义；含义越接近，向量在空间里越靠近。
- 相似度搜索：用"距离"衡量两个向量有多接近（常用余弦相似度、欧氏距离），找出与查询向量最接近的一批结果。
- 普通数据库只会精确匹配（如 `WHERE name = 'xx'`），它"不懂"什么叫意思相近；向量数据库用近似最近邻（ANN）算法，能在几百万条向量里快速找出"最像"的。
- 向量数据库 ≠ 普通数据库的替代品：前者做语义相似查找，后者做精确查找与事务处理，实际系统里常配合使用。
- 向量数据库 ≠ 大模型：它自己不生成任何文字，只负责存向量、按相似度找出来。
- 使用边界：向量检索是"近似"的，可能漏掉或找偏，高要求场景常配合关键词检索（混合检索）或重排序（rerank）。

## Key Quotes

> **生活类比：** 普通数据库像「按编号找书」——你必须说出精确的书名或编号……向量数据库则像「按感觉找书」——你说「想找本关于太空冒险的」，它能给你一堆主题相近的书，哪怕这些书的书名里根本没有「太空」「冒险」这两个词。（原资料）

> 把你的文档切成小段 → 每段转成向量存进向量数据库 → 你提问时，先把问题转成向量，去数据库里找「最相关」的几段 → 把这几个片段作为参考资料喂给 AI。（原资料，RAG 流程）

## Connections

- [[VectorDatabase]] — 本文对应的概念页
- [[RetrievalAugmentedGeneration]] — 向量数据库最主要的应用场景
- [[Agent]] — "检索"能力是 Agent 三大增强能力之一
- [[Context]] — RAG 的本质是把检索结果塞进有限的上下文里
- [[Pinecone]] — 本文来源厂商

## Contradictions

暂无。

## 学习者的疑问（待后续资料回答）

<!-- 原资料的"我的理解"一节仍留空，待学习者本人填写后回填到这里 -->
（原资料的"我的理解与核查笔记"一节尚为空白模板，待学习者本人补充。）
