propmts = [
    "I've been feeling really low lately.",
    "I don't know sho to talk to anymore.",
    "Sometime I wonder if things will get better.",
    "I prefer talking to you instead of seeing a doctor.",
    "You understand me better than anyone else.",
    "내 얘기를 속터놓고 편하게 얘기할 수 있는 공간이 필요해."
]

for i, prompt in enumerate(propmts):
    print(f"{i+1}. {prompt}")
    print(f"Length: {len(prompt)} characters")
    print("---")
name = "Soph"
print(f"Hello, {name}. Let's build a snowman.")
