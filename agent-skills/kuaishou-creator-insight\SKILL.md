---
name: kuaishou-creator-insight
title: Kuaishou Creator Insight
platform: kuaishou
version: 1.0.0
tools:
  - kuaishou.profile.lookup
  - kuaishou.content.search
  - kuaishou.comment.summary
---

# Kuaishou Creator Insight

Analyze Kuaishou creators, videos, content style, and audience signals.

Inputs:

- `target`: creator, video URL, keyword, or topic
- `objective`: analysis goal
- `language`: output language

Process:

1. Fetch available creator and content signals.
2. Summarize format, frequency, engagement, and comment themes.
3. Identify fit for collaboration, sales prospecting, or content adaptation.
4. Return recommendations and risks.

Rules:

- Use registered SDCenter tools only.
- Do not infer private identity or demographics.
- State missing evidence.
