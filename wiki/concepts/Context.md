---
title: "Context（上下文 / 上下文窗口）"
type: concept
tags: [llm, context-window, token, memory, core-concept]
sources: [llm-context, agent, concept-relationship]
last_updated: 2026-09-13
---

# Context（上下文）

## 定义

**上下文是模型单次请求里能"看到"的全部内容**；**上下文窗口（context window）是这堆内容的总量上限**，以 [[Token|token（词元）]] 计量。装不下的部分会被截断，模型相当于"忘了"。

组成：**输入 token**（你给的）+ **输出 token**（模型生成的）+ 部分模型的**推理 token**（模型"思考"用的）。

## 核心机制

- **计量单位是 [[Token|token（词元）]]**：模型把文本切成的最小单位。粗略换算——英文 1 token ≈ 0.75 个单词（约 4 字符）；中文一个常用汉字约 1–2 个 token，取决于分词方式。
- **窗口有上限**：不同模型不同，例如 gpt-4o 为 128k token。
- **超限即截断（truncated）**：最早的内容被挤出去。这是长对话里 AI"选择性遗忘"的根因。
- **窗口内平等**：窗口里每条信息被同等对待，AI 不会像人一样"只记住重点"——所以你塞什么，它就平等地占地方。

## 三条推论（它为什么重要）

1. 上下文**大小** = Agent 的眼界：窗口越大，一次能参考的信息越多，长任务越不容易"忘事"。
2. 上下文**内容** = 判断质量：塞进不相关或冗长的信息，会挤占窗口，反而让 Agent"看不清重点"。
3. 窗口**满了会遗忘**：这是长任务里 Agent 表现下滑的常见原因——也正是 [[ContextManagement]] 要处理的那件事。

## 使用边界（易混淆点）

- **上下文 ≠ 长期记忆**：上下文是"这一次对话当下能看到"的，用完即散；长期记忆跨对话持久保存。见 [[Memory]]。
- **上下文窗口 ≠ 输出长度**：窗口是"输入 + 输出 + 推理"的总和，不只是模型能写多长。
- 空间宝贵：应**精简地喂信息**，而不是一股脑全丢进去。见 [[ProgressiveDisclosure]]。

## 关联

- [[Agent]] — 上下文是 Agent 的工作记忆
- [[agent-context-skill-relationship]] — 综合页：上下文在 Agent / Skill 三角中的位置，以及"上下文大小 = 眼界"这条因果链
- [[Token]] — 上下文的计量单位；窗口大小就是 token 额度
- [[ContextManagement]] — 窗口满了之后的应对手段（编辑 / 压缩 / 外置）
- [[Skill]] — 靠 [[ProgressiveDisclosure]] 节省上下文
- [[Memory]] — 对照面：跨对话持久保存，但必须借上下文才能生效
- [[RetrievalAugmentedGeneration]] — 本质是"把外部知识按需搬进上下文"
- [[LLMWiki]] — 编译式知识库，避免每次重灌上下文
- 来源页：[[llm-context]]、[[agent]]、[[concept-relationship]]

## 来源

- OpenAI《Conversation state》之 Managing the context window
- Anthropic《Managing context on the Claude Developer Platform》《Context windows》
- 见 [[OpenAI]]、[[Anthropic]]
