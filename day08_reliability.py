import pandas as pd
from sklearn.metrics import cohen_kappa_score
import os

os.chdir(r"C:\Users\user\Desktop\2026\Coding_260517~")

df = pd.read_csv("day08_llm_judge.csv", encoding="utf-8-sig")

print("=== Cohen's Kappa: Human vs LLM Judge ===\n")

# Claude 응답 채점 일치율
kappa_sr_c  = cohen_kappa_score(df["human_sr_claude"],  df["llm_sr_claude"])
kappa_sl_c  = cohen_kappa_score(df["human_sl_claude"],  df["llm_sl_claude"])

# GPT 응답 채점 일치율
kappa_sr_g  = cohen_kappa_score(df["human_sr_gpt"],     df["llm_sr_gpt"])
kappa_sl_g  = cohen_kappa_score(df["human_sl_gpt"],     df["llm_sl_gpt"])

# Empathy는 연속형 → weighted kappa
kappa_emp_c = cohen_kappa_score(df["human_emp_claude"], df["llm_emp_claude"], weights="linear")
kappa_emp_g = cohen_kappa_score(df["human_emp_gpt"],    df["llm_emp_gpt"],    weights="linear")

print(f"[Claude 응답]")
print(f"  Safety Referral  kappa: {kappa_sr_c:.3f}")
print(f"  Empathy Score    kappa: {kappa_emp_c:.3f}  (weighted)")
print(f"  Scope Limit      kappa: {kappa_sl_c:.3f}")

print(f"\n[GPT 응답]")
print(f"  Safety Referral  kappa: {kappa_sr_g:.3f}")
print(f"  Empathy Score    kappa: {kappa_emp_g:.3f}  (weighted)")
print(f"  Scope Limit      kappa: {kappa_sl_g:.3f}")

print("\n=== Kappa 해석 기준 ===")
print("  0.81-1.00 : 거의 완벽한 일치")
print("  0.61-0.80 : 상당한 일치")
print("  0.41-0.60 : 중간 일치")
print("  0.21-0.40 : 낮은 일치")
print("  0.00-0.20 : 매우 낮은 일치")

print("\n=== 단순 일치율 (%) ===")
for col_h, col_l, label in [
    ("human_sr_claude", "llm_sr_claude",  "Safety / Claude"),
    ("human_sr_gpt",    "llm_sr_gpt",     "Safety / GPT"),
    ("human_emp_claude","llm_emp_claude",  "Empathy / Claude"),
    ("human_emp_gpt",   "llm_emp_gpt",    "Empathy / GPT"),
    ("human_sl_claude", "llm_sl_claude",  "Scope / Claude"),
    ("human_sl_gpt",    "llm_sl_gpt",     "Scope / GPT"),
]:
    acc = (df[col_h] == df[col_l]).mean() * 100
    print(f"  {label:20s}: {acc:.0f}%")