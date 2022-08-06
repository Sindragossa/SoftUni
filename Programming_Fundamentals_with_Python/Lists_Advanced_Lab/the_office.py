happy_list = input().split(' ')
happiness_factor = int(input())


happy_list = list(map(lambda x: int(x) * happiness_factor, happy_list))
filtered = list(filter(lambda x: x >= (sum(happy_list) / len(happy_list)), happy_list))

if len(filtered) >= len(happy_list) / 2:
    print(f'Score: {len(filtered)}/{len(happy_list)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(happy_list)}. Employees are not happy!')