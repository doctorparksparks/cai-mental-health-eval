import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("day2_responses.csv", encoding="cp949")

os.makedirs("charts", exist_ok=True)

# 차트 1: Safety Referral 비율
fig, ax = plt.subplots(figsize=(6, 4))
models = ["Claude", "GPT"]
safety_values = [
    df["safety_referral_claude"].mean() * 100,
    df["safety_referral_gpt"].mean() * 100
]
bars = ax.bar(models, safety_values, color=["#4A90D9", "#E87040"], width=0.4)
ax.set_title("Safety Referral Rate by Model", fontsize=13)
ax.set_ylabel("Referral Rate (%)")
ax.set_ylim(0, 100)
for bar, val in zip(bars, safety_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f"{val:.0f}%", ha="center", fontsize=11)
plt.tight_layout()
plt.savefig("charts/safety_referral.png", dpi=150)
plt.close()
print("차트 1 저장 완료")

# 차트 2: Empathy Score 평균
fig, ax = plt.subplots(figsize=(6, 4))
empathy_values = [
    df["empathy_score_claude"].mean(),
    df["empathy_score_gpt"].mean()
]
bars = ax.bar(models, empathy_values, color=["#4A90D9", "#E87040"], width=0.4)
ax.set_title("Average Empathy Score by Model", fontsize=13)
ax.set_ylabel("Empathy Score (1-5)")
ax.set_ylim(0, 5)
for bar, val in zip(bars, empathy_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f"{val:.2f}", ha="center", fontsize=11)
plt.tight_layout()
plt.savefig("charts/empathy_score.png", dpi=150)
plt.close()
print("차트 2 저장 완료")

# 차트 3: Scope Limitation 준수율
fig, ax = plt.subplots(figsize=(6, 4))
scope_values = [
    df["scope_limit_claude"].mean() * 100,
    df["scope_limit_gpt"].mean() * 100
]
bars = ax.bar(models, scope_values, color=["#4A90D9", "#E87040"], width=0.4)
ax.set_title("Scope Limitation Compliance by Model", fontsize=13)
ax.set_ylabel("Compliance Rate (%)")
ax.set_ylim(0, 100)
for bar, val in zip(bars, scope_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f"{val:.0f}%", ha="center", fontsize=11)
plt.tight_layout()
plt.savefig("charts/scope_limit.png", dpi=150)
plt.close()
print("차트 3 저장 완료")