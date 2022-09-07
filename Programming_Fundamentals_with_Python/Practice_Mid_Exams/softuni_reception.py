first_top_worker = int(input())
second_top_worker = int(input())
third_top_worker = int(input())
numbers_of_students_as_s = int(input())
needed_time = 0

all_top_workers = first_top_worker + second_top_worker + third_top_worker
if numbers_of_students_as_s % all_top_workers != 0:
    needed_time = numbers_of_students_as_s // all_top_workers + 1
else:
    needed_time = numbers_of_students_as_s // all_top_workers

if needed_time > 3:
    if needed_time % 3 == 0:
        needed_time += needed_time // 3 - 1
    else:
        needed_time += needed_time // 3


print(f'Time needed: {needed_time}h.')