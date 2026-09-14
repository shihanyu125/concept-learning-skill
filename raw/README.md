# raw/ — 原始资料投放区（只读）

这里放**原始资料**：论文、文章、笔记、会议纪要、书籍摘录、网页存档……

## 规则

- **只放不改**：文件一旦放进 `raw/`，就不再修改、重命名或删除。它是"事实来源"，wiki 里的每一页都要能追溯回这里。
  - **唯一例外：纯文件名的规范化重命名**（统一为 `kebab-case`、修正编号）。必须同时满足三条，缺一条就不要动：① **文件内容一字不改**；② 全部引用同步更新（wiki 页面、`source_file`、本 README、`learning-materials/` 里的对应引用）；③ 在 `wiki/log.md` 记一条。
- **AI 只读不写**：Agent 摄取（ingest）时只读取这里的文件，不会改动它们。
- **格式不限**：`.md` 直接读；`.pdf` `.docx` `.pptx` `.xlsx` `.html` `.txt` `.csv` `.json` `.epub` `.mp3` 等由 Agent 先转成 Markdown 再摄取。
- **建议命名**：用能一眼看懂内容的 `kebab-case` 名字，例如 `attention-is-all-you-need.md`。这个文件名会成为 wiki 里 source 页的 slug。
  - **不要**用日期开头，也不要用中文或含大写字母的文件名——日期写进文件正文与 frontmatter 的 `date` 字段即可；含中文/大写的名字在大小写敏感的文件系统上容易出问题。

## 怎么用

1. 把资料丢进这个目录；
2. 对 Agent 说：`ingest raw/你的文件名.md`；
3. Agent 会写出 `wiki/sources/` 摘要页，并顺手创建/更新相关的概念页、实体页，把 `wiki/index.md`、`wiki/log.md`、`wiki/overview.md` 一并更新。

## 当前内容

| 文件 | 类型 | 说明 |
|---|---|---|
| `llm-wiki-pattern.md` | md | 本套 LLM Wiki 模式自身的说明（Karpathy 思路 + 参考实现 SamurAIGPT/llm-wiki-agent），即本仓库的"安装说明书" |
| `karpathy-llm-wiki-gist.md` | md | Karpathy 原始材料（gist `llm-wiki` + X 长帖）的**二手整理**：三层架构、编译器 vs 解释器、index/log 分工、规模与边界、已知瓶颈。**含待核实标注** |
| `agent.html` | html | 概念学习资料之一：Agent。**副本**，原件仍在 `learning-materials/agent.html` |
| `llm-context.html` | html | 概念学习资料之二：大模型的上下文。**副本**，原件仍在 `learning-materials/llm-context.html` |
| `skill.html` | html | 概念学习资料之三：Skill。**副本**，原件仍在 `learning-materials/skill.html` |
| `vector-database.html` | html | 概念学习资料之四：向量数据库。**副本**，原件仍在 `learning-materials/vector-database.html` |
| `concept-relationship.md` | md | 概念学习资料之五（体裁为关系梳理，非单概念九段式）：Agent / 上下文 / Skill 三者如何串成闭环。**副本**，原件仍在 `learning-materials/concept-relationship.md` |
| `concept-relationship.html` | html | 上述关系说明的**网页版**（与 `.md` 同一份内容的两种呈现）。**副本**，原件仍在 `learning-materials/concept-relationship.html` |
| `llm-wiki.html` | html | 概念学习资料之六：LLM Wiki（本仓库自身的组织模式）。**副本**，原件仍在 `learning-materials/llm-wiki.html` |
| `pumo-era.md` | md | 普莫时代（PUMO）概念的原始材料汇编（2025 年利希腾塔勒原论文 + 周敏、陈飞扬 2026 中文论文的可核查事实）。**新增原件**（非副本，非原文复制，由 AI 依据多来源汇编并附全部核查链接），对应概念学习资料 `learning-materials/pumo.html` |

> **编号说明**：上表中「之一～之六」是 `concept-learner` 的**产出顺序**，与 wiki 侧 `index.md`、`log.md` 里"concept-learner 第 6 份产出"的口径一致：Agent → 大模型的上下文 → Skill → 向量数据库 → 概念关系说明 → LLM Wiki。
> 其中**之一～之四是单概念九段式资料，之五是关系梳理（体裁不同），之六回到九段式**。

### 关于那些"副本"（重要）

上表中带"**副本**"标记的 6 个文件，都是从 `learning-materials/` **复制**过来的，**原始文件仍然保留在原处、未被移动或删除**。

之所以要复制进 `raw/`，是因为 `raw/` 才是这套模式的**事实来源层**：wiki 里每一页的 `source_file` 字段都要能指向 `raw/` 中的一份资料。而 `learning-materials/` 属于"作品输出区"，内容可能被继续修订——把来源钉在 `raw/`（只读）上，追溯链才稳定。

核对指纹（md5，写入当日）：

| 文件 | md5 |
|---|---|
| `agent.html` | `c51bd38ada5bbb63506492f572c79324` |
| `llm-context.html` | `46f984074affa946ada6b031cfa3fb7d` |
| `skill.html` | `8a4bee80537a0d6b96720bf5ee5c9130` |
| `vector-database.html` | `98f2bc4e1fa5b89cd7697fb635756772` |
| `concept-relationship.md` | `32e5ead78fa07f4de1507fcfb7c68cc0` |
| `concept-relationship.html` | `4aa97b7285dad64d351c8bf62749c915` |
| `llm-wiki.html` | `68c14456035af308e3a3397d2e7ac926` |

> 注：`concept-relationship.html` 是 `concept-relationship.md` 的网页版（同一份内容的两种呈现），已一并纳入本目录。wiki 中对应的 source 页 `source_file` 仍引用 `.md` 版本（那是 wiki 摘要的编写依据），`.html` 作为同一来源的另一种格式并列存放。

## 变更记录

- **2026-09-14 · 文件名规范化**：把以日期开头、含中文或含大写字母的旧文件名统一为 `kebab-case`（**文件内容一字未改**），并同步更新了全部引用（wiki 双链、`source_file`、`index` / `log` / `overview` 与知识图谱产物）。
- **2026-09-14 · 编号补齐**：当前内容表此前有"之六"却无"之五"，序号断档——现补上"之五：概念关系说明"，并新增上方「编号说明」交代编号口径。
