---
name: weibo-account-monitor
title: Weibo Account Monitor
platform: weibo
version: 1.0.0
tools:
  - weibo.profile.lookup
  - weibo.content.search
  - weibo.comment.summary
---

# Weibo Account Monitor

Monitor Weibo accounts for brand, public opinion, creator, or competitor tracking.

Inputs:

- `target`: account, profile URL, keyword, or campaign
- `objective`: monitoring goal
- `language`: output language

Process:

1. Resolve the account and available public content.
2. Summarize posting themes, audience reaction, and risk signals.
3. Identify trend direction, stakeholder signals, and follow-up topics.
4. Return an account monitoring brief.

Rules:

- Do not fabricate trend or engagement data.
- Separate evidence from inference.
- Keep outputs suitable for operational review.
