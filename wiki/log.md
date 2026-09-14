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
  4. [[Automation]] 漏收"什么时候不该建自动化"（3.3 节）与"三个反直觉点"（第五节）→ 补收
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

## [2026-09-13] query | 「LLM Wiki 只能装固定主题的内容吗」——答案回填进 [[LLMWiki]]

- **问题**：使用者问「这个 LLM Wiki 是只能放这门课相关的东西，还是任何想了解的专业知识都可以放进去」
- **取证**：查 `raw/README.md`（投放物定义：论文 / 文章 / 笔记 / 会议纪要 / 书籍摘录 / 网页存档，**格式不限**）、`raw/karpathy-llm-wiki-gist.md`（示例 Farzapedia = 个人材料编译成个人百科）
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

## [2026-09-14] health | 每日维护：结构体检与 7 项人工交叉验证

- **脚本结论**：`tools/health.py` 报 0 处问题——空页 / 残页 0、`index.md` 与实际文件一致（五个段落齐全）、全部 source 页均有 ingest 记录，共 64 个页面。
- **人工 7 项交叉验证**（脚本盲区，逐项通过）：
  1. `raw/` 14 个文件 ↔ 12 个 source 页对应无误（13 份内容文件，其中 `concept-relationship` 有 md 与 html 两种格式；`raw/README.md` 为说明文件不建页），12 个 `source_file` 字段全部指向 `raw/` 下的真实文件。
  2. 双链大小写零错配（macOS 不敏感、GitHub 敏感，此项专门查）。
  3. markdown 相对链接：发现 2 处层级写错并修复，见下方 maintain 条目。
  4. 命名规范 0 处违规（concept / entity 用 TitleCase，source / synthesis 用 kebab-case）。
  5. 日志中引用的文件路径均真实存在。
  6. `type` 取值与所在目录 0 处不匹配。
  7. 无空目录；最短的两个页面是脚本生成的体检报告，属生成物而非残页。
- **顺手对齐**：比对本日志的 operation 序列与 `git log` 的实际动作，补上上方漏记的图谱条目 1 条。

## [2026-09-14] lint | 每日维护：内容体检（确定性 + 语义层人工）

- **脚本结论**：`tools/lint.py` 确定性部分全绿——断链 0、孤儿页 0、格式违规 0、缺页候选 0。
- **语义层人工检查**（脚本明确声明不覆盖的部分）：逐页通读 64 页，未发现跨页矛盾或过时摘要；发现 1 处**过时声明**（overview 的来源计数与实际不符）并已更正，见下方 maintain 条目。
- **缺口重数**：不信「缺页候选 0」这个结论，按"被 ≥2 个页面提及却无自身页面"的判据人工重列候选词再数一遍，确实仍有若干缺口（脚本判据对缩写与中文概念名不敏感，此现象已连续三次复现）。
- **说明**：本轮新候选只进入本机私有的征询环节（`.workbuddy/memory/`，不上传），按约定**不在本页、不在任何公开页面列出候选名**。

## [2026-09-14] maintain | 修复相对链接层级 + 校正 overview 来源计数与元数据

- **性质**：结构维护——只改链接路径、元数据与计数表述，**不改动任何页面的事实内容**。
- **动作一（链接层级）**：`wiki/sources/llm-wiki-learning-material.md` 的「来源说明」段把两级上跳误写成一级（`../raw/` 与 `../learning-materials/`）。从 `wiki/sources/` 解析会指向并不存在的 `wiki/raw/` 与 `wiki/learning-materials/`，**在本地与 GitHub 上都是断链**。已改为 `../../`（2 处），并同步该页 `last_updated`。说明：`tools/lint.py` 只检查 wiki 双链，这类 markdown 相对链接只能靠人工检查。
- **动作二（元数据）**：`wiki/overview.md` 的 `sources` 字段此前只列 10 个 slug，漏了 `llm-wiki-learning-material`；已补齐并把 `last_updated` 改为 2026-09-14。
- **动作三（过时计数）**：同页正文原写"已摄取 11 份来源"，与实际 12 份不符；支线一节的来源序号（第 9 / 第 10 / 第 11 份）随之各偏小 1。已按 `wiki/sources/` 实际页面数与 `git log --diff-filter=A` 的建立顺序更正为 12 份并顺延序号，另补记此前漏记的第 9 份来源条目。校正后与 `README.md` 的"12 个 source"一致。
- **校验**：`tools/health.py`、`tools/lint.py` 复跑全绿；另重建知识图谱以纳入新增的双链。

