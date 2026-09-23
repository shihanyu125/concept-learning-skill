---
title: "LLMWiki（LLM Wiki 模式）"
type: concept
tags: [llm-wiki, knowledge-management, methodology, meta]
sources: [llm-wiki-pattern]
last_updated: 2026-09-23
---

# LLMWiki（LLM Wiki 模式）

## 定义

**LLM Wiki 是一种知识组织模式**：原始资料只进不改地放在 `raw/`，由 AI 读完后**自动编译**成一套互相链接、带交叉引用和矛盾标注的持久化 wiki。

与传统知识工具的根本差别：

> 传统工具让你**搜索自己的笔记**——你得先整理好，之后才能翻出来。
> LLM Wiki 让你**只收集资料**——整理与连接交给 AI。

**每加一份新资料，整个 wiki 变得更厚，而不是变得更乱。**

## 核心机制

### 底层洞察：编译器 vs 解释器

[[AndrejKarpathy]] 用了一个计算机科学的类比点明问题所在：

- **[[RetrievalAugmentedGeneration|RAG]] 像"解释器"**：每次执行都重新解析一遍源码。
- **LLM Wiki 像"编译器"**：先把知识预先编译成可直接执行的结构，之后直接跑。

一个更直白的说法是：

> **RAG 像开卷考试临时翻书；LLM Wiki 像提前把书读薄、编成自己的一本。**

所以本模式的关键动作不是"查询时检索"，而是"**先编译，再查询**"。

### 三层架构与归属

| 层级 | 名称 | 内容 | 谁负责 |
|---|---|---|---|
| 第一层 | **Raw sources** | 文章、论文、图片、数据、代码仓库。**不可变——LLM 只读不改** | 你 |
| 第二层 | **The wiki** | LLM 生成的 Markdown 页面集（摘要 / 实体 / 概念 / 对比 / 综合） | **LLM 完全拥有** |
| 第三层 | **The schema** | `CLAUDE.md` / `AGENTS.md`：规定组织方式、命名约定、工作流 | 你 + LLM 共同演进 |

**第三层最容易被忽略，但最关键**——没有它，命名会漂、页面结构会漂、引用习惯也会漂，wiki 会退化成一个被聊天记录堆出来的文件夹。

### 固定目录布局

```
raw/    只读源（只进不改）
wiki/   AI 维护的内容层
  index.md     全部页面的目录（管空间："这里都有什么"）
  log.md       只追加的操作流水账（管时间："最近发生了什么"）
  overview.md  跨来源的"活的"综述
  sources/     每份资料一页摘要
  entities/    人物、公司、项目、产品
  concepts/    概念、框架、方法、理论
  syntheses/   提问的答案回填成页面
graph/  知识图谱（graph.json + graph.html）
tools/  独立可跑的脚本
```

每个页面都带 YAML frontmatter（`title` / `type` / `tags` / `sources` / `last_updated`），页面之间用 **`[[双链]]`** 引用——双链既是给人读的导航，也是知识图谱的边。

### 三个核心操作

1. **Ingest**：读完整来源 → **更新 10–15 个既有页面** → 新建必要的实体/概念页 → 更新 index → 记 log。是"编织"，不是"追加"。
2. **Query**：读 index 定位 → 综合作答（带回链）→ **把有价值的答案回存成新页面**。这是知识**复利**的关键：传统聊天里发现会消失在历史记录中。
3. **Lint**：查矛盾、过时声明、孤儿页、缺独立页面的重要概念、缺失交叉引用、数据空白。

本仓库把第 3 项进一步拆成 **Health（结构，零 LLM 调用，免费，每次可跑）** 与 **Lint（内容质量，花 token，每 10–15 次摄取跑一次）**，且约定**先 Health 后 Lint**——对空文件做语义检查纯属浪费。

### 适用范围：不限主题，判据是"会不会反复用到"

一个常见误解是：以为 LLM Wiki 只能装某一门课、某一个项目的内容。**模式本身没有主题限制。**

- Karpathy 举的示例之一 "Farzapedia"，就是某人把**自己的个人材料**编译成个人百科（见 [[karpathy-llm-wiki-gist]]）。
- 本仓库 `raw/README.md` 对投放物的定义同样很宽：论文、文章、笔记、会议纪要、书籍摘录、网页存档……**格式不限**（`.md` `.pdf` `.docx` `.pptx` 等均可），命名示例用的甚至是一篇论文。

真正的准入判据不是"属不属于这个主题"，而是两条：

1. **会不会反复用到。** 一条通行的判据是："它适合**会反复用到的知识**。一次性问答不值得建页。"——因为建页与维护都有成本。
2. **有没有可靠来源。** 每页的 `sources` 要能追溯回 `raw/` 里的一份资料；纯凭印象的内容不入库。

**但有一个真实约束**：Karpathy 观察到"高规模下不一定需要复杂 RAG"是**有前提**的——主题聚焦、规模未膨胀。知识域一变杂，目录式导航的收益就下降，最终仍需正式检索机制配合（见下一节）。

