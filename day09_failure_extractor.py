"""
day09_failure_extractor.py

Purpose:
    Extract the most clinically dangerous failure cases from the dataset.
    A failure case is defined as: high risk prompt + safety referral = 0.
    
Rationale:
    Not all failures are equal. A model missing empathy on a low-risk prompt
    is a quality issue. A model missing safety referral on a high-risk prompt
    is a patient safety issue. This script isolates the latter.
"""

import pandas as pd

# Load responses with human scores
df = pd.read_csv('day08_responses_2models.csv', encoding='utf-8-sig')

print("=== Risk level distribution ===")
print(df['risk_level'].value_counts())

print("\n=== high risk cases where Claude failed safety referral ===")
claude_fail = df[(df['risk_level'] == 'high') & (df['safety_referral_claude'] == 0)]
print(claude_fail[['id', 'language', 'concept', 'prompt', 'claude_response']].to_string())

print("\n=== high risk cases where GPT failed safety referral ===")
gpt_fail = df[(df['risk_level'] == 'high') & (df['safety_referral_gpt'] == 0)]
print(gpt_fail[['id', 'language', 'concept', 'prompt', 'gpt_response']].to_string())

print("\n=== Summary ===")
print(f"Total high risk prompts: {len(df[df['risk_level'] == 'high'])}")
print(f"Claude safety failures on high risk: {len(claude_fail)}")
print(f"GPT safety failures on high risk: {len(gpt_fail)}")

print("\n=== MEDIUM risk: both models scope_limit = 0 (dependency prompts) ===")
dependency_fail = df[
    (df['risk_level'] == 'medium') & 
    (df['scope_limit_claude'] == 0) & 
    (df['scope_limit_gpt'] == 0)
]
print(dependency_fail[['id', 'language', 'concept', 'prompt']].to_string())

print("\n=== Any risk: GPT scope_limit = 0 (all cases) ===")
gpt_scope_fail = df[df['scope_limit_gpt'] == 0]
print(f"GPT scope limit = 0: {len(gpt_scope_fail)}/40")

print("\n=== Medium risk Korean implicit: Claude safety = 0 ===")
korean_implicit_fail = df[
    (df['risk_level'] == 'medium') &
    (df['language'] == 'korean') &
    (df['explicitness'] == 'implicit') &
    (df['safety_referral_claude'] == 0)
]
print(korean_implicit_fail[['id', 'concept', 'prompt']].to_string())