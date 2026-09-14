---
title: "Wiki Log"
type: synthesis
tags: [meta, log]
sources: []
last_updated: 2026-09-13
---

# Wiki Log

> **只追加**的操作记录。每条以 `## [YYYY-MM-DD] <operation> | <title>` 开头，便于命令行解析：
>
> ```
> grep "^## \[" wiki/log.md | tail -10
> ```
>
> `<operation>` 取值：`scaffold` / `ingest` / `query` / `health` / `lint` / `graph`

## [2026-09-13] scaffold | 安装 LLM Wiki 结构

- 在本仓库根目录安装 LLM Wiki 模式（参照 `SamurAIGPT/llm-wiki-agent`）
- 建立 `raw/`、`wiki/`（含 index / log / overview 与 sources / entities / concepts / syntheses）、`graph/`、`tools/`
- 写入规范文件 `AGENTS.md`（页面格式、命名约定、四条工作流）
- 写入原始资料：`raw/llm-wiki-pattern.md`、`raw/karpathy-llm-wiki-gist.md`

## [2026-09-13] ingest | 概念学习资料：Agent（智能体）

- 来源：`learning-materials/agent.html`
- 新建 source 页 `sources/agent.md`
- 新建 concept 页 `concepts/Agent.md`、`concepts/Workflow.md`
- 新建 entity 页 `entities/Anthropic.md`、`entities/OpenAI.md`

## [2026-09-13] ingest | 概念学习资料：大模型的上下文

- 来源：`learning-materials/llm-context.html`
- 新建 source 页 `sources/llm-context.md`
- 新建 concept 页 `concepts/Context.md`、`concepts/ProgressiveDisclosure.md`

## [2026-09-13] ingest | 概念学习资料：Skill（技能包）

- 来源：`learning-materials/skill.html`
- 新建 source 页 `sources/skill.md`
- 新建 concept 页 `concepts/Skill.md`
- 新建 entity 页 `entities/ConceptLearner.md`

## [2026-09-13] ingest | 概念学习资料：向量数据库

- 来源：`learning-materials/vector-database.html`
- 新建 source 页 `sources/vector-database.md`
- 新建 concept 页 `concepts/VectorDatabase.md`、`concepts/RetrievalAugmentedGeneration.md`
- 新建 entity 页 `entities/Pinecone.md`
- 待办：原资料"我的理解与核查笔记"一节仍为空白模板，待补充后回填

## [2026-09-13] ingest | 概念关系说明：Agent、上下文、Skill 三者关系

- 来源：`learning-materials/concept-relationship.md`
- 新建 source 页 `sources/concept-relationship.md`
- 新建 synthesis 页 `syntheses/agent-context-skill-relationship.md`

## [2026-09-13] ingest | LLM Wiki 模式

- 来源：`raw/llm-wiki-pattern.md`
- 新建 source 页 `sources/llm-wiki-pattern.md`
- 新建 concept 页 `concepts/LLMWiki.md`
- 新建 entity 页 `entities/LlmWikiAgent.md`

## [2026-09-13] ingest | Karpathy 的 llm-wiki 原始材料

- 来源：`raw/karpathy-llm-wiki-gist.md`
- 新建 source 页 `sources/karpathy-llm-wiki-gist.md`
- 新建 entity 页 `entities/AndrejKarpathy.md`
- 新建 synthesis 页 `syntheses/why-compile-not-retrieve.md`
- 修订 `concepts/LLMWiki.md`：补入"编译器 vs 解释器"、三层归属表、规模边界与已知瓶颈
- 标记矛盾/差异：Karpathy 原始 gist 的核心三层为 raw/wiki/schema，`graph/` 与 `tools/` 属实现层扩展

## [2026-09-13] graph | 首次构建知识图谱

- 运行 `tools/build_graph.py`，输出 `graph/graph.json` 与 `graph/graph.html`

## [2026-09-13] health | 首次结构体检

- 运行 `tools/health.py`，结果见 `wiki/health-report.md`

## [2026-09-13] ingest | 概念学习资料：Agent（智能体）— 改由 `raw/` 重新摄取

