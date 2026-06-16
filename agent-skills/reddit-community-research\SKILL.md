---
name: reddit-community-research
title: Reddit Community Research
platform: reddit
version: 1.0.0
tools:
  - reddit.profile.lookup
  - reddit.content.search
  - reddit.comment.summary
---

# Reddit Community Research

Research Reddit communities, posts, comments, and user pain points for product, sales, and market teams.

Inputs:

- `target`: subreddit, post URL, keyword, or topic
- `objective`: research goal
- `language`: output language

Process:

1. Identify relevant subreddit or topic data.
2. Summarize repeated problems, objections, language patterns, and sentiment.
3. Extract opportunity signals and risks.
4. Return actionable research notes and follow-up questions.

Rules:

- Do not deanonymize users.
- Avoid unsupported demographic claims.
- Separate direct evidence from inference.
