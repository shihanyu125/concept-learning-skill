---
title: "MCP（Model Context Protocol）"
type: concept
tags: [mcp, protocol, tool-use, agent-platform, anthropic, context]
sources: []
last_updated: 2026-09-14
---

# MCP（Model Context Protocol）

**一句话**：MCP 是 **AI 应用接外部世界的"通用插座"**——以前每接一个数据源或工具都要单独写一套对接代码，现在大家统一插同一个口。

## 官方定义（原文）

> MCP (Model Context Protocol) is an **open-source standard for connecting AI applications to external systems**. Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks. **Think of MCP like a USB-C port for AI applications.** Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

（出自 MCP 官方文档《What is the Model Context Protocol (MCP)?》，逐字摘出，仅保留重点加粗。）

**白话**：USB-C 之前，每个牌子的手机、电脑、耳机各用各的接口，出门得带一把线；USB-C 之后，一根线走天下。MCP 想干的就是这件事——把"AI 接系统"从各家自定义，变成一根通用线。

## 诞生背景

- **2024-11-25 由 Anthropic 开源**。官方公告原文：*Today, we're open-sourcing the Model Context Protocol (MCP)*；文中说明 *MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers*。
- **要解决的痛点**（公告原文）：*Every new data source requires its own custom implementation, making truly connected systems difficult to scale.*（每来一个新数据源就要写一套自定义实现，真正连通的系统难以规模化。）
- **它的定位**（公告原文）：*a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol*（用单一协议取代碎片化的集成），目标是 *help frontier models produce better, more relevant responses*。
- 发布时同时给出的三样东西：MCP 规范与 SDK、Claude Desktop 的本地 MCP server 支持、一个开源的 MCP server 仓库。

## 三个角色（架构）

官方定义，逐字摘出：

| 角色 | 原文定义 | 白话 |
|---|---|---|
| **MCP Host** | *The AI application that coordinates and manages one or multiple MCP clients* | 那个 AI 应用本身（如 Claude Code / Claude Desktop） |
| **MCP Client** | *A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use* | 应用为**每个** server 单独开的一个连接器 |
| **MCP Server** | *A program that provides context to MCP clients* | 真正去读你的文件、连你的数据库、调你的 API 的那一端 |

关系：Host 为每个 Server 创建一个专属 Client，各持一条独立连接。本地 server 通常走 **STDIO** 传输、服务单个 client；远程 server 走 **Streamable HTTP**、服务多个 client。官方特别说明：**"MCP server"指的是提供上下文数据的程序，与它跑在哪里无关**（本地、远程都行）。

## 三类核心能力（Server 端对外暴露的原语）

官方原文：*MCP defines three core primitives that servers can expose.*

| 原语 | 官方定义 | 白话 | 对应的既有页面 |
|---|---|---|---|
| **Tools** | *Executable functions that AI applications can invoke to perform actions*（如文件操作、API 调用、数据库查询） | **能动手的**：让 AI 真的去执行 | [[ToolUse|工具调用]] 是本页的邻居概念 |
| **Resources** | *Data sources that provide contextual information to AI applications*（如文件内容、数据库记录、API 响应） | **能读的**：给 AI 补上下文原料 | [[Context]]、[[RetrievalAugmentedGeneration|检索增强生成]] |
| **Prompts** | *Reusable templates that help structure interactions with language models*（如系统提示、少样本示例） | **现成的说法模板**：可复用的交互骨架 | [[Prompt]] |

交互方法也统一：发现用 `*/list`、读取用 `*/get`，执行则只有 Tools 有（`tools/call`）。

## 与既有概念的分工（本页的重点）

| 概念 | 它管什么 | 与 MCP 的关系 |
|---|---|---|
| [[ToolUse]] 工具调用 | **能力**：模型怎么决定调用一个工具 | MCP 是让这些工具**可被标准接入**的协议——能力是"会开车"，MCP 是"统一了加油口" |
| [[Skill]] 技能包 | **说明书**：这类任务怎么做，按需加载给模型看 | 两者都让 AI "更能干活"，但一层在**连接**、一层在**流程**；一个 Skill 可以内含"用哪个 MCP server"的步骤 |
| [[Prompt]] 提示词 | 一次性的说法 | MCP 的 Prompts 原语是"可复用的模板"，与提示词分层（系统/开发者/用户）是**不同维度**的分类 |
| [[ProgressiveDisclosure]] 渐进式披露 | 按需加载，别一次吃满 | MCP 的 `*/list` → `*/get` 就是这个思路的连接层版本：**先列目录，再取内容** |

## 日常形态：你其实天天在用它

本 wiki 的载体（[[WorkBuddy]]）里的**连接器**就是 MCP 的落地面——你在连接器管理页看到的每一个外部服务（邮箱、日程、云文档……），背后就是一个 MCP server。所以"点一下连接器就能让 AI 读我的邮件"这件事，靠的不是 AI 变聪明了，而是**接口统一了**。

同理，官方文档强调 *build once and integrate everywhere*（一次开发、到处集成）：Claude、ChatGPT、VS Code、Cursor 等都已支持 MCP，写一个 server 能同时被多家客户端用。

## 使用边界

- MCP 解决的是**怎么接**（协议与传输），**不解决"接了以后该不该用、能用到什么程度"**——权限控制、护栏、审计属于另外一层（与 [[ToolUse]] 提到的 guardrails 同一类问题）。
- 接得越多不等于越好：每个 server 都可能往上下文里塞内容，**上下文仍然有限**（见 [[Context]]）——这是 MCP 普及之后的老问题换了个地方出现。

## 来源

- **外部一手来源（未进本仓库 `raw/`）**：
  - MCP 官方文档《What is the Model Context Protocol (MCP)?》——`https://modelcontextprotocol.io/docs/getting-started/intro`（2026-09-14 抓取）
  - MCP 官方架构文档（Participants 与 Primitives 两节）——`https://modelcontextprotocol.io/docs/learn/architecture`（2026-09-14 抓取）
  - Anthropic 公告《Introducing the Model Context Protocol》——`https://www.anthropic.com/news/model-context-protocol`（2026-09-14 抓取；含发布日 2024-11-25 与创建者姓名）
- **⚠️ 来源层说明**：本页材料来自上述**外部官方文档**，**尚未进入 `raw/` 来源层**（`raw/` 是公开层，新增任何文件都需先经本人同意）。因此本页 `sources` 字段为空。若日后把这几份文档归档进 `raw/`，应改为对应 slug。
- **通用共识 / 推论（已标注）**："USB 线的类比是官方自己给的"之外，"Skill 与 MCP 一层在流程一层在连接""接得越多上下文越挤"两句是**整理时的推论**，非官方表述；"连接器 = MCP 的落地面"是依据本仓库与平台实际形态的**反推**，非官方文档直述。

## 待核实

- MCP 是否已经移交给某个基金会或标准组织（如 Linux Foundation 体系）：2024-11-25 的公告中**未提及**任何移交，公告口径仍是 Anthropic 主导的开源协作项目。2025 年以后的治理变化**未联网核实**。
- 规范各版本号与传输方式（STDIO / Streamable HTTP / SSE 的演进）的对应关系：官方文档有版本化路径，本页未逐版比对。