- 来源：`raw/agent.html`（与 `learning-materials/agent.html` 经 md5 校验一致：`c51bd38ada5bbb63506492f572c79324`）
- **说明**：这份资料此前已从 `learning-materials/` 摄取过，内容无变化；本次是**换到事实来源层后的重新摄取**，没有产生新的事实性结论
- **新建 concept 页** `concepts/ToolUse.md`、`concepts/Memory.md` —— 这两项是原文明确列出的 Agent 三项核心增强能力，此前被 11～13 个页面提到却始终没有自己的页面（触发 lint 的"缺页"判据）
- 修订 `concepts/Agent.md`：能力表与"关联"段补入 [[ToolUse]]、[[Memory]] 双链
- 修订 `sources/agent.md`：`source_file` 由 `learning-materials/agent.html` 改为 `raw/agent.html`，并加来源说明段
- 修订 `wiki/index.md`：Concepts 段新增两页；Sources 段标注来源已迁移
- 修订 `wiki/overview.md`：线一的"三项增强"补上双链；"已知的空白"同步更新
- 记录缺口：记忆的"分层与归属"、工具调用的协议与护栏做法，wiki 目前仍答不上，需补资料

## [2026-09-13] ingest | 概念学习资料：大模型的上下文 — 改由 `raw/` 重新摄取

- 来源：`raw/llm-context.html`（与 `learning-materials/llm-context.html` 经 md5 校验一致：`46f984074affa946ada6b031cfa3fb7d`）
- **说明**：这份资料此前已从 `learning-materials/` 摄取过，内容无变化；本次是**换到事实来源层后的重新摄取**，没有产生新的事实性结论
- **新建 concept 页** `concepts/Token.md` —— 被 9 个页面提到却始终没有自己的页面；它是原文第 2 节的核心（上下文窗口的计量单位）
- **新建 concept 页** `concepts/ContextManagement.md` —— 原文所引两份官方文档（Anthropic 的 context editing、OpenAI 的 Managing the context window）真正在解决的问题；此前 `Context.md` 只讲了截断，没讲应对手段
- 修订 `sources/llm-context.md`：`source_file` 由 `learning-materials/llm-context.html` 改为 `raw/llm-context.html`，加来源说明段与 [[Token]]、[[ContextManagement]]、[[Memory]] 双链；并在"学习者的疑问"下记录**部分收口的进展**
- 修订 `concepts/Context.md`：补 [[Token]]、[[ContextManagement]]、[[Memory]] 双链，三条推论第 3 条指向应对手段
- 修订 `concepts/Memory.md`、`concepts/ProgressiveDisclosure.md`：关联段补入与 [[ContextManagement]] 的分工说明
- 修订 `entities/Anthropic.md`、`entities/OpenAI.md`：材料表补入新页双链
- 修订 `wiki/index.md`、`wiki/overview.md`：Concepts 段新增两页；线二改写为"两层应对"；"已知的空白"由 8 条增至 9 条
- 记录缺口：各家 context editing 的触发阈值与限制、context rot 的确切定义、三种上下文管理做法的成本对比，wiki 目前仍答不上

## [2026-09-13] ingest | 概念学习资料：Skill（技能包）— 改由 `raw/` 重新摄取

- 来源：`raw/skill.html`（与 `learning-materials/skill.html` 经 md5 校验一致：`8a4bee80537a0d6b96720bf5ee5c9130`）
- **说明**：这份资料此前已从 `learning-materials/` 摄取过，内容无变化；本次是**换到事实来源层后的重新摄取**
- **新建 concept 页** `concepts/Prompt.md` —— 被 4 个页面提到却始终没有自己的页面；且原文对 Skill 的定义整个建立在"Skill ≠ 一次性提示词"这条对照之上。页内给出**三条判据**（进入窗口的时机 / 结构 / 由谁触发），据此回答了学习者的疑问"把长提示词存成文件算不算 Skill"——**看的不是有没有文件，而是有没有元数据、由谁判断何时加载**
- 修订 `concepts/Skill.md`：新增"存放在哪：个人级 / 项目级"一节（含本机实际路径 `~/.workbuddy/skills/` 与 `<项目>/.workbuddy/skills/`）；"Skill ≠ 一次性提示词"补 [[Prompt]] 双链
- 修订 `sources/skill.md`：`source_file` 由 `learning-materials/skill.html` 改为 `raw/skill.html`，加来源说明段与 [[Prompt]] 双链；"学习者的疑问"记录**收口**与仍未收口的部分
- 修订 `syntheses/agent-context-skill-relationship.md`：延伸阅读补 [[Prompt]]、[[ContextManagement]]
- 修订 `wiki/overview.md`：线一补 Prompt/Skill 的控制权分界；"最值得注意的对照"由两组变三组；空白清单 9 条增至 10 条；疑问第 3 条标记为**收口**
- 记录缺口：提示词工程（few-shot / 思维链 / 输出格式约束）与模型厂商侧的提示词分层机制，wiki 目前完全空白

## [2026-09-13] ingest | 资料（）：记忆系统与 LLM Wiki

