---
name: douyin-creator-profile
title: Douyin Creator Profile
platform: douyin
version: 1.0.0
tools:
  - douyin.profile.lookup
  - douyin.content.search
  - douyin.comment.summary
---

# Douyin Creator Profile

Create a Douyin creator profile for commercial fit, content research, and account comparison.

Inputs:

- `target`: creator handle, profile URL, or sec user id
- `objective`: profiling goal
- `language`: output language

Process:

1. Resolve the creator and available public content.
2. Summarize content themes, engagement signals, comments, and audience cues.
3. Identify brand fit, conversion signals, and operational risks.
4. Return verified findings and next actions.

Rules:

- Do not bypass SDCenter tool routing.
- Do not invent private account data.
- Label inference explicitly.
