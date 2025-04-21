import random

# ფაილების წაკითხვა
with open("students.txt", "r", encoding="utf-8") as f:
    students = [line.strip() for line in f.readlines() if line.strip()]

with open("exercises.txt", "r", encoding="utf-8") as f:
    exercises = [line.strip() for line in f.readlines() if line.strip()]

# თითოეული სტუდენტისთვის ბილეთის გენერაცია
for student in students:
    selected = random.sample(exercises, 4)  # 4 უნიკალური ამოცანა
    filename = f"{student}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for i, task in enumerate(selected, 1):
            f.write(f"{i}. {task}\n")