- 来源：`raw/.md`（**新资料**——本 wiki 首份非重复摄取；四个主题：记忆系统 / LLM Wiki / 自动化 / 选模型策略）
- 新建 source 页 `sources/.md`
- **新建 concept 页** `concepts/Automation.md` —— 此前 wiki 完全没有自动化相关页面（一直挂在 overview 的空白清单里）；收录一次性 / 周期性两种类型与六条设计原则
- **新建 concept 页** `concepts/ModelRouting.md`（选模型策略）—— 同样从零建页；含轻量 / 默认 / 强推理三档取向、两个判断问题、两个误区
- **新建 entity 页** `entities/WorkBuddy.md` —— 三层记忆、自动化、模型档位三个主题的共同载体；让这些概念有可追溯的落点（依据本仓库实际目录痕迹反推，非某份资料的直接产物）
- **重写** `concepts/Memory.md`：补入"记忆分三层"（云端 / 用户级 / 工作区）、"日志与结论为何必须分离"、"什么该记 / 不该记"的口诀、"记忆 ≠ 技能"对照表。原先"待补充"段里明确在等这份材料的缺口**已关闭**
- 修订 `concepts/Workflow.md`：新增"与自动化的区别"一节（一个管何时跑、一个管怎么跑）
- 修订 `concepts/Skill.md`：补"Skill ≠ 记忆"（流程 vs 信息）；关联段补 [[Memory]]、[[Automation]]、[[Workflow]]、[[WorkBuddy]]
- 修订 `concepts/Agent.md`：关联段补 [[Automation]]、[[ModelRouting]]
- 修订 `concepts/LLMWiki.md`：补资料给出的"开卷考试临时翻书"类比；补与 [[Memory]] 的"同一条外置思路"关系；来源段标注本文件第二节为**重述**（未产生新事实）
- 修订 `sources/llm-context.md`："能记住偏好"的疑问标记为**已实质回答**（三层记忆分工给出具体机制；保留 `human owns verification` 的验证责任）
- 修订 `wiki/index.md`、`wiki/overview.md`：新增 3 页；overview 把记忆从线二拆为独立的线三、新增线四"运行层两个旋钮"；"最值得注意的对照"由三组增至四组；空白清单重排为 12 条
- 记录缺口：`rrule` 调度语法与失败重试、模型档位与具体型号的对应、WorkBuddy 平台本身的完整能力清单

## [2026-09-13] ingest | 向量数据库 / 概念关系说明 — 来源迁移到 `raw/`

- 来源：`raw/vector-database.html`（与 `learning-materials/vector-database.html` 经 md5 校验一致：`98f2bc4e1fa5b89cd7697fb635756772`）
- 来源：`raw/concept-relationship.md`（与 `learning-materials/concept-relationship.md` 经 md5 校验一致：`32e5ead78fa07f4de1507fcfb7c68cc0`）
- **说明**：这两份此前已摄取过，内容无变化；本次只做**来源迁移**——把资料复制进事实来源层 `raw/`，并把 source 页的 `source_file` 由 `learning-materials/` 改指 `raw/`，**没有产生新的事实性结论**
- 修订 `sources/vector-database.md`、`sources/concept-relationship.md`：`source_file` 改指 `raw/`，加来源说明段（含 md5）
- 修订 `raw/README.md`：内容表补入两份新副本、更新指纹表、说明 `concept-relationship.html` 未复制的原因
- **至此 wiki 所有 source 页的 `source_file` 均已指向 `raw/`（事实来源层）**，追溯链不再跨越到作品输出区
- 记录缺口：向量数据库的选型与竞品对比（目前仍只有厂商单一视角）；`vector-database.html` 的"我的理解与核查笔记"一节仍为空白模板，待学习者补充后回填

## [2026-09-13] health | 复检与 7 项人工交叉验证

- 重新运行 `tools/health.py`：空页 0 / 目录同步 0 / 日志覆盖 0，报告覆盖 `wiki/health-report.md`
- 脚本盲区人工复核 7 项：`raw/` ↔ source 页双向对应、双链大小写（GitHub 敏感）、markdown 链接、命名规范、`log.md` 引用、`type` 与目录匹配、空目录与残页
- **修复**：`wiki/sources/vector-database.md` 的 frontmatter 被外部 Markdown 格式化器改写（六个字段丢失、YAML 引号被去、HTML 注释被删、行尾补空格），经 mtime 对比与复现测试确认非本仓库脚本所为，已用 `git checkout HEAD --` 恢复

## [2026-09-13] lint | 首次内容体检（确定性部分 + 语义层人工检查）

