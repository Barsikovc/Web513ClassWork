stud_marks = [
    ['Bob', 5, 4, 5],
    ['Alice', 5, 5, 5],
    ['Tom', 3, 4, 3]
]

for name, mark1, mark2, mark3 in stud_marks:
    print(f'Имя: {name}. Оценки: {mark1}, {mark2}, {mark3}. Средний балл: {(mark1 + mark2 + mark3) / 3:.2f}')
