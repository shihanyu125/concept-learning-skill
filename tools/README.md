# tools/ — 零依赖脚本

这里的脚本**只用 Python 标准库**，不需要 `pip install` 任何东西，也不需要 API Key。

## 快速开始

```bash
# 结构体检（快、免费、每次会话都可以跑）
python3 tools/health.py

# 内容体检（确定性部分，便宜）
python3 tools/lint.py

# 建知识图谱 → graph/graph.json + graph/graph.html
python3 tools/build_graph.py
```

其它常用参数：

```bash
python3 tools/health.py --json          # 机器可读输出
python3 tools/health.py --save          # 另存为 wiki/health-report.md
python3 tools/lint.py --min-mentions 3  # 被提及几次才算"缺页候选"
python3 tools/build_graph.py --open     # 生成后用浏览器打开
python3 tools/build_graph.py --no-inferred   # 只保留双链边，不要推断边
```

> ⚠️ 不要用 `python tools/xxx.py`（可能指向系统里的旧版本 Python）。
> 本项目使用 Python 3.12/3.13，命令里的 `python3` 请确保指向你的目标版本。

## 三个脚本各自管什么

| 脚本 | 范围 | 是否调用 LLM | 成本 |
|---|---|---|---|
| `health.py` | **结构完整性**：空页/残页、index 与实际文件是否同步、source 页有没有对应的 ingest 日志 | 零调用 | 免费 |
| `lint.py` | **内容质量（确定性部分）**：断链、孤儿页、frontmatter 格式违规、缺页候选 | 零调用 | 免费 |
| `build_graph.py` | **知识图谱**：两遍建图 + 社区聚类 + 可视化 | 零调用 | 免费 |

**顺序上先跑 health，再跑 lint。** 对内容质量做分析之前先确认结构没坏——否则就是在给一个空文件做语义检查。

## lint.py 覆盖不到的部分

以下检查**需要语义理解**，脚本做不了，得由 Agent（也就是我）来读、来判断：

- 跨页面的**矛盾**：两页对同一件事说法不一致
- 被新来源取代的**过时声明**
- 该建链却漏建的**缺失交叉引用**
- 可以通过外部搜索填补的**数据空白**

所以 `lint.py` 报"全部通过"，只代表**确定性检查**通过，不代表 wiki 内容没问题。

## build_graph.py 的建图方式

参照 LLM Wiki 规范的两遍构建：

1. **第一遍（确定性）**：解析所有页面里的 `[[双链]]` → 边标记 `EXTRACTED`，置信度 1.0
2. **第二遍（推断）**：找出"共享来源高度重合、但双链上没有直连"的页面 → 边标记 `INFERRED`，带 `confidence`（来源集合的 Jaccard 相似度，阈值 0.5）

**社区检测**用 Louvain 第一层（贪心模块度优化），纯标准库手写实现，不依赖 networkx。只做节点级聚合，不做第二层折叠——对 wiki 这个规模已经够用，且结果可复现（随机种子固定）。

> 与参考实现的差异：原项目用 `networkx` + `python-louvain`。这里为了避免装依赖，自己实现了一层。

`graph.html` 是**零依赖**的：不加载任何 CDN，用 canvas 手写力导向布局，**断网也能打开**。支持的交互：拖拽节点、滚轮缩放、空白处拖动平移、悬停高亮邻居并显示该页信息。

## 参考实现里有、但这里没装的脚本

| 脚本 | 为什么没装 |
|---|---|
| `ingest.py` | 摄取需要 LLM 判断"该建哪些实体/概念页"，在 Agent 环境里由 Agent 直接完成，不需要脚本 |
| `query.py` | 同上，提问与综合由 Agent 完成 |
| `heal.py` | 自修复同样依赖语义判断（怎么算"缺失的结构性概念"是个判断题） |
| `pdf2md.py` / `file_to_md.py` | 格式转换可以用 `markitdown`，但它是第三方依赖；当前仓库的资料本来就是 Markdown/HTML，暂不需要 |

**这是刻意的取舍**：三个能真跑、有测试的脚本，胜过八个半成品。

## 文件说明

| 文件 | 作用 |
|---|---|
| `wiki_lib.py` | 公共库：目录定位、frontmatter 解析（不依赖 PyYAML）、双链抽取（会剥掉代码块里的示例）、日志解析、终端配色 |
| `health.py` | 结构体检 |
| `lint.py` | 内容体检（确定性部分） |
| `build_graph.py` | 建图与可视化 |