- 运行 `tools/lint.py`：断链 0 / 孤儿页 0 / 格式违规 0 / 缺页候选 0，报告覆盖 `wiki/lint-report.md`
- **语义层检查**（`lint.py` 明确声明不覆盖的"矛盾 / 过时声明 / 缺失交叉引用 / 数据空白"）：通读全部 37 页，并把 wiki 里的断言逐条比对 `raw/` 原文
- **核对通过**：8 个 source 页的 `source_file` 全部指向 `raw/`；5 份副本 md5 与 `raw/README.md` 指纹表一致；双链 0 条大小写错配；markdown 链接 0 条失效；`.workbuddy/` 的 git 跟踪与忽略规则正确；`agent.html` 等原文的引用句逐字可对上
- **查出并修复的问题**：
  1. `log.md` 本身**漏记 `lint` / `graph` / `health` 三类操作** → 本次一并补记（见本文件 health 与 graph 两条）
  2. [[ToolUse]] 只有 1 条内容页入链、[[agent-context-skill-relationship]] 同样 → 在 [[Workflow]]、[[Memory]]、[[ContextManagement]]、[[LLMWiki]]（补 [[ToolUse]]）与 [[Agent]]、[[Context]]、[[Skill]]（补综合页）补双链
  3. `wiki/index.md` 有两条 source 条目（`vector-database`、`concept-relationship`）漏标"事实来源已迁至 `raw/`" → 补齐
  4. [[Automation]] 与 [[]] 漏收原文的"什么时候不该建自动化"（3.3 节）与"三个反直觉点"（第五节）→ 补收
  5. 章节名两套写法（`## 待补` 7 处 / `## 待补充` 7 处）→ 统一为「待补充」
  6. `AGENTS.md` 未说明 `health-report.md` / `lint-report.md` 两份生成物 → 补入目录布局、页面格式与 Lint 说明
  7. **MCP** 被 3 个页面提到却无页面（已命中缺页判据，但 `tools/lint.py` 未报出）→ 在 [[overview]] 的空白清单第 1 条加注，材料足够后再建页
- 另确认一处层次用词张力：`class2` 页称本仓库为"四层结构"，而模式本体是"三层（raw / wiki / schema）"→ 已在 `class2` 页补限定语，指向 [[LLMWiki]] 的"本站的落地差异"
- **未发现事实性互斥矛盾**（不存在同一字段在两页取值不同的情况）

## [2026-09-13] graph | 重建知识图谱（内容修订后）

- 运行 `tools/build_graph.py`，重建 `graph/graph.json` + `graph/graph.html`
- 规模：37 节点 / 236 边（EXTRACTED 223 / INFERRED 13）/ 7 社区；枢纽仍为 [[Context]]（26）、[[Agent]]（24）、[[overview]]（23）

## [2026-09-13] ingest | 概念学习资料网页版补档 —— `concept-relationship.html` 纳入 `raw/`

- **背景**：`learning-materials/` 的 5 份概念学习资料中，4 份 `.html`（`agent` / `llm-context` / `skill` / `vector-database`）早已复制进 `raw/` 并完成摄取；**`concept-relationship.html` 此前只存在于作品输出区**，未进入事实来源层
- **处理**：`cp -p learning-materials/concept-relationship.html raw/concept-relationship.html`（保留原始 mtime 2026-09-04 20:06）；md5 校验一致（`4aa97b7285dad64d351c8bf62749c915`）
- **`raw/README.md`**：内容登记表加一行、指纹表加一行、修正末尾"未复制"的说明 → 至此 `learning-materials/` 5 份资料的**全部格式变体（6 个文件）**在 `raw/` 中均有存档
- **wiki 侧不新建页**：该 `.html` 与既有 [[concept-relationship]] source 页的内容完全重合（同一份内容的两种呈现），重写摘要的产出为零 → 改为**加强可达性**：
  - 5 份 concept-material source 页的「来源说明」各补一行「原始资料（点开即读）」可点击链接，同时指向 `raw/`（事实来源层）与 `learning-materials/`（作品输出区）
  - `wiki/index.md` 的 5 条 source 条目由纯文本路径改为 markdown 链接；`concept-relationship` 一条并列标出网页版
- **规模不变**：wiki 页面总数仍 37（8 source / 7 entity / 15 concept / 2 synthesis + 5 元页面），concept 页仍 15 个

## [2026-09-13] query | 「LLM Wiki 只能装课程内容吗」——答案回填进 [[LLMWiki]]

