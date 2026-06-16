---
name: x-sentiment-watch
title: X Sentiment Watch
platform: x
version: 1.0.0
tools:
  - x.content.search
  - x.comment.summary
---

# X Sentiment Watch

Track X sentiment around a brand, product, public topic, or campaign.

Inputs:

- `target`: brand, product, keyword, hashtag, or topic
- `objective`: sentiment monitoring goal
- `language`: output language

Process:

1. Search available X content through registered tools.
2. Cluster positive, negative, neutral, and uncertain themes.
3. Highlight recurring claims, objections, and risk signals.
4. Return a sentiment watch report with next queries.

Rules:

- Do not overstate sample representativeness.
- Label uncertain or sparse data.
- Do not call external URLs directly.
