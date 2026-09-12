# LLM Wiki 模式（The LLM Wiki Pattern）

> 原始资料 · 来源：Andrej Karpathy 提出的 "LLM Wiki" 思路 + 开源实现 SamurAIGPT/llm-wiki-agent
> 采集日期：2026-09-12

## 一句话

把原始资料丢进 `raw/`，让 AI 读完后**自己写出一套互相链接的 wiki**——人要做的只是"喂资料"和"提问"，而不是"写笔记"。

## 它想解决的问题

大多数知识工具是让人**搜索自己的笔记**：你得先把笔记整理好，之后才能在检索里翻出来。LLM Wiki 反过来——你只管收集原始资料，AI 负责把它编译成结构化、有交叉引用、有矛盾标注、有综合结论的 wiki。**每加一份新资料，整个 wiki 变得更厚，而不是变得更乱。**

## 与 RAG 的区别

| RAG | LLM Wiki |
|---|---|
| 每次提问都从头推导知识 | 一次性编译好，之后持续维护 |
| 检索单位是原始文本块（chunk） | 检索单位是结构化 wiki 页面 |
| 没有交叉引用 | 交叉引用是预先建好的 |
| 矛盾通常在提问时才（可能）暴露 | 矛盾在摄取资料时就标出来 |
| 不积累 | 每份新资料都让 wiki 更丰富 |

## 目录布局

```
raw/          # 不可变的原始资料——只进不改
wiki/         # AI 完全拥有的内容层
  index.md    # 全部页面的目录，每次摄取后更新
  log.md      # 只追加的操作流水账
  overview.md # 跨所有来源的"活的"综述
  sources/    # 每份原始资料一页摘要
  entities/   # 人物、公司、项目、产品
  concepts/   # 概念、框架、方法、理论
  syntheses/  # 回答过的提问，回填成页面
graph/        # 自动生成的知识图谱（graph.json + graph.html）
tools/        # 独立可跑的 Python 脚本
```

## 页面格式

每个 wiki 页面都以 YAML frontmatter 开头：

```yaml
---
title: "页面标题"
type: source | entity | concept | synthesis
tags: []
sources: []       # 本页内容所依据的来源 slug
last_updated: YYYY-MM-DD
---
```

页面之间用 `[[双链]]`（wikilinks）互相引用——这既是给人读的，也是知识图谱的边。

## 四条工作流

1. **摄取 Ingest**：读原始资料 → 写 source 页 → 更新 index/overview → 建或更新 entity、concept 页 → 标矛盾 → 记 log → 校验断链。
2. **提问 Query**：读 index 定位相关页 → 综合作答（带双链引用）→ 询问是否回填成 synthesis 页。
3. **体检 Health / Lint**：
   - Health 查**结构完整性**（空文件、index 与实际文件是否同步、source 页有没有对应的 ingest 日志），零 LLM 调用、免费、可以每次会话都跑；
   - Lint 查**内容质量**（孤儿页、断链、矛盾、过期摘要、缺失的实体/概念页、数据缺口），要花 token，建议每 10–15 次摄取跑一次。
   - 顺序上先 Health 后 Lint——对空文件做语义检查纯属浪费。
4. **建图 Build graph**：两遍构建。第一遍**确定性**解析所有 `[[wikilinks]]`，边标为 `EXTRACTED`；第二遍**语义推断**出双链没覆盖的隐含关系，边标为 `INFERRED`（带置信度分数）或 `AMBIGUOUS`。再用社区检测（Louvain）按主题把节点聚类，输出自包含的 `graph.html`。带缓存，只重新处理变更过的页面。

## 关键性质

- **纯文本**：整个 wiki 就是一堆 Markdown 文件，没有服务器、没有数据库、全在本地跑。
- **天然带版本历史**：wiki 本身是个 git 仓库，改动历史免费获得。
- **可在 Obsidian 里无缝浏览**：`wiki/` 就是一个 vault，双链和 frontmatter 都能被 Obsidian 直接识别（配合 Dataview 插件还能按 frontmatter 查询；常用做法是过滤掉 `index.md`、`log.md` 两个元页面）。
- **不用 API Key 也能用**：在 Claude Code / Codex / WorkBuddy 这类 Agent 里打开本仓库，直接用自然语言驱动即可；`tools/` 下的独立脚本才需要额外配置。

## 参考实现

- 项目：`SamurAIGPT/llm-wiki-agent`
- 核心配置：仓库根目录的 `CLAUDE.md` / `AGENTS.md`——它告诉 Agent 怎么维护这套 wiki，是整套机制最关键的一个文件
- MIT 许可

## 对我的启发（学习者批注）

我原先以为"记笔记"这件事必须自己动手，AI 顶多帮我把某一段话写漂亮。这套模式让我意识到：**可以把"整理与连接"这件事外包出去**——我负责收集和判断，AI 负责结构化和交叉引用。这和我之前理解的 `[[Skill]]` 是同一个思路的延伸：把一类重复劳动固化成可复用的流程，而不是每次重来。
