---
name: bilibili-comment-sentiment
title: Bilibili Comment Sentiment
platform: bilibili
version: 1.0.0
tools:
  - bilibili.content.search
  - bilibili.comment.summary
---

# Bilibili Comment Sentiment

Analyze Bilibili comment sentiment and audience reaction for videos, creators, or topics.

Inputs:

- `target`: video URL, creator, keyword, or topic
- `objective`: sentiment analysis goal
- `language`: output language

Process:

1. Retrieve available content and comment signals.
2. Cluster sentiment, repeated questions, objections, and jokes or memes.
3. Identify risks, audience fit, and content improvement opportunities.
4. Return a sentiment brief.

Rules:

- Do not fabricate comment content.
- Do not infer private user attributes.
- Mark incomplete evidence.
