from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import os
import time

load_dotenv()

clinent = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

f_prompts = pd.read_csv("prompts.csv")

results = []
for _, row in f_prompts.iterrows():
    response = clinent.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=256,
        messages=[{"role": "user", "content": row["prompt"]}]
    )
    results.append({
        "id": row["id"],
        "explicitness": row["explicitness"],
        "culture": row["culture"],
        "register": row["register"],
        "prompt": row["prompt"],
        "response": response.choices[0].message.content
    })
    print(f"완료: row {row['id']}/20")
    time.sleep(0.5)

df = pd.DataFrame(results)
df.to_csv("openai_results.csv", index=False, encoding="utf-8-sig")
print("저장 완료: openai_results.csv")