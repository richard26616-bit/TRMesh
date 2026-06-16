---
name: zhihu-question-research
title: Zhihu Question Research
platform: zhihu
version: 1.0.0
tools:
  - zhihu.profile.lookup
  - zhihu.content.search
  - zhihu.comment.summary
---

# Zhihu Question Research

Research Zhihu questions, answers, authors, and discussion signals for market and content strategy.

Inputs:

- `target`: question URL, author, keyword, or topic
- `objective`: research goal
- `language`: output language

Process:

1. Retrieve available question, answer, and author signals.
2. Summarize recurring arguments, objections, expertise signals, and sentiment.
3. Identify content angles, customer pains, and knowledge gaps.
4. Return research notes and suggested follow-up queries.

Rules:

- Do not overstate author authority without evidence.
- Avoid private user inference.
- Explain missing or incomplete data.
