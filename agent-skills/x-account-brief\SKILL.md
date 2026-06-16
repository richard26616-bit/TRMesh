---
name: x-account-brief
title: X Account Brief
platform: x
version: 1.0.0
tools:
  - x.profile.lookup
  - x.content.search
  - x.comment.summary
---

# X Account Brief

Create a concise X account brief for sales, analyst, investor, or communication workflows.

Inputs:

- `target`: X handle, profile URL, or account id
- `objective`: brief goal
- `language`: output language

Process:

1. Resolve the account through registered SDCenter tools.
2. Summarize profile, posting themes, engagement cues, and conversation context.
3. Identify influence signals, risks, and follow-up topics.
4. Return a structured account brief.

Rules:

- Do not infer private user attributes.
- Distinguish facts from interpretation.
- Do not invent posts or metrics.