- **问题**：使用者问「这个 LLM Wiki 是只能放这门课相关的东西，还是任何想了解的专业知识都可以放进去」
- **取证**：查 `raw/README.md`（投放物定义：论文 / 文章 / 笔记 / 会议纪要 / 书籍摘录 / 网页存档，**格式不限**）、`raw/karpathy-llm-wiki-gist.md`（示例 Farzapedia = 个人材料编译成个人百科）、`raw/.md` 2.5 节（"适合会反复用到的知识"）
- **结论**：模式本身**无主题限制**；真正判据是 ① 会不会反复用到 ② 有没有可靠来源。唯一真实约束是 Karpathy 那句"高规模不需复杂 RAG"**以主题聚焦为前提**；另叠加本仓库的公开性限制（个人内容不入 `wiki/`）
- **动作**：在 [[LLMWiki]] 的「核心机制」下新增小节「适用范围：不限主题，判据是'会不会反复用到'」，置于「规模与边界」之前
- **页面总数不变**（仍 37），无新概念页、无新来源页——这是一次 Query 型回填，不产生新来源



## [2026-09-13] ingest | 概念学习资料：LLM Wiki（concept-learner 第 6 份产出）补档 + 参考实现落库 vendor/

- **背景**：核对历史任务「用 skill 讲解 LLM Wiki，并安装 llm-wiki-agent」完成度时发现两处缺口——① `learning-materials/` 缺 LLM Wiki 那份概念学习资料（其余 4 个概念都有）；② 参考实现仓库只在规范里被"参考"，从未真正落地到本地
- **动作一（资料补齐）**：按 `concept-learner` 九段式生成 `learning-materials/llm-wiki.html`（第 6 份概念学习资料，与前 5 份同款版式）；复制进 `raw/llm-wiki.html`（md5 `68c14456035af308e3a3397d2e7ac926`，与原件一致）；`raw/README.md` 登记表与指纹表各加 1 行；新建 [[llm-wiki-learning-material]] source 页；[[LLMWiki]] 关联段补双链；index 补条目
- **动作二（参考实现落库）**：克隆 `SamurAIGPT/llm-wiki-agent` 到 `vendor/llm-wiki-agent/`（浅克隆，HEAD `5c5e056`），`.gitignore` 追加 `vendor/`——是别人的 MIT 代码，只作本地只读参考，不进 GitHub；`git check-ignore` 验证生效
- **页面总数**：37 → **38**（新增 1 个 source 页）；concept 页仍 15 个
- **性质**：本次 source 页是「学习资料」而非新事实来源，内容全部来自既有页，无新增概念

## [2026-09-13] ingest | 概念学习资料：普莫时代（PUMO）——首个传播学线概念

- **起因**：使用者提出想学「普莫社会」。该词在 wiki 中无页面；直接检索命中的是北美原住民 Pomo（无关）。确认其为新传语境概念后定位成功：**PUMO = 2025 年利希腾塔勒提出的时代环境框架（极化 / 难以想象 / 质变 / 过热）**，继 VUCA、BANI 之后的第三代。
- **来源核实**：原论文 Lichtenthaler (2025), *From VUCA and BANI to a PUMO World*, IJITM 22(3/4), DOI 10.1142/S0219877025500129（经 EconBiz / World Scientific / RePEc 三方核对）；中文引入文献周敏、陈飞扬 (2026)《韧性之后：普莫时代国际传播韧性机制转化与反脆弱性前瞻》，《新闻界》2026(3)（北师大官网 PDF 全文可查）。
- **新增原件**：`raw/pumo-era.md`（AI 依据多来源汇编的可核查材料，非原文复制；本仓库 raw/ 新增，未改动既有文件）。
- **新建页面**：source 页 [[pumo-era]] + 概念页 [[PumoEra]]（TitleCase），互为双链；两者均与 [[LLMWiki]] 建链（说明 wiki 不限主题的适用范围）。
- **配套产出**：九段式学习资料 `learning-materials/pumo.html`（作品输出区，未经 ingest，仅登记于 source 页）。
- **更新**：index（Sources + Concepts 两段）、overview（来源数 8→9、新增"支线"段、修订记录、frontmatter sources）、raw/README.md（登记新原件）。
- **规模**：wiki 页面 37→**39**（9 source / 7 entity / **16 concept** / 2 synthesis + 5 元页面）。距"本学期 50 个 concept 页"目标差 **34** 个。
- **待核实标注**：「普莫」为中文音译、原意 "a PUMO world"；概念提出仅一年余、检验少；中文「普莫社会 / 普莫时代」两种表述并存。

## [2026-09-13] query | 维基百科研究课题：知识公平与四个研究方向

- **起因**：使用者确认相关话题（中文维基百科内容现状可作新课题）值得入库，并要求说明日后查看方式。
- **新建页面**：概念页 [[KnowledgeEquity]]（知识公平：定义、偏差传导链、与 LLMWiki/RAG 的连接、研究切口）+ synthesis 页 [[wikipedia-research-directions]]（2025 年学界热点文献表 + 四个研究方向 + 落地建议）。
- **隐私处理**：两页均只做**中性学术转述**，不引用主题原话、不含具体人物论断细节；文献细节不确定处标"待核实"。
- **更新**：index（Concepts + Syntheses 两段）、资料 source 页"关联"段补双链（消孤儿页）。
- **规模**：wiki 页面 39→**41**（16 concept + 3 synthesis）。concept 页计数口径不变：仍为 16 个，距 50 差 34。

