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

| 文件 | 类型 | 说明 |
|---|---|---|
| `llm-wiki-pattern.md` | md | 本套 LLM Wiki 模式自身的说明（Karpathy 思路 + 参考实现 SamurAIGPT/llm-wiki-agent），即本仓库的"安装说明书" |
| `karpathy-llm-wiki-gist.md` | md | Karpathy 原始材料（gist `llm-wiki` + X 长帖）的**二手整理**：三层架构、编译器 vs 解释器、index/log 分工、规模与边界、已知瓶颈。**含待核实标注** |
| `2026-09-12--.md` | md | 资料，四个主题：记忆系统（三层分工）、LLM Wiki（编译器 vs 解释器）、自动化（一次性/周期性）、选模型策略（轻量/默认/强推理） |
| `agent.html` | html | 概念学习资料之一：Agent。**副本**，原件仍在 `learning-materials/agent.html` |
| `llm-context.html` | html | 概念学习资料之二：大模型的上下文。**副本**，原件仍在 `learning-materials/llm-context.html` |
| `skill.html` | html | 概念学习资料之三：Skill。**副本**，原件仍在 `learning-materials/skill.html` |
| `vector-database.html` | html | 概念学习资料之四：向量数据库。**副本**，原件仍在 `learning-materials/vector-database.html` |
| `concept-relationship.md` | md | 概念关系说明：Agent / 上下文 / Skill 三者如何串成闭环。**副本**，原件仍在 `learning-materials/concept-relationship.md` |

### 关于那些"副本"（重要）

上表中带"**副本**"标记的 5 个文件，都是从 `learning-materials/` **复制**过来的，**原始文件仍然保留在原处、未被移动或删除**。

之所以要复制进 `raw/`，是因为 `raw/` 才是这套模式的**事实来源层**：wiki 里每一页的 `source_file` 字段都要能指向 `raw/` 中的一份资料。而 `learning-materials/` 属于"作品输出区"，内容可能被继续修订——把来源钉在 `raw/`（只读）上，追溯链才稳定。

核对指纹（md5，写入当日）：

| 文件 | md5 |
|---|---|
| `agent.html` | `c51bd38ada5bbb63506492f572c79324` |
| `llm-context.html` | `46f984074affa946ada6b031cfa3fb7d` |
| `skill.html` | `8a4bee80537a0d6b96720bf5ee5c9130` |
| `vector-database.html` | `98f2bc4e1fa5b89cd7697fb635756772` |
| `concept-relationship.md` | `32e5ead78fa07f4de1507fcfb7c68cc0` |

> 注：`learning-materials/` 里另有 `concept-relationship.html`（上述 `.md` 的网页版），**未**复制进本目录——wiki 中对应的 source 页引用的是 `.md` 版本。至此，wiki 所有 source 页的 `source_file` 均已指向 `raw/`。
