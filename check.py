import pandas as pd

df = pd.read_csv("day2_responses.csv")
print(df["claude_response"][0])
print("---")
print(df["gpt_response"][0])