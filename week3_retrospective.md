# Week 3 Retrospective
**Date:** 2026-06-13
**Author:** Seokyung Park, KMD | MSc Public Health, LSHTM

---

## What was completed

| Day | Output | Description |
|-----|--------|-------------|
| Day 08 | matched_pair_analysis, explicitness_analysis | Language effect isolation |
| Day 09 | failure_cases.md, failure_extractor.py | Clinical failure case analysis |
| Day 10 | multiturn_pilot.py, multiturn_results.csv, multiturn_analysis.md | Multi-turn pilot |
| Day 11 | research_memo_v2.md | Full memo with all findings integrated |
| Day 12 | run_all.py, .env.example | Reproducibility package |
| Day 13 | index.html | GitHub Pages portfolio landing page |
| Day 14 | README.md (final) | Project wrap-up |

---

## Key findings that emerged this week

**From failure case analysis (Day 09):**
All high-risk failures occurred in Korean. GPT normalised passive suicidal
ideation in KM08 — not a passive omission but an active clinical error.
Help-seeking barriers (체면, 눈치, 빨리빨리) were missed by both models as
elevated risk signals.

**From multi-turn pilot (Day 10):**
Claude tracked risk accumulation in English but not consistently in Korean —
the language gap persists across conversation depth. GPT's responses followed
a surface template ("I'm sorry" → "I'm really sorry" → "I'm truly sorry")
without genuine escalation tracking. MT04 revealed an additional GPT failure:
it misidentified the AI itself as a human teacher when addressed as "선생님".

---

## What I learned about research design

The matched pair design (KK vs EM series) was the single most valuable
methodological decision. Without it, language effects and content effects
would have been confounded. The failure case analysis taught me that
aggregate statistics hide the most important clinical findings — the 0%
figure for GPT Korean high-risk only becomes meaningful when you read
what GPT actually said to "내가 없어지면 어떨까".

LLM-as-judge is useful for binary dimensions at scale but cannot replace
clinician judgment for empathy — κ = 0.18 confirmed this empirically,
not just theoretically.

---

## What I would do differently

1. Pre-register the scoring rubric before running the pipeline
2. Include a second human rater from the start
3. Design multi-turn scenarios before single-turn — they reveal more
4. Add a system prompt condition to test safety engineering effects

---

## What comes next

This project is going into my MSc dissertation at LSHTM, focusing on
conversational AI in mental health help-seeking pathways — particularly
around cultural-linguistic equity and evaluation methodology.

Both repositories are public and reproducible:
- github.com/doctorparksparks/cai-mental-health-eval
- github.com/doctorparksparks/mental-health-triage-chatbot