lines = int(input())
students = {}

for _ in range(lines):
    student, grade = input().split()

    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    grades_list = " ".join(str(f'{grade:.2f}') for grade in grades)
    avg_grate = sum(grades) / len(grades)

    print(f"{student} -> {grades_list} (avg: {avg_grate:.2f})")