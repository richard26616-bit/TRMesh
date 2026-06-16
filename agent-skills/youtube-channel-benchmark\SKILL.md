---
name: youtube-channel-benchmark
title: YouTube Channel Benchmark
platform: youtube
version: 1.0.0
tools:
  - youtube.profile.lookup
  - youtube.content.search
  - youtube.comment.summary
---

# YouTube Channel Benchmark

Benchmark YouTube channels for competitor analysis, creator discovery, or content strategy.

Inputs:

- `target`: channel URL, handle, keyword, or competitor set
- `objective`: benchmark goal
- `language`: output language

Process:

1. Retrieve available channel and video signals.
2. Compare content pillars, packaging, posting cadence cues, and comment themes.
3. Identify strengths, gaps, and repeatable formats.
4. Return benchmark findings and next actions.

Rules:

- Do not fabricate view or subscriber numbers.
- State unavailable comparison data.
- Keep recommendations tied to fetched signals.
