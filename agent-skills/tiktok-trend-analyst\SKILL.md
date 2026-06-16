---
name: tiktok-trend-analyst
title: TikTok Trend Analyst
platform: tiktok
version: 1.0.0
tools:
  - tiktok.profile.lookup
  - tiktok.content.search
  - tiktok.comment.summary
---

# TikTok Trend Analyst

Use this skill to analyze TikTok accounts, videos, hashtags, and content trends through registered SDCenter tools.

Inputs:

- `target`: account, video URL, hashtag, or keyword
- `objective`: research goal
- `language`: output language

Process:

1. Identify the target type and select the registered TikTok tool.
2. Retrieve available profile, content, engagement, and comment signals.
3. Summarize growth signals, audience fit, content hooks, and risks.
4. Return recommendations for content, sales, research, or marketing teams.

Rules:

- Do not call external URLs directly.
- Do not invent metrics.
- If data is missing, mark it as unavailable.
