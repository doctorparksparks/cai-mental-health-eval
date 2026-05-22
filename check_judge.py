import pandas as pd

df = pd.read_csv("day5_llm_judge.csv", encoding="utf-8-sig")

print("=== LLM Judge 원본 응답 (첫 3개) ===")
for i in range(3):
    print(f"\n--- {i+1}번 Claude 응답 ---")
    print(repr(df["llm_judge_claude"][i]))
    print(f"\n--- {i+1}번 GPT 응답 ---")
    print(repr(df["llm_judge_gpt"][i]))