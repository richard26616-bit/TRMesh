---
name: youtube-comment-insight
title: YouTube Comment Insight
platform: youtube
version: 1.0.0
tools:
  - youtube.content.search
  - youtube.comment.summary
---

# YouTube Comment Insight

Summarize YouTube comment themes for product feedback, audience insight, and content planning.

Inputs:

- `target`: video URL, channel, keyword, or topic
- `objective`: comment analysis goal
- `language`: output language

Process:

1. Gather available video and comment signals.
2. Cluster questions, praise, objections, requests, and risk themes.
3. Translate comment patterns into product, content, or sales actions.
4. Return a concise comment insight report.

Rules:

- Do not quote unavailable comments.
- Do not infer private user data.
- Separate observed themes from recommendations.
