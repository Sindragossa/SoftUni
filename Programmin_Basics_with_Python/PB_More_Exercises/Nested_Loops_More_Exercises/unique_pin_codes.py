max_num_1 = int(input())
max_num_2 = int(input())
max_num_3 = int(input())

for num_1 in range(2, max_num_1 + 1, 2):
    for num_2 in range(2, max_num_2 + 1):
        for num_3 in range(2, max_num_3 + 1, 2):
            if num_2 == 2 or num_2 == 3 or num_2 == 5 or num_2 == 7:
                print(f'{num_1} {num_2} {num_3}')