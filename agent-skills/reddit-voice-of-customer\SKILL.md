---
name: reddit-voice-of-customer
title: Reddit Voice of Customer
platform: reddit
version: 1.0.0
tools:
  - reddit.content.search
  - reddit.comment.summary
---

# Reddit Voice of Customer

Extract voice-of-customer signals from Reddit conversations for product, marketing, and sales teams.

Inputs:

- `target`: product, category, competitor, problem, or subreddit
- `objective`: customer research goal
- `language`: output language

Process:

1. Search related posts and comments through registered tools.
2. Cluster pains, desired outcomes, buying objections, and language patterns.
3. Identify messaging opportunities and product gaps.
4. Return customer-language notes and next actions.

Rules:

- Do not represent anecdotes as statistically representative.
- Preserve uncertainty.
- Avoid private user inference.
