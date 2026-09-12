---
title: "Token（词元）"
type: concept
tags: [llm, token, tokenization, context-window, core-concept]
sources: [llm-context]
last_updated: 2026-09-13
---

# Token（词元）

## 定义

**token（词元）是模型切分与计量文本的最小单位。**

模型并不按"字"或"词"来处理文本：它先把文本切成 token 序列，再以 token 为单位计算输入、输出与上下文占用。[[Context|上下文窗口]]的大小、生成的速度、API 的计费，用的都是同一把尺子——token。

## 核心机制

- **切分方式（分词 / tokenization）因模型而异**：同一句话在不同模型下可能被切成不同数量的 token，所以"多少个字"不能直接倒推出"多少个 token"。
- **粗略估算**（原资料给出的换算，仅供心里有数）：
  - 英文：1 token ≈ 0.75 个单词 ≈ 4 个英文字符
  - 中文：一个常用汉字通常对应 1–2 个 token，取决于该模型的分词方式
- **三类占用共同计入窗口**：**输入 token**（你给的）+ **输出 token**（模型生成的）+ 部分模型的**推理 token**（模型"思考"用的）。
- **超限即截断**：token 总数超过窗口上限时，最早的内容被挤出去。

## 为什么这个单位重要

1. **它把"记不记得住"变成可计算的量**：窗口是 128k token、当前对话已用 120k——还剩多少余量是能算的，而不是凭感觉。
2. **它是"容量"与"成本"共用的尺子**：占 token 就是占窗口，通常也等于花钱。
3. **它让"精简地喂信息"有了依据**：省下的不是抽象空间，而是实打实的额度。见 [[ProgressiveDisclosure]]、[[ContextManagement]]。

## 常见误区

- **一个字 ≠ 一个 token**：中文里一个字可能被切成 1–2 个 token，也可能多个字合并成一个 token。
- **窗口 128k ≠ 能写 128k 字**：窗口是输入 + 输出 + 推理的**总和**，不只是输出长度。见 [[Context]]。
- **别用字数精确倒推 token**：不同模型分词不同；要精确就得用该模型自己的分词器（tokenizer）来算。

## 关联

- [[Context]] — token 是上下文（窗口）的计量单位
- [[ContextManagement]] — 管理上下文，本质上就是在管理 token 预算
- [[ProgressiveDisclosure]] — 省上下文，省的就是 token
- [[Memory]] — 记忆的"取回"环节要花 token 把内容重新放回上下文
- [[OpenAI]] — 128k 示例与 token 计量说明的来源方
- 来源页：[[llm-context]]

## 来源

- `raw/llm-context.html` 第 2 节"核心机制 / 组成"—— token 的定义、换算估算、三类占用
- OpenAI《Conversation state》—— 上下文窗口定义与 token 计量。见 [[OpenAI]]
- **待核实**：具体换算比例系原资料标注的"粗略估算"，不同模型差异较大，不作为精确依据。
