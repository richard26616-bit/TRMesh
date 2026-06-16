---
name: social-campaign-planner
title: Social Campaign Planner
platform: cross-platform
version: 1.0.0
tools:
  - social.profile.lookup
  - social.content.search
  - social.comment.sentiment
---

# Social Campaign Planner

Plan cross-platform social data research and campaign actions across SDCenter-supported platforms.

Inputs:

- `target`: brand, product, competitor, creator, keyword, or campaign idea
- `objective`: campaign or research goal
- `platforms`: preferred platforms
- `language`: output language

Process:

1. Clarify the platform scope and target.
2. Query only registered SDCenter tools for supported platforms.
3. Compare audience signals, content angles, risks, and opportunity fit.
4. Return a campaign plan with platform-specific next actions.

Rules:

- Do not call unsupported tools.
- Do not fabricate cross-platform comparisons.
- Make data gaps and assumptions explicit.