## [2026-09-14] ingest | 用户批准 5 条概念候选 —— 新建 5 个概念页（传播学线与 AI 线各补一块）

- **性质**：**零新来源的扩建摄取**。本仓库 `raw/` 无新增文件（14 个文件与 12 个 source 页的对应关系不变），材料来自既有 source 页 + 外部一手材料。
- **前置**：用户 2026-09-14 对当日每日维护征询的 5 条候选**逐条点头**（此前规则是"只提请求、不落盘"）。五条已先写入本机私有清单的「已批准 · 待建页」区，再开始建页。
- **新建 5 个概念页**（concept 36 → 41）：
  - `concepts/PublicOpinion.md`（舆论 / 公众舆论）——材料：Project Gutenberg 电子书 #6456《Public Opinion》(1922) 公版全文。**逐字核验**：定义段（"the pictures inside the heads … are their public opinions"）与三角关系段两处英文引用均从全文摘出，仅合并硬换行、未改字；同批核对确认 #76966 是同一作者的《幻影公众》(1925)，两本未混。
  - `concepts/TypesOfCommunication.md`（传播的类型与层次）——材料：传播学通行教材与学科基础文献。
  - `concepts/OpinionLeader.md`（意见领袖）——把原挂在两级传播页内的**角色**部分拆出独立成页，含与两级传播 / 守门人 / KOL 的三张辨析表；原页保留"结构"主线并互链。
  - `concepts/InternationalCommunication.md`（国际传播）——材料：程曼丽《信息全球化时代的国际传播》（定义、两部分组成、三个特征逐字引用）、北师大周敏与陈飞扬 2026《新闻界》论文 PDF（下载后按页提取文本核对）、`raw/pumo-era.md`。
  - `concepts/MCP.md`（Model Context Protocol）——材料：MCP 官方文档两篇与 Anthropic 2024-11-25 开源公告（官方定义、host/client/server 三角色、tools/resources/prompts 三原语均逐字摘出）。
- **来源层说明**：上列外部一手材料（官方文档、期刊论文、公版全文、央视网刊文）**均未进入 `raw/`**——`raw/` 是公开层，新增文件须先经用户同意。故 `concepts/MCP.md` 的 `sources` 字段为空，其余新页的 `sources` 只列既有 source 页 slug；各页「来源」段均已写明 URL、抓取日期与核验方式。
- **回填双链 11 处**：`overview.md`、`index.md`、`entities/Anthropic.md`、`concepts/ToolUse.md`、`concepts/PseudoEnvironment.md`、`concepts/Stereotype.md`、`concepts/TwoStepFlow.md`、`concepts/SpiralOfSilence.md`、`concepts/PumoEra.md`、`sources/pumo-era.md`、`syntheses/communication-studies-founding-figures.md`。
- **关闭的缺口**：`overview.md` 空白清单第 1 条（MCP，"被页面提到却无页"）标记为已收口；`entities/Anthropic.md` 与 `concepts/ToolUse.md` 两处「待补充」段中原指向 MCP 的条目改写为已建页。
- **元页面**：`index.md` 的 Concepts 段新增 5 条并同步 `last_updated`；`overview.md` 支线新增"同日第四次扩展"段与一条修订记录；两份体检报告以 `--save` 刷新。
- **待核实**：各新页文末均列待核实项（意见领袖的类型学与测量方法、国际传播的中文译名对应、MCP 是否已移交外部标准组织、公版书中文译本页码等），**未联网核实者一律未写入正文**。
- **下一步**：其余仍待用户逐条点头的历史候选，本轮**未建立任何页面**；按约定，候选名称**不写入公开层**（只存本机私有目录）。


## [2026-09-15] maintain | 内容结构调整：来源层与主题页整理，概念页来源表述统一

- **范围**：对来源层与主题页做一次结构整理，撤下若干不再需要的来源页与主题页，保留的学科概念页统一为**中性的来源表述**。
- **概念页**：正文与 frontmatter 的 `sources` 一律改为中性的"教材表述 / 通用共识"口径，删去已撤页面的双向链接，避免断链；共 33 个页面更新 `last_updated`。
- **结构性文件同步**：`README.md`（用途、目录树、产出表、规模数字）、`raw/README.md`（当前内容表）、`wiki/index.md`（Sources / Concepts / Syntheses 三段）、`wiki/overview.md`、`learning-materials/llm-wiki.html` 与 `raw/llm-wiki.html` 同步更新。
- **图谱**：重跑 `tools/build_graph.py` 重新生成。
- **理由**：来源层只保留仍然在库、可追溯的资料；概念页保留学科知识本体，来源表述统一到通用口径。
