import pandas as pd
import json

df = pd.read_csv("day5_llm_judge.csv", encoding="utf-8-sig")

llm_sr_claude, llm_emp_claude, llm_sl_claude = [], [], []
llm_sr_gpt, llm_emp_gpt, llm_sl_gpt = [], [], []

for _, row in df.iterrows():
    try:
        raw = row["llm_judge_claude"].replace("```json", "").replace("```", "").strip()
        c = json.loads(raw)
        llm_sr_claude.append(c["safety_referral"])
        llm_emp_claude.append(c["empathy_score"])
        llm_sl_claude.append(c["scope_limit"])
    except:
        llm_sr_claude.append(None)
        llm_emp_claude.append(None)
        llm_sl_claude.append(None)

    try:
        raw = row["llm_judge_gpt"].replace("```json", "").replace("```", "").strip()
        g = json.loads(raw)
        llm_sr_gpt.append(g["safety_referral"])
        llm_emp_gpt.append(g["empathy_score"])
        llm_sl_gpt.append(g["scope_limit"])
    except:
        llm_sr_gpt.append(None)
        llm_emp_gpt.append(None)
        llm_sl_gpt.append(None)

df["llm_sr_claude"] = llm_sr_claude
df["llm_emp_claude"] = llm_emp_claude
df["llm_sl_claude"] = llm_sl_claude
df["llm_sr_gpt"] = llm_sr_gpt
df["llm_emp_gpt"] = llm_emp_gpt
df["llm_sl_gpt"] = llm_sl_gpt

print("=== Safety Referral 일치율 ===")
print(f"Claude 응답: {(df['llm_sr_claude'] == df['human_sr_claude']).mean():.0%}")
print(f"GPT 응답:    {(df['llm_sr_gpt'] == df['human_sr_gpt']).mean():.0%}")

print("\n=== Empathy Score 평균 차이 ===")
print(f"Claude 응답: {(df['llm_emp_claude'] - df['human_emp_claude']).abs().mean():.2f}점")
print(f"GPT 응답:    {(df['llm_emp_gpt'] - df['human_emp_gpt']).abs().mean():.2f}점")

print("\n=== Scope Limit 일치율 ===")
print(f"Claude 응답: {(df['llm_sl_claude'] == df['human_sl_claude']).mean():.0%}")
print(f"GPT 응답:    {(df['llm_sl_gpt'] == df['human_sl_gpt']).mean():.0%}")

print("\n=== 전체 비교표 (Claude 응답) ===")
print(f"{'ID':<5} {'SR 사람':>8} {'SR LLM':>8} {'EMP 사람':>9} {'EMP LLM':>9} {'SL 사람':>8} {'SL LLM':>8}")
print("-" * 60)
for _, row in df.iterrows():
    print(f"{int(row['id']):<5} {int(row['human_sr_claude']):>8} {str(row['llm_sr_claude']):>8} {int(row['human_emp_claude']):>9} {str(row['llm_emp_claude']):>9} {int(row['human_sl_claude']):>8} {str(row['llm_sl_claude']):>8}")