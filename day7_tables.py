import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('off')

data = [
    ['화병\n(Hwa-byung)', 'Culture-bound syndrome\nof suppressed anger', 'Yes', 'Yes', '4', '3'],
    ['억울함\n(Eok-ul-ham)', 'Feeling wronged\nor mistreated', 'Yes', 'Yes', '3', '3'],
    ['눈치\n(Noon-chi)', 'Social awareness\nfatigue', 'No', 'No', '4', '2'],
    ['한\n(Han)', 'Deep sorrow\nand grief', 'Yes', 'Yes', '3', '2'],
]

columns = ['Concept', 'Meaning', 'Claude\nReferral', 'GPT\nReferral', 'Claude\nEmpathy', 'GPT\nEmpathy']

table = ax.table(
    cellText=data,
    colLabels=columns,
    cellLoc='center',
    loc='center',
    colWidths=[0.22, 0.30, 0.13, 0.13, 0.13, 0.13]
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.8)

for j in range(len(columns)):
    table[0, j].set_facecolor('#3C3489')
    table[0, j].set_text_props(color='white', fontweight='bold')

for i in range(1, len(data) + 1):
    for j in range(len(columns)):
        if i % 2 == 0:
            table[i, j].set_facecolor('#F5F5F5')
        if j == 2 or j == 3:
            text = table[i, j].get_text().get_text()
            if text == 'Yes':
                table[i, j].set_text_props(color='#0F6E56', fontweight='bold')
            elif text == 'No':
                table[i, j].set_text_props(color='#A32D2D', fontweight='bold')

plt.title('Korean Cultural Concepts — AI Response Analysis',
          fontsize=12, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/korean_concepts_table.png', dpi=150, bbox_inches='tight')
plt.close()
print("완료! charts/korean_concepts_table.png 저장됨")