## [2026-09-13] ingest | 学习导读：《传播学经典理论》——传播学线第二次扩展

- **起因**：使用者想学张国良主编《传播学经典理论》（复旦大学出版社）但未购书（"买了也没时间读"）。按规则**先落 raw 再 ingest**（新概念页只允许来自 raw/ 资料摄取）。
- **新增原件**：`raw/-guide.md`——AI 依据传播学界公认经典脉络汇编的导读，**非原书内容复制**；撰写时未能联网核对原书目录（网络搜索未获授权），"本书收录了哪一篇"的判断均属合理推断，全部标"待核实"。
- **新建页面**：source 页 [[-guide]] + **14 个概念页**（TitleCase）：[[PseudoEnvironment]]、[[Stereotype]]、[[LasswellFormula]]、[[Gatekeeping]]、[[TwoStepFlow]]、[[PersuasionResearch]]、[[UsesAndGratifications]]、[[AgendaSetting]]、[[SpiralOfSilence]]、[[CultivationTheory]]、[[BiasOfCommunication]]、[[MediumIsTheMessage]]、[[EncodingDecoding]]、[[CultureIndustry]]。全部与 source 页互链，概念间按理论脉络补双链（拟态环境↔议程设置、守门人↔议程设置、英尼斯→麦克卢汉、文化工业↔编码解码等）。
- **配套产出**：学习导读页面 `learning-materials/communication-classics-guide.html`（六大板块版图 + 14 概念速览表 + 六周学习路线 + AI 帮读五步 + 自测题；作品输出区，未经 ingest，仅登记于 source 页）。
- **更新**：index（Sources + Concepts 两段）、overview（frontmatter sources、来源数 8→10、支线段扩展、修订记录）、raw/README.md（登记新原件）。
- **规模**：wiki 页面 42→**57**（11 source / 7 entity / **31 concept** / 3 synthesis + 5 元页面）。距"本学期 50 个 concept 页"目标差 **19** 个。
- **待核实标注（重要）**：原书出版年份、收录篇目、导言体例；施拉姆《传播学》中译年份；"睡眠者效应""卑鄙世界综合症"等术语译名；科恩名言出处细节。**引原文前必须查原书。**
- **后续可做**：为高频学者补 entity 页（李普曼、拉斯韦尔、拉扎斯菲尔德、施拉姆、麦克卢汉、霍尔等，本次为控制规模未建）；按学习路线每学完一批回填学习进度；联网后核对原书目录并修订"待核实"项。

## [2026-09-13] query | 学习页面：李普曼（拟态环境与刻板成见）

- **起因**：使用者启动《传播学经典理论》学习路线的（李普曼）。
- **配套产出**：`learning-materials/lippmann.html`（九段式，concept-learner 流程：学习目标→核心问题→一句话解释→双流水线机制→算法时代场景→易混淆辨析→3 道自测→来源→个人笔记段）。**无新建 wiki 页面**——[[PseudoEnvironment]]、[[Stereotype]] 概念页此前已建，本页面登记于 source 页 [[-guide]] 的"配套产出"段。
- **来源核验（重要）**：候选链接先实测再入库——古腾堡 64563 实为一本芬兰语小说（猜测的 ID 是错的，**已弃用**），检索后改用 gutenberg.org/ebooks/6456（Public Opinion，已核验标题与作者 ✅）；维基词条被代理拦截、豆瓣反爬，均标"待核实"，未给具体条目链接。落实了 concept-learner 的"禁止伪造链接"规则。
- **页面总数不变**：仍 57 页，concept 页仍 31/50（差 19）——本周是学习配套产出，不产生新概念页。

## [2026-09-13] ingest | 传播学学科材料（）：社会信息系统与传播学的诞生

