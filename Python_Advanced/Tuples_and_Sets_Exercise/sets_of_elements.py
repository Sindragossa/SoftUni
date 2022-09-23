first, second = tuple(map(int, input().split()))

first_set = {input() for _ in range(first)}
second_set = {input() for _ in range(second)}

print('\n'.join((map(str, first_set.intersection(second_set)))))