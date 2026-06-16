---
name: kuaishou-live-commerce-brief
title: Kuaishou Live Commerce Brief
platform: kuaishou
version: 1.0.0
tools:
  - kuaishou.profile.lookup
  - kuaishou.content.search
  - kuaishou.comment.summary
---

# Kuaishou Live Commerce Brief

Analyze Kuaishou live commerce signals for products, creators, and merchant discovery.

Inputs:

- `target`: account, product keyword, video URL, or topic
- `objective`: commerce analysis goal
- `language`: output language

Process:

1. Gather available creator, product, content, and comment signals.
2. Summarize product fit, selling angles, trust cues, and objections.
3. Identify opportunity segments and risk points.
4. Return a live commerce brief.

Rules:

- Do not fabricate GMV or order volume.
- Mark unavailable commerce metrics.
- Keep advice tied to observed signals.