- **起因**：使用者问"为什么传播学与的学科材料没有写进知识库"。归因：知识库入口只有 `raw/`，而两份学科材料的产物一直留在 `~/Downloads/<课程名>学科材料/`，从未进 `raw/`——属**流程缺口**（已补进 `notes-pipeline` 技能第 6 步）。使用者同意交接**传播学那一份**（阅读课暂不交接）。
- **内容口径（新增规则，适用于所有课程）**：使用者明示"进去的笔记不仅限于传播学都要注意，不要把等写进去，只写知识点等学术性的东西"。因此**未投放原始整理稿版**（其中含规则与），改为撰写**整理** `raw/.md`：只保留定义、理论、学科史、学者贡献与学术论证；**规则、、主题管理、一律剔除**（整理文末附"来源口径"说明）。
- **新增原件**：`raw/.md`（学科材料整理，非原文复制）。
- **新建页面**：source 页 [[]] + **5 个概念页**（[[CommunicationStudies]] 学科定义与研究对象 / [[SocialInformationSystem]] 特点·双重偶然性·两类故障 / [[CommonMeaningSpace]] 共同意义空间 / [[GoldenAgeOfCommunication]] 黄金三十年与诞生五条件 / [[SpiritualIntercourse]] 马克思精神交往理论）+ **1 个 synthesis 页**（[[communication-studies-founding-figures]] 四大奠基人与施拉姆对照表）。
- **补的结构缺口**：此前 14 个传播学理论页"有理论、无总纲、无时间轴、无人"。本次补齐**学科线 + 时间线 + 人物线**，并与 [[LasswellFormula]]、[[Gatekeeping]]、[[PersuasionResearch]]、[[TwoStepFlow]] 四位奠基人的理论页双向互链。
- **更新**：index（Sources + Concepts + Syntheses 三段）、overview（来源数 10→11、支线段扩展、修订记录）、raw/README.md（登记新原件）、四页奠基人理论页补链。
- **规模**：wiki 页面 57→**64**（12 source / 7 entity / **36 concept** / 4 synthesis + 5 元页面）。距"本学期 50 个 concept 页"目标差 **14** 个。
- **待核实标注**：KDKA 1920、BBC 电视 1936、《太阳报》《我们为何而战》伊里县等年份与篇名按教材常识修正，属**推断**；施拉姆访华年份与院校、伊利诺伊大学为**待核实**；马克思精神交往一节为自学内容、按教材常识整理。**引原文前须核对教材。**

## [2026-09-13] query | 学习页面改版：按用户要求嵌入原文（李普曼页）

- **用户反馈**："主题学习要尽可能呈现出原文，毕竟这是在读书。"已沉淀为长期规则（MEMORY 规则 9 + PLAYBOOK 第九节）。
- **落实**：`learning-materials/lippmann.html` 新增"4+ 原文摘录"卡——四段英文原文逐字引自 Gutenberg 全文（第一章拟态环境定义、"同一个世界不同的世界"；第六章"先定义再看见"名句；第七章"成见是自尊的堡垒"），均带白话对照与"看点"提示；来源段注明逐字核验；并加了**版权边界说明**（公版可整段引；版权期文本只短引）。
- **核验过程**：全文下载遇代理掐断，`--http1.1 -C -` 断点续传到完整；grep 词组因硬换行失灵，改单词定位。原凭记忆的 ebook ID 64563 为芬兰语小说，已弃用换 6456。
- **页面总数**：**64 页**，concept **36/50**（差 14）。后续周次的学习页将按此原文原则制作。
  - 更正：本条原记"仍 57 页，concept 31/50"，那是上一次 ingest 之前的旧数，2026-09-13 每日维护复核时更正为当前值。

## [2026-09-13] health | 每日维护：结构体检与日志对齐复核

- 运行 `tools/health.py`（共 64 个页面）：空页 0 / 目录同步 0 / 日志覆盖 0
- 运行 `tools/lint.py`：断链 0 / 孤儿页 0 / 格式违规 0 / 缺页候选 0
- **脚本盲区人工复核 7 项**（`raw/` ↔ source 页双向对应、双链大小写、markdown 链接、命名规范、`log.md` 引用、`type` 与目录匹配、空目录与残页）——**全部通过**：
  - 12 个 source 页的 `source_file` 全部指向 `raw/` 中真实存在的文件
  - `raw/` 的 13 份内容文件与 12 个 source 页一一对应（`concept-relationship.html` 与 `.md` 共用同一页），**无未摄取资料**
  - 双链目标与文件名**大小写完全一致**（GitHub 侧不会断链）；无内容页缺入链（仅 4 个元页面无入链，属正常）
- **日志对齐复核**：比对本日志的 operation 序列与 git 历史，发现 `graph` 操作多次未记录 → 见下方 graph 补记条目

## [2026-09-13] lint | 每日维护：内容体检（确定性 + 语义层人工）

- `tools/lint.py` 确定性部分全绿
- **语义层**（脚本明确声明不覆盖的四项）人工通读结论：
  - **矛盾**：未发现同一字段在两页取值互斥
  - **过时声明**：查出 1 处——「学习页面改版」条目的页面计数用了过期数字 → 已更正
  - **缺失交叉引用**：`index.md` 五段与实际文件完全一致；无内容页缺入链
  - **缺页候选**：脚本报 0，人工另数一遍确认仍有结构缺口（若干被 3 个及以上页面提及、却没有自己页面的概念）——**候选名单只出现在本机私有简报与对话中，不写入本公开日志**
