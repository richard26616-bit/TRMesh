---
name: wechat-channel-brief
title: WeChat Channel Brief
platform: wechat
version: 1.0.0
tools:
  - wechat.profile.lookup
  - wechat.content.search
  - wechat.comment.summary
---

# WeChat Channel Brief

Create concise research briefs for WeChat Channels accounts, videos, and public content signals.

Inputs:

- `target`: channel, video URL, keyword, or topic
- `objective`: brief goal
- `language`: output language

Process:

1. Collect available public account and content data.
2. Summarize topic, audience reaction, and content pattern.
3. Highlight risks, collaboration value, and next actions.
4. Return a brief suitable for business review.

Rules:

- Do not access unregistered external resources.
- Do not fabricate private WeChat data.
- Separate observed evidence from inferred recommendations.
