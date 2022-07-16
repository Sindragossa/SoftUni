num_of_student = int(input())

top_student = 0
between_four = 0
between_three = 0
fail_student = 0
average_student = 0

for student in range(1, num_of_student + 1):
    grade_of_student = float(input())

    if grade_of_student >= 5:
        top_student += 1
        average_student += grade_of_student
    elif 4 <= grade_of_student <= 4.99:
        between_four += 1
        average_student += grade_of_student
    elif 3 <= grade_of_student <= 3.99:
        between_three += 1
        average_student += grade_of_student
    elif 2 <= grade_of_student <= 2.99:
        fail_student += 1
        average_student += grade_of_student

print(f'Top students: {(top_student / num_of_student):.2%}')
print(f'Between 4.00 and 4.99: {(between_four / num_of_student):.2%}')
print(f'Between 3.00 and 3.99: {(between_three / num_of_student):.2%}')
print(f'Fail: {(fail_student / num_of_student):.2%}')
print(f'Average: {(average_student / num_of_student):.2f}')

