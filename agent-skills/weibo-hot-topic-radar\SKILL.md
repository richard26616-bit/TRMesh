---
name: weibo-hot-topic-radar
title: Weibo Hot Topic Radar
platform: weibo
version: 1.0.0
tools:
  - weibo.profile.lookup
  - weibo.content.search
  - weibo.comment.summary
---

# Weibo Hot Topic Radar

Monitor Weibo accounts, posts, hot topics, and discussion sentiment.

Inputs:

- `target`: account, post URL, keyword, or topic
- `objective`: monitoring goal
- `language`: output language

Process:

1. Gather available Weibo topic and content data.
2. Summarize trend direction, audience reaction, and risk signals.
3. Identify relevant stakeholders, narratives, and content angles.
4. Return a concise radar report.

Rules:

- Do not make unsupported claims about virality.
- Label inference explicitly.
- Keep outputs suitable for operations review.
