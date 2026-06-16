---
name: x-topic-monitor
title: X Topic Monitor
platform: x
version: 1.0.0
tools:
  - x.profile.lookup
  - x.content.search
  - x.comment.summary
---

# X Topic Monitor

Monitor X accounts, posts, keywords, and discussion themes for social listening and market research.

Inputs:

- `target`: account, post URL, keyword, or topic
- `objective`: monitoring goal
- `language`: output language

Process:

1. Resolve the topic or account.
2. Gather available posts, engagement, and conversation signals.
3. Cluster themes, sentiment, risks, and influential angles.
4. Return a monitoring summary and recommended follow-up queries.

Rules:

- Use registered SDCenter tools only.
- Distinguish facts from interpretation.
- Do not infer private user attributes.
