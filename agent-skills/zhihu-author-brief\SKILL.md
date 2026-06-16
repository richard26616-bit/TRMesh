---
name: zhihu-author-brief
title: Zhihu Author Brief
platform: zhihu
version: 1.0.0
tools:
  - zhihu.profile.lookup
  - zhihu.content.search
  - zhihu.comment.summary
---

# Zhihu Author Brief

Create a Zhihu author brief for expert discovery, partnership research, or topic mapping.

Inputs:

- `target`: author profile, name, answer URL, or topic
- `objective`: author research goal
- `language`: output language

Process:

1. Resolve available author and content signals.
2. Summarize expertise themes, audience reaction, and topic coverage.
3. Identify collaboration fit, credibility signals, and risks.
4. Return an author brief with follow-up queries.

Rules:

- Do not infer private credentials.
- Distinguish observed expertise signals from assumptions.
- Use only registered SDCenter tools.
