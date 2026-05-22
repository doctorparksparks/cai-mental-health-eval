import pandas as pd

df = pd.read_csv("day2_responses.csv", encoding="cp949")

# 영어/한국어 짝 정의
pairs = [
    {"en_id": 3,  "ko_id": 12, "theme": "General distress"},
    {"en_id": 1,  "ko_id": 19, "theme": "Low mood / no motivation"},
    {"en_id": 6,  "ko_id": 15, "theme": "Isolation"},
    {"en_id": 7,  "ko_id": 16, "theme": "AI dependency"},
    {"en_id": 9,  "ko_id": 17, "theme": "Avoiding professional help"},
]

# 한국어 고유 개념
korean_only = [11, 13, 14, 18, 20]

print("=== 짝 비교: 영어 vs 한국어 (같은 주제) ===\n")

for pair in pairs:
    en = df[df["id"] == pair["en_id"]].iloc[0]
    ko = df[df["id"] == pair["ko_id"]].iloc[0]

    print(f"[{pair['theme']}]")
    print(f"  영어 프롬프트: {en['prompt']}")
    print(f"  한국어 프롬프트: {ko['prompt']}")
    print(f"  Safety Referral  — Claude: EN={int(en['safety_referral_claude'])} / KO={int(ko['safety_referral_claude'])}  |  GPT: EN={int(en['safety_referral_gpt'])} / KO={int(ko['safety_referral_gpt'])}")
    print(f"  Empathy Score    — Claude: EN={int(en['empathy_score_claude'])} / KO={int(ko['empathy_score_claude'])}  |  GPT: EN={int(en['empathy_score_gpt'])} / KO={int(ko['empathy_score_gpt'])}")
    print(f"  Scope Limit      — Claude: EN={int(en['scope_limit_claude'])} / KO={int(ko['scope_limit_claude'])}  |  GPT: EN={int(en['scope_limit_gpt'])} / KO={int(ko['scope_limit_gpt'])}")
    print()

print("=== 한국어 고유 개념 (영어 짝 없음) ===\n")

ko_concepts = {
    11: "화병 (Hwa-byung)",
    13: "억울함 (Injustice/resentment)",
    14: "눈치 (Social awareness fatigue)",
    18: "한 (Han — deep sorrow)",
    20: "포기 (Giving up — suicide risk signal)",
}

for id_, concept in ko_concepts.items():
    row = df[df["id"] == id_].iloc[0]
    print(f"[{concept}]")
    print(f"  프롬프트: {row['prompt']}")
    print(f"  Safety Referral — Claude: {int(row['safety_referral_claude'])} / GPT: {int(row['safety_referral_gpt'])}")
    print(f"  Empathy Score   — Claude: {int(row['empathy_score_claude'])} / GPT: {int(row['empathy_score_gpt'])}")
    print(f"  Scope Limit     — Claude: {int(row['scope_limit_claude'])} / GPT: {int(row['scope_limit_gpt'])}")
    print()