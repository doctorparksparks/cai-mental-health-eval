import anthropic
import pandas as pd
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path=r"C:\Users\user\Desktop\2026\Coding_260517~\.env")

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

df_prompts = pd.read_csv("prompts.csv")

results = []
for _, row in df_prompts.iterrows():
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        messages=[{"role": "user", "content": row["prompt"]}]
    )
    results.append({
        "id": row["id"],
        "explicitness": row["explicitness"],
        "culture": row["culture"],
        "prompt": row["prompt"],
        "model": "claude-haiku-4-5",
        "response": response.content[0].text
    })
    print(f"완료: {row['id']}/20")
    time.sleep(0.5)

df = pd.DataFrame(results)
df.to_csv("responses.csv", index=False, encoding="utf-8-sig")
print("저장 완료!")