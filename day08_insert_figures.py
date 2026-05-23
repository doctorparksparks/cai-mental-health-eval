import os

os.chdir(r"C:\Users\user\Desktop\2026\Coding_260517~")

with open("day08_research_memo.md", "r", encoding="utf-8") as f:
    content = f.read()

insertions = {
    "Claude outperformed GPT-4o-mini across all three dimensions. Notably, GPT-4o-mini\nacknowledged its AI limitations in zero of 40 responses, consistently responding as\nthough it were a human therapist.":
    "Claude outperformed GPT-4o-mini across all three dimensions. Notably, GPT-4o-mini\nacknowledged its AI limitations in zero of 40 responses, consistently responding as\nthough it were a human therapist.\n\n![Figure 1](charts/day08_safety_by_language.png)\n*Figure 1. Safety Referral Rate by Language (Claude vs GPT-4o-mini)*",

    "Claude showed a 15 percentage point reduction in safety referral rates for Korean\ninputs compared to English. GPT-4o-mini showed no difference, maintaining a uniformly\nlow rate across both languages.":
    "Claude showed a 15 percentage point reduction in safety referral rates for Korean\ninputs compared to English. GPT-4o-mini showed no difference, maintaining a uniformly\nlow rate across both languages.\n\n![Figure 2](charts/day08_empathy_by_language.png)\n*Figure 2. Empathy Score by Language (Claude vs GPT-4o-mini)*",

    "Claude demonstrated risk-sensitive escalation — safety referral rates increased\nproportionally with risk level, consistent with clinically appropriate behavior.\nGPT-4o-mini failed to escalate adequately at high-risk level (25%).":
    "Claude demonstrated risk-sensitive escalation — safety referral rates increased\nproportionally with risk level, consistent with clinically appropriate behavior.\nGPT-4o-mini failed to escalate adequately at high-risk level (25%).\n\n![Figure 3](charts/day08_safety_by_risk.png)\n*Figure 3. Safety Referral Rate by Risk Level*",

    "*GPT Scope Limit kappa = 0.000 reflects zero variance: both human and LLM judge\nagreed GPT never acknowledged limitations, resulting in undefined kappa.":
    "*GPT Scope Limit kappa = 0.000 reflects zero variance: both human and LLM judge\nagreed GPT never acknowledged limitations, resulting in undefined kappa.\n\n![Figure 4](charts/day08_empathy_by_concept.png)\n*Figure 4. Empathy Score by Clinical Concept*",
}

for old, new in insertions.items():
    if old in content:
        content = content.replace(old, new)
        print(f"✓ 삽입 완료")
    else:
        print(f"⚠️ 텍스트 못 찾음 — 수동 확인 필요")

with open("day08_research_memo.md", "w", encoding="utf-8") as f:
    f.write(content)

print("\n완료! day08_research_memo.md 업데이트됨")