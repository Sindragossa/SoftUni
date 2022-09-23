sets = set()

for _ in range(int(input())):
    line = input().split()
    for c in line:
        sets.add(c)

print('\n'.join(sets))