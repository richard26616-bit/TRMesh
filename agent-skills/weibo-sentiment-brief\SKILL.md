---
name: weibo-sentiment-brief
title: Weibo Sentiment Brief
platform: weibo
version: 1.0.0
tools:
  - weibo.content.search
  - weibo.comment.summary
---

# Weibo Sentiment Brief

Create a Weibo sentiment brief for brands, topics, incidents, or campaigns.

Inputs:

- `target`: brand, product, keyword, hashtag, or topic
- `objective`: sentiment brief goal
- `language`: output language

Process:

1. Search available Weibo content through registered tools.
2. Cluster sentiment, narratives, concerns, and repeated claims.
3. Highlight escalation risks and response opportunities.
4. Return concise findings and suggested actions.

Rules:

- Do not overstate evidence.
- Mark sparse data.
- Do not call unregistered resources.
