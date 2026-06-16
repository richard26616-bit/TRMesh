---
name: bilibili-video-analysis
title: Bilibili Video Analysis
platform: bilibili
version: 1.0.0
tools:
  - bilibili.profile.lookup
  - bilibili.content.search
  - bilibili.comment.summary
---

# Bilibili Video Analysis

Analyze Bilibili creators, videos, comments, and topic trends for Chinese content research.

Inputs:

- `target`: creator, video URL, keyword, or topic
- `objective`: analysis goal
- `language`: output language

Process:

1. Retrieve available creator and video metadata.
2. Summarize content structure, audience comments, and engagement signals.
3. Identify content hooks, community tone, and collaboration opportunities.
4. Return risks and next actions.

Rules:

- Use only registered tools.
- Do not invent danmaku or comment content.
- Mark unavailable fields clearly.