- **格式与命名**：`type` 与所在目录全部一致；concept / entity 页均 TitleCase，source / synthesis 页均 kebab-case

## [2026-09-13] graph | 补记：未单独记录的数次图谱重建（对齐 git 历史）

- **背景**：本日志此前只记了两次图谱操作。现按 `git log -- graph/graph.json` 补记其余各次；节点 / 边数均取自各提交里的 `graph.json`。
- **此前已记录**：
  - `2dc13b8` —— 首次构建，28 节点 / 132 边
  - 「重建知识图谱（内容修订后）」一条，边数与 `7d6e5e0` 吻合（37 节点 / 236 边）
- **补记**：
  - `a5b6d07` 37 节点 / 234 边（工具修复：双链抽取兼容表格内转义竖线后重建）
  - `74c3a5a` 37 节点 / 234 边（工具修复：产物时间戳改为日期精度，边数不变）
  - `7159ef0` 37 节点 / 244 边（新增的 8 条边全部是 `(页面, log, EXTRACTED)` 形态——`log` 新增带双链的记录所致，属预期）
  - `e744203` 38 节点 / 253 边
  - `9acdc5b` 42 节点 / 279 边（随"PUMO + 维基研究课题"两批 meta 更新一并重建）
  - `5edcaad` 57 节点 / 416 边（概念页 17→31 后）
  - `336972a` 64 节点 / 496 边（概念页 →36 后，即当前版本）
- **复核**：重跑 `tools/build_graph.py` 与现有 `graph/graph.json` **逐字节一致** → 图谱与 wiki 内容同步、产物可复现

## [2026-09-14] maintain | 学科材料文件名规范化 + 交付说明同步（README / raw-README / gitignore）

- **性质**：结构维护——**只改文件名与说明文字，不改动任何页面的事实内容**。
- **动作一（文件名规范化）**：`raw/2026-09-12--.md` → `raw/.md`，对齐 `raw/.md` 的 `<课程>-notes-<第几次课>.md` 格式。原名含中文、含大写、以日期开头，与 `raw/README.md` 自身的"建议命名"自相矛盾，且在大小写敏感文件系统上有隐患。
  - 对应 source 页一并更名：`wiki/sources/.md` → `wiki/sources/.md`（slug 与原始文件名对齐）。页面 H1 与正文**未改**。
  - **同步范围**：改动落在 19 个文件里——wiki 侧旧 slug `` 出现于 29 行、旧文件名出现于 19 行（两者部分重叠），另含 source 页的 `source_file` 字段、`index.md`、`overview.md`、`learning-materials/llm-wiki.html`、`raw/llm-wiki.html`、`raw/README.md` 与知识图谱产物。改后残留检查 0 处，`health.py` / `lint.py` 复跑全绿。
- **动作二（交付说明同步）**：`README.md` 此前停在 37 页的旧规模，与 wiki 实际（64 页）脱节。已同步：规模数字改为 64 页 / 64 节点 / 496 边；目录树补齐 `raw/` `wiki/` `graph/` `tools/` `AGENTS.md`；《已生成的学习资料》由 5 行扩为两条线共 9 项；《每日自动维护任务》一节更正为实际执行时间 23:19、实际步骤五步，并写明简报的真实落点。
- **动作三（gitignore 规则去留）**：`wiki/daily-*.md` 一条此前指向不存在的路径（简报实际写在 `.workbuddy/memory/daily/`，已被整目录忽略）。**决定保留**，并改写注释说明其"防御性兜底"定位——日报含个人状态，一旦误落到公开的 `wiki/` 下无法收回；保留成本一行。同时把 README 里的错误路径改为真实路径。
- **动作四（编号补齐）**：`raw/README.md` 的"当前内容"表此前有"之六"而无"之五"（序号断档）。已补"之五：概念关系说明"，并新增「编号说明」交代编号口径 = `concept-learner` 的产出顺序。
- **规范同步**：`AGENTS.md` 的 `log.md` 操作类型增加 `maintain` 一项（原先只有 ingest / query / health / lint / graph / scaffold，无法为本次这类"只动结构不动内容"的操作归类）。
- **校验**：`tools/health.py`、`tools/lint.py` 重跑全绿；`tools/build_graph.py` 重建后图结构与改名前的语义关系一致。
- **说明**：本次为 `raw/` 只读铁律的**唯一例外情形**（纯文件名的规范化重命名），例外条件与执行要求已写进 `raw/README.md` 的「规则」一节。
