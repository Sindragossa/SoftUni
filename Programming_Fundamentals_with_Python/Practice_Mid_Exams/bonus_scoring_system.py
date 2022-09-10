import math
count_students = int(input())
count_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attendances = 0

if count_lectures > 0 and count_students > 0:
    for bonus_points_student in range(count_students):
        attendances_student = int(input())
        total_bonus = attendances_student / count_lectures * (5 + additional_bonus)
        if total_bonus >= max_bonus:
            max_bonus = total_bonus
            attendances = attendances_student

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {attendances} lectures.")