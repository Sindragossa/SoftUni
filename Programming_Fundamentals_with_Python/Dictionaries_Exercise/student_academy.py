from collections import defaultdict

students = defaultdict(list)
num = int(input())

for n in range(num):
    name = input()
    grade = float(input())

    students[name].append(grade)

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f'{student} -> {average_grade:.2f}')