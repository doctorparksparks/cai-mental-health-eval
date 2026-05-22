import anthropic
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r"C:\Users\user\Desktop\2026\Coding_260517~\.env")

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "I've been feeling really low lately."}]
)

print(response.content[0].text)