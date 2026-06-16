---
name: wechat-topic-monitor
title: WeChat Topic Monitor
platform: wechat
version: 1.0.0
tools:
  - wechat.content.search
  - wechat.comment.summary
---

# WeChat Topic Monitor

Monitor WeChat public content topics for brand, category, or campaign research.

Inputs:

- `target`: topic, keyword, account set, or campaign
- `objective`: monitoring goal
- `language`: output language

Process:

1. Search available WeChat public content through registered tools.
2. Cluster narratives, audience questions, and risk signals.
3. Identify content gaps, message opportunities, and follow-up searches.
4. Return a topic monitoring brief.

Rules:

- Do not access private conversations.
- Mark unavailable evidence clearly.
- Use only registered tools.
