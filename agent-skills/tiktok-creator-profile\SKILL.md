---
name: tiktok-creator-profile
title: TikTok Creator Profile
platform: tiktok
version: 1.0.0
tools:
  - tiktok.profile.lookup
  - tiktok.content.search
  - tiktok.comment.summary
---

# TikTok Creator Profile

Profile a TikTok creator for sales, creator partnership, competitor research, or content planning.

Inputs:

- `target`: creator handle, profile URL, or creator id
- `objective`: profiling goal
- `language`: output language

Process:

1. Resolve the creator through registered SDCenter TikTok tools.
2. Summarize profile positioning, content pillars, engagement signals, and audience cues.
3. Identify collaboration fit, brand safety risks, and comparable creator angles.
4. Return a concise creator profile with next actions.

Rules:

- Do not infer private demographics.
- Do not fabricate follower, engagement, or comment data.
- Separate observed evidence from recommendations.
