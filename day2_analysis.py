import pandas as pd

df = pd.read_csv("day2_responses.csv", encoding="cp949")

print("=== 1. Safety Referral 비율 (모델별) ===")
print(f"Claude: {df['safety_referral_claude'].mean():.0%}")
print(f"GPT:    {df['safety_referral_gpt'].mean():.0%}")

print("\n=== 2. Empathy Score 평균 (모델별) ===")
print(f"Claude: {df['empathy_score_claude'].mean():.2f} / 5")
print(f"GPT:    {df['empathy_score_gpt'].mean():.2f} / 5")

print("\n=== 3. Scope Limitation 준수율 (모델별) ===")
print(f"Claude: {df['scope_limit_claude'].mean():.0%}")
print(f"GPT:    {df['scope_limit_gpt'].mean():.0%}")

print("\n=== 4. Safety Referral 영어 vs 한국어 ===")
en = df[df['culture'] == 'western']
ko = df[df['culture'] == 'korean']
print(f"Claude 영어: {en['safety_referral_claude'].mean():.0%}")
print(f"Claude 한국어: {ko['safety_referral_claude'].mean():.0%}")
print(f"GPT 영어: {en['safety_referral_gpt'].mean():.0%}")
print(f"GPT 한국어: {ko['safety_referral_gpt'].mean():.0%}")

print("\n=== 5. Empathy explicit vs implicit ===")
ex = df[df['explicitness'] == 'explicit']
im = df[df['explicitness'] == 'implicit']
print(f"Claude explicit: {ex['empathy_score_claude'].mean():.2f}")
print(f"Claude implicit: {im['empathy_score_claude'].mean():.2f}")
print(f"GPT explicit: {ex['empathy_score_gpt'].mean():.2f}")
print(f"GPT implicit: {im['empathy_score_gpt'].mean():.2f}")