# raw/ — 原始资料投放区（只读）

这里放**原始资料**：论文、文章、笔记、会议纪要、书籍摘录、网页存档……

## 规则

- **只放不改**：文件一旦放进 `raw/`，就不再修改、重命名或删除。它是"事实来源"，wiki 里的每一页都要能追溯回这里。
- **AI 只读不写**：Agent 摄取（ingest）时只读取这里的文件，不会改动它们。
- **格式不限**：`.md` 直接读；`.pdf` `.docx` `.pptx` `.xlsx` `.html` `.txt` `.csv` `.json` `.epub` `.mp3` 等由 Agent 先转成 Markdown 再摄取。
- **建议命名**：用能一眼看懂内容的 `kebab-case` 名字，例如 `attention-is-all-you-need.md`。这个文件名会成为 wiki 里 source 页的 slug。

## 怎么用

1. 把资料丢进这个目录；
2. 对 Agent 说：`ingest raw/你的文件名.md`；
3. Agent 会写出 `wiki/sources/` 摘要页，并顺手创建/更新相关的概念页、实体页，把 `wiki/index.md`、`wiki/log.md`、`wiki/overview.md` 一并更新。

## 当前内容

| 文件 | 说明 |
|---|---|
| `llm-wiki-pattern.md` | 本套 LLM Wiki 模式自身的说明（Karpathy 思路 + 参考实现 SamurAIGPT/llm-wiki-agent），即本仓库的"安装说明书" |
| `karpathy-llm-wiki-gist.md` | Karpathy 原始材料（gist `llm-wiki` + X 长帖）的**二手整理**：三层架构、编译器 vs 解释器、index/log 分工、规模与边界、已知瓶颈。**含待核实标注** |

> 注：仓库里已有的 `learning-materials/` 目录（Agent / 上下文 / Skill / 向量数据库 等概念资料）也可作为来源，已在各自 source 页的 `source_file` 字段中登记引用。