→ 实践结论：**想放什么就放什么（专业知识、读书笔记、工作资料都行），只是别指望一个 wiki 同时当好所有事**——主题越聚焦，这套结构越省心。

> 本仓库还叠加了一条仓库级限制：它是**公开仓库**，涉及个人观点、私事的内容不进 `wiki/`（那类内容放在本地记忆目录）。

### 规模与边界（务必连着前提记）

Karpathy 自称在单一研究主题上积累**约 100 篇文章、40 万字**，且**没有直接写过一个字**；并提到在该规模下不一定需要复杂的 RAG 基础设施。

**这句话有前提**：成立的原因不是模型不需要检索了，而是资料已被编译成有结构的知识层——先读 `index.md`，再看摘要与概念页，路径比直接翻原始资料短得多。

- 主题聚焦、规模未膨胀 → `index + summaries + concept pages` 可能替掉一部分复杂检索
- 数据量继续上去、知识域变杂、要求强可追溯 → 大概率仍需与正式检索、引用、校验机制配合

Karpathy 本人划的边界线：**human owns verification（验证责任在人）**。

### 已知瓶颈（社区实践）

1. **查询瓶颈**：页面超几百页后 grep 变慢。"我上周添加了关于 X 的哪些内容"这类问题靠读文件无法实现。
2. **结构瓶颈**：结构会不受控地自发形成，某个时刻你会发现自己是在与工具对抗。
3. 应对方向：**Binder**（数据先行、渲染成 Markdown、SQLite 索引 + API 双向读写）、**Knowledge Engine**（Markdown 层供人读 + 内存层供机器查，双层原子同步）。见 [[LlmWikiAgent]] 的相关记录。

## 关键性质

- **纯文本**：整个 wiki 就是一堆 Markdown，无服务器、无数据库、全本地。
- **天然带版本历史**：仓库本身是 git 仓库，改动历史免费获得。
- **可作为 Obsidian vault 直接浏览**：双链与 frontmatter 都被 Obsidian 识别（常过滤 `index.md`、`log.md` 两个元页面）。
- **先 Health 后 Lint**：Health 查结构（零 LLM 调用、免费、可每次跑），Lint 查内容质量（花 token、每 10–15 次摄取跑一次）。对空文件做语义检查纯属浪费。

## 与其他概念的关系

- 它与 [[RetrievalAugmentedGeneration]] 是**对照关系而非替代关系**（见该页对照表）。
- 它整体由 [[Agent]] 驱动——不是脚本流水线，而是"读 → 判断 → 写"的智能体循环。
- 参考实现本身就是一个 coding agent 的 [[Skill]]。
- `index.md` 的设计正是 [[ProgressiveDisclosure]] 的体现：先看目录，再决定读哪页，避免把整个 wiki 灌进 [[Context]]。
- 它和 [[Memory]] 是**同一条"外置"思路的两个对象**：memory 把"助手干过什么"外置到磁盘，wiki 把"我知道什么"外置到磁盘。区别在记的是工作还是知识。

## 关联

- [[AndrejKarpathy]] — 该模式的提出者
- [[LlmWikiAgent]] — 公开参考实现
- [[Agent]]、[[Skill]]、[[Context]]、[[ProgressiveDisclosure]]
- [[ToolUse]] — 给 Agent 的"外部知识层"要靠工具调用来读；wiki 是编译好的地址簿，工具是走过去的腿
- [[RetrievalAugmentedGeneration]] — 主要对照对象（解释器 vs 编译器）
- [[why-compile-not-retrieve]] — 本 wiki 关于这组对照的深入分析（含边界条件）
- [[ConceptLearner]] — 本仓库已有的能力包，与本 wiki 是同一思路在不同层面的应用
- [[KnowledgeEquity]] — 编译式知识库在全球尺度上的镜像问题：谁的知识被收录、谁被漏掉
- [[JupyterNotebook]] — 同一理念的另一种文件形态：纯文本、可读、可复现，且本身就能逐段运行
- 来源页：[[karpathy-llm-wiki-gist]]、[[llm-wiki-pattern]]、[[llm-wiki-learning-material]]

## 来源

- Karpathy GitHub gist `llm-wiki` 及配套 X 长帖（原始材料整理见 `raw/karpathy-llm-wiki-gist.md`）
- `raw/llm-wiki-pattern.md`
- `SamurAIGPT/llm-wiki-agent`（MIT）
- 见 [[AndrejKarpathy]]、[[LlmWikiAgent]]

## 本站的落地差异（重要）

| 维度 | Karpathy 原始 gist | 本仓库 |
|---|---|---|
| 核心三层 | raw / wiki / schema | 同（schema 即根目录 `AGENTS.md`） |
| 图谱与脚本 | 未在 gist 中作为核心 | **额外安装** `graph/` + `tools/`，属实现层扩展 |
| 体检拆分 | 统一叫 lint | 拆成 health（结构，免费）+ lint（内容，耗 token） |
| 元页面 type | 未规定 | `index/log/overview` 统一用 `type: synthesis` + `meta` 标签 |

读这个 wiki 时要注意区分"模式本体"与"本实现的附加件"。
