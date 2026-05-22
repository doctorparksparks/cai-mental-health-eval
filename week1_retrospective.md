# Week 1 Retrospective — From Clinic to Code

**Period:** 2026-05-17 to 2026-05-22  
**Total hours:** ~35h  
**Author:** Seokyung Park

---

## What I built

A systematic behavioral evaluation pipeline comparing Claude and GPT-4o-mini
on mental health prompts across English and Korean contexts.

- 20 standardized prompts (explicit/implicit × western/korean × formal/colloquial)
- Two-model API pipeline (Anthropic + OpenAI)
- Manual scoring rubric with 3 clinical dimensions
- Paired English/Korean comparison analysis
- LLM-as-judge pilot with human agreement analysis
- 3 visualizations + structured research memo

---

## What I learned

**Technical:**
- Python functions, loops, pandas, matplotlib from scratch
- API calls, CSV handling, git workflow
- LLM-as-judge technique and its limitations

**Research:**
- How to design a systematic prompt evaluation
- Why rubric documentation matters for reproducibility
- The difference between "AI feels empathetic" and "AI is clinically safe"

**Unexpected:**
- LLM judges consistently overestimate empathy
- Korean expressions of distress trigger fewer safety referrals
- 눈치 is invisible to both models as a clinical signal

---

## What was hard

- Debugging encoding errors (cp949 vs utf-8-sig)
- Understanding why functions need return statements
- Git merge conflicts on first push

---

## Strongest finding

"Both models failed to screen for suicidal ideation when a Korean user
expressed wanting to give up on everything (포기하고 싶다).
This is not a minor gap — it is a critical clinical failure."

---

## Week 2 goals

1. Expand prompts to 40 (add more Korean cultural expressions)
2. Add inter-rater reliability calculation
3. Test one additional model (Gemini)
4. Write first full draft of research memo in academic style
5. Publish Medium post: "From Clinic to Code — Week 1 findings"

---

## One sentence summary

I went from not knowing what a terminal was to building a
clinician-led AI safety evaluation pipeline in 6 days.