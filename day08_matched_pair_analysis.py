"""
day08_matched_pair_analysis.py

Purpose:
    Isolate the pure language effect by directly comparing matched prompt pairs —
    identical clinical concepts expressed in Korean (KK series) vs English (EM series).

Rationale:
    KK01-KK10 and EM01-EM10 are semantically equivalent prompts in different languages.
    Any performance difference between the two groups can be attributed to language
    rather than clinical content, since the underlying concept is held constant.

    delta = Korean score - English score
    delta < 0 : model performs worse on Korean input (language disadvantage)
    delta > 0 : model performs better on Korean input

Outputs:
    - day08_matched_pairs.csv
    - charts/day08_matched_pair_empathy_delta.png
    - charts/day08_matched_pair_safety.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ── Setup ────────────────────────────────────────────────
BASE = r"C:\Users\user\Desktop\2026\Coding_260517~"
os.chdir(BASE)

font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("day08_responses_2models.csv", encoding="utf-8-sig")

# ── Matched Pair Definitions ─────────────────────────────
# Each tuple: (Korean prompt id, English matched id, concept label)
# Korean cultural concepts labeled with both Korean and English:
#   화병(Hwabyung), 한(Han), 눈치(Nunchi), 정(Jeong), 체면(Chemyeon)
pairs = [
    ("KK01", "EM01", "화병(Hwabyung) / suppressed anger"),
    ("KK02", "EM02", "general distress"),
    ("KK03", "EM03", "한(Han) / injustice"),
    ("KK04", "EM04", "눈치(Nunchi) / reading the room"),
    ("KK05", "EM05", "suppression"),
    ("KK06", "EM06", "dependency: no therapist"),
    ("KK07", "EM07", "dependency: AI preferred"),
    ("KK08", "EM08", "한(Han) / unresolved grief"),
    ("KK09", "EM09", "anhedonia"),
    ("KK10", "EM10", "suicidal ideation"),
]

# ── Compute Deltas ───────────────────────────────────────
results = []
for kor_id, eng_id, concept in pairs:
    kor = df[df["id"] == kor_id].iloc[0]
    eng = df[df["id"] == eng_id].iloc[0]

    results.append({
        "concept":        concept,
        "korean_id":      kor_id,
        "english_id":     eng_id,

        # Claude scores
        "sr_claude_kor":  kor["safety_referral_claude"],
        "sr_claude_eng":  eng["safety_referral_claude"],
        "emp_claude_kor": kor["empathy_score_claude"],
        "emp_claude_eng": eng["empathy_score_claude"],
        "sl_claude_kor":  kor["scope_limit_claude"],
        "sl_claude_eng":  eng["scope_limit_claude"],

        # GPT scores
        "sr_gpt_kor":     kor["safety_referral_gpt"],
        "sr_gpt_eng":     eng["safety_referral_gpt"],
        "emp_gpt_kor":    kor["empathy_score_gpt"],
        "emp_gpt_eng":    eng["empathy_score_gpt"],
        "sl_gpt_kor":     kor["scope_limit_gpt"],
        "sl_gpt_eng":     eng["scope_limit_gpt"],

        # Deltas (Korean - English)
        "delta_sr_claude":  kor["safety_referral_claude"] - eng["safety_referral_claude"],
        "delta_emp_claude": kor["empathy_score_claude"]   - eng["empathy_score_claude"],
        "delta_sr_gpt":     kor["safety_referral_gpt"]    - eng["safety_referral_gpt"],
        "delta_emp_gpt":    kor["empathy_score_gpt"]      - eng["empathy_score_gpt"],
    })

df_pairs = pd.DataFrame(results)
df_pairs.to_csv("day08_matched_pairs.csv", index=False, encoding="utf-8-sig")
print("Saved: day08_matched_pairs.csv")

# ── Chart 1: Empathy Delta by Concept ───────────────────
# Red/orange = Korean disadvantage (delta < 0)
# Green/blue  = Korean advantage   (delta > 0)
fig, ax = plt.subplots(figsize=(10, 5))
y = range(len(df_pairs))

colors_claude = ["#C0392B" if d < 0 else "#2ECC71" for d in df_pairs["delta_emp_claude"]]
colors_gpt    = ["#E07B54" if d < 0 else "#4A6FA5" for d in df_pairs["delta_emp_gpt"]]

ax.barh([i+0.2 for i in y], df_pairs["delta_emp_claude"], 0.35,
        color=colors_claude, label="Claude (red = Korean disadvantage)")
ax.barh([i-0.2 for i in y], df_pairs["delta_emp_gpt"], 0.35,
        color=colors_gpt,    label="GPT (orange = Korean disadvantage)")
ax.set_yticks(list(y))
ax.set_yticklabels(df_pairs["concept"], fontsize=9)
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_xlabel("Empathy Delta (Korean − English)")
ax.set_title("Language Effect on Empathy: Korean vs English Matched Pairs\n"
             "(negative = lower empathy for Korean input)")
ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig("charts/day08_matched_pair_empathy_delta.png", dpi=150)
plt.close()
print("Saved: charts/day08_matched_pair_empathy_delta.png")

# ── Chart 2: Safety Referral — Korean vs English ─────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
x = range(len(df_pairs))
width = 0.35

for ax, kor_col, eng_col, title in [
    (axes[0], "sr_claude_kor", "sr_claude_eng", "Claude"),
    (axes[1], "sr_gpt_kor",    "sr_gpt_eng",    "GPT-4o-mini"),
]:
    ax.bar([i-width/2 for i in x], df_pairs[kor_col], width,
           label="Korean", color="#4A6FA5")
    ax.bar([i+width/2 for i in x], df_pairs[eng_col], width,
           label="English", color="#E07B54")
    ax.set_xticks(list(x))
    ax.set_xticklabels(df_pairs["concept"], rotation=45, ha="right", fontsize=7)
    ax.set_ylabel("Safety Referral (0/1)")
    ax.set_title(f"{title}: Safety Referral — Korean vs English")
    ax.legend(fontsize=8)
    ax.set_ylim(0, 1.3)

plt.tight_layout()
plt.savefig("charts/day08_matched_pair_safety.png", dpi=150)
plt.close()
print("Saved: charts/day08_matched_pair_safety.png")

# ── Summary Statistics ───────────────────────────────────
print("\n=== Matched Pair Language Effect Summary ===")
print(f"\nMean Empathy Delta — Claude: {df_pairs['delta_emp_claude'].mean():.3f}")
print(f"Mean Empathy Delta — GPT:    {df_pairs['delta_emp_gpt'].mean():.3f}")
print(f"\nPairs with Korean disadvantage — Claude: "
      f"{(df_pairs['delta_emp_claude'] < 0).sum()}/10")
print(f"Pairs with Korean disadvantage — GPT:    "
      f"{(df_pairs['delta_emp_gpt'] < 0).sum()}/10")
print(f"\nMean Safety Delta — Claude: {df_pairs['delta_sr_claude'].mean():.3f}")
print(f"Mean Safety Delta — GPT:    {df_pairs['delta_sr_gpt'].mean():.3f}")

print("\n=== Top 3 Korean Disadvantage Pairs (Claude Empathy) ===")
worst_c = df_pairs.nsmallest(3, "delta_emp_claude")[
    ["concept", "delta_emp_claude", "delta_emp_gpt"]]
print(worst_c.to_string(index=False))

print("\n=== Top 3 Korean Disadvantage Pairs (GPT Empathy) ===")
worst_g = df_pairs.nsmallest(3, "delta_emp_gpt")[
    ["concept", "delta_emp_gpt", "delta_emp_claude"]]
print(worst_g.to_string(index=False))