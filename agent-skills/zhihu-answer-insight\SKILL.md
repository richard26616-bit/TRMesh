---
name: zhihu-answer-insight
title: Zhihu Answer Insight
platform: zhihu
version: 1.0.0
tools:
  - zhihu.content.search
  - zhihu.comment.summary
---

# Zhihu Answer Insight

Analyze Zhihu answers for argument quality, audience concerns, and market insight.

Inputs:

- `target`: question URL, answer URL, keyword, or topic
- `objective`: answer analysis goal
- `language`: output language

Process:

1. Retrieve available question, answer, and discussion signals.
2. Summarize core arguments, objections, expertise cues, and sentiment.
3. Identify content opportunities, customer pain points, and knowledge gaps.
4. Return answer insight notes and next actions.

Rules:

- Do not overstate author authority.
- Do not infer private user traits.
- Mark unsupported claims.
