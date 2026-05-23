import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 경로 설정
BASE = r"C:\Users\user\Desktop\2026\Coding_260517~"
os.chdir(BASE)

# 한글 폰트
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("day08_responses_2models.csv", encoding="utf-8-sig")

# ── 1. 언어별 Safety Referral ──────────────────────────
lang = df.groupby("language")[["safety_referral_claude","safety_referral_gpt"]].mean() * 100

fig, ax = plt.subplots(figsize=(7,4))
x = range(len(lang))
ax.bar([i-0.2 for i in x], lang["safety_referral_claude"], 0.4, label="Claude", color="#4A6FA5")
ax.bar([i+0.2 for i in x], lang["safety_referral_gpt"],    0.4, label="GPT",    color="#E07B54")
ax.set_xticks(list(x))
ax.set_xticklabels(lang.index, fontsize=12)
ax.set_ylabel("Safety Referral Rate (%)")
ax.set_title("언어별 Safety Referral Rate", fontproperties=font_prop)
ax.legend()
ax.set_ylim(0, 80)
for i, (c, g) in enumerate(zip(lang["safety_referral_claude"], lang["safety_referral_gpt"])):
    ax.text(i-0.2, c+1.5, f"{c:.0f}%", ha="center", fontsize=9)
    ax.text(i+0.2, g+1.5, f"{g:.0f}%", ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("charts/day08_safety_by_language.png", dpi=150)
plt.close()
print("✓ chart 1 저장")

# ── 2. 언어별 Empathy Score ───────────────────────────
emp = df.groupby("language")[["empathy_score_claude","empathy_score_gpt"]].mean()

fig, ax = plt.subplots(figsize=(7,4))
x = range(len(emp))
ax.bar([i-0.2 for i in x], emp["empathy_score_claude"], 0.4, label="Claude", color="#4A6FA5")
ax.bar([i+0.2 for i in x], emp["empathy_score_gpt"],    0.4, label="GPT",    color="#E07B54")
ax.set_xticks(list(x))
ax.set_xticklabels(emp.index, fontsize=12)
ax.set_ylabel("Empathy Score (1-5)")
ax.set_title("언어별 Empathy Score 평균", fontproperties=font_prop)
ax.legend()
ax.set_ylim(0, 5)
for i, (c, g) in enumerate(zip(emp["empathy_score_claude"], emp["empathy_score_gpt"])):
    ax.text(i-0.2, c+0.05, f"{c:.2f}", ha="center", fontsize=9)
    ax.text(i+0.2, g+0.05, f"{g:.2f}", ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("charts/day08_empathy_by_language.png", dpi=150)
plt.close()
print("✓ chart 2 저장")

# ── 3. Risk Level별 Safety Referral ───────────────────
risk = df.groupby("risk_level")[["safety_referral_claude","safety_referral_gpt"]].mean() * 100
risk = risk.reindex(["low","medium","high"])

fig, ax = plt.subplots(figsize=(7,4))
x = range(len(risk))
ax.bar([i-0.2 for i in x], risk["safety_referral_claude"], 0.4, label="Claude", color="#4A6FA5")
ax.bar([i+0.2 for i in x], risk["safety_referral_gpt"],    0.4, label="GPT",    color="#E07B54")
ax.set_xticks(list(x))
ax.set_xticklabels(["Low","Medium","High"], fontsize=12)
ax.set_ylabel("Safety Referral Rate (%)")
ax.set_title("Risk Level별 Safety Referral Rate", fontproperties=font_prop)
ax.legend()
ax.set_ylim(0, 100)
for i, (c, g) in enumerate(zip(risk["safety_referral_claude"], risk["safety_referral_gpt"])):
    ax.text(i-0.2, c+1.5, f"{c:.0f}%", ha="center", fontsize=9)
    ax.text(i+0.2, g+1.5, f"{g:.0f}%", ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("charts/day08_safety_by_risk.png", dpi=150)
plt.close()
print("✓ chart 3 저장")

# ── 4. Concept별 Empathy (상위 개념만) ────────────────
concept_emp = df.groupby("concept")[["empathy_score_claude","empathy_score_gpt"]].mean()
concept_emp = concept_emp.sort_values("empathy_score_claude", ascending=True)

fig, ax = plt.subplots(figsize=(9,6))
y = range(len(concept_emp))
ax.barh([i+0.2 for i in y], concept_emp["empathy_score_claude"], 0.4, label="Claude", color="#4A6FA5")
ax.barh([i-0.2 for i in y], concept_emp["empathy_score_gpt"],    0.4, label="GPT",    color="#E07B54")
ax.set_yticks(list(y))
ax.set_yticklabels(concept_emp.index, fontsize=9)
ax.set_xlabel("Empathy Score (1-5)")
ax.set_title("개념별 Empathy Score", fontproperties=font_prop)
ax.legend()
ax.set_xlim(0, 5)
plt.tight_layout()
plt.savefig("charts/day08_empathy_by_concept.png", dpi=150)
plt.close()
print("✓ chart 4 저장")

# ── 5. 요약 통계 출력 ─────────────────────────────────
print("\n=== 언어별 분석 ===")
print(lang.round(1))
print("\n=== Risk Level별 Safety ===")
print(risk.round(1))
print("\n=== 핵심 수치 ===")
high_risk = df[df["risk_level"] == "high"]
print(f"고위험(high) 프롬프트 수: {len(high_risk)}")
print(f"고위험 Safety Claude: {high_risk['safety_referral_claude'].mean()*100:.0f}%")
print(f"고위험 Safety GPT:    {high_risk['safety_referral_gpt'].mean()*100:.0f}%")
korean_high = df[(df["language"]=="korean") & (df["risk_level"]=="high")]
print(f"\n한국어 고위험 Safety Claude: {korean_high['safety_referral_claude'].mean()*100:.0f}%")
print(f"한국어 고위험 Safety GPT:    {korean_high['safety_referral_gpt'].mean()*100:.0f}%")