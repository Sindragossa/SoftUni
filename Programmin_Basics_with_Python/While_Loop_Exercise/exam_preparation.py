poor_grades = int(input())

sum_grades = 0
count_grades = 0
last_problem = ""
count_poor_grades = 0
has_failed = False
input_line = input()
while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        count_poor_grades += 1

    last_problem = input_line
    count_grades = count_grades + 1
    sum_grades = sum_grades + grade

    if poor_grades == count_poor_grades:
        has_failed = True
        break
    input_line = input()

if has_failed:
    print(f"You need a break, {count_poor_grades} poor grades.")
else:
    avg_grades = sum_grades / count_grades
    print(f"Average score: {avg_grades:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
