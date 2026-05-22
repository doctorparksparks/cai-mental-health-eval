import anthropic
import openai
import pandas as pd
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path=r"C:\Users\user\Desktop\2026\Coding_260517~\.env")

print("ANTHROPIC:", os.getenv("ANTHROPIC_API_KEY"))
print("OPENAI:", os.getenv("OPENAI_API_KEY"))

claude_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_claude(prompt):
    response = claude_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def call_gpt(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def run_pipeline(prompts_csv, output_csv):
    df_prompts = pd.read_csv(prompts_csv)
    results = []

    for _, row in df_prompts.iterrows():
        print(f"진행 중: {row['id']}/20")
              
        claude_response = call_claude(row["prompt"])
        time.sleep(0.5)

        gpt_response = call_gpt(row["prompt"])
        time.sleep(0.5)

        results.append({
            "id": row["id"],
            "explicitness": row["explicitness"],
            "culture": row["culture"],
            "prompt": row["prompt"],
            "claude_response": claude_response,
            "gpt_response": gpt_response,
            "safety_referral_claude": "",
            "safety_referral_gpt": "",
            "empathy_score_claude": "",
            "empathy_score_gpt": "",
        })

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"완료! {output_csv} 저장됨")

run_pipeline("prompts.csv", "day2_responses.csv")