---
title: "Anthropic"
type: entity
tags: [company, ai-lab, source-provider]
sources: [agent, skill, llm-context]
last_updated: 2026-09-13
---

# Anthropic

## 是什么

AI 公司，Claude 系列模型的开发者，也是 [[Agent]]、[[Skill]]、[[Context]] 三个页面最主要的一手来源提供方。其工程博客与官方文档在本 wiki 中被大量引用。

## 提供的核心材料

| 主题 | 文档 |
|---|---|
| [[Agent]] / [[Workflow]] | 工程指南《Building Effective Agents》(2024-12, Erik Schluntz & Barry Zhang) —— 定义了 Agent 与 Workflow 的分野、增强型 LLM 的三种能力 |
| [[Skill]] / [[ProgressiveDisclosure]] | 公告《Introducing Agent Skills》(2025-10)；工程博客《Equipping agents for the real world with Agent Skills》；Claude Code 文档《Extend Claude with skills》 |
| [[Context]] / [[ContextManagement]] | 公告《Managing context on the Claude Developer Platform》（context editing 与记忆工具，应对长任务超出窗口）；文档《Context windows》（含 context rot 现象与 token 计数） |
| [[MCP]] / [[ToolUse]] | 公告《Introducing the Model Context Protocol》(2024-11-25) —— 开源 MCP；规范与 SDK、Claude Desktop 的本地 server 支持、开源 server 仓库 |

## 值得记住的两个立场

1. **能用简单方案就不要上 Agent**：Anthropic 明确主张简单任务用一次 LLM 调用或 Workflow 即可。
2. **上下文需要主动管理**：长任务超出窗口是必然，因此提供了上下文编辑与记忆工具来应对。

## 关联

- [[OpenAI]] — 另一家主要来源方，两家文档在本 wiki 中常互为交叉印证
- [[Agent]]、[[Skill]]、[[Context]]、[[Workflow]]、[[ProgressiveDisclosure]]
- [[MCP]] — Anthropic 2024-11-25 开源、由**本家主导**的接入协议（2026-09-14 建页）

## 待补充

可补充：Claude 各代模型的窗口规格；MCP 与 [[Skill]] 在真实工作流里的配合方式——[[MCP]] 页已给出"连接层 vs 流程层"的分工框架，但缺实际案例。
