---
name: reddit-subreddit-monitor
title: Reddit Subreddit Monitor
platform: reddit
version: 1.0.0
tools:
  - reddit.content.search
  - reddit.comment.summary
---

# Reddit Subreddit Monitor

Monitor a subreddit or Reddit topic for community themes, questions, and risk signals.

Inputs:

- `target`: subreddit, keyword, topic, or post URL
- `objective`: monitoring goal
- `language`: output language

Process:

1. Retrieve available posts and comments through registered tools.
2. Group recurring themes, problems, objections, and vocabulary.
3. Identify community norms, opportunity signals, and risks.
4. Return a monitoring brief and follow-up searches.

Rules:

- Do not deanonymize users.
- Do not infer personal traits.
- Mark sparse or unavailable data.
