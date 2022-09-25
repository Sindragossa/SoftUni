names = input().split()
moves = int(input())
idx = 0

while not len(names) == 1:
    idx = (idx + moves) % len(names) - 1

    if idx == -1:
        idx = len(names) - 1
    print(f'Removed {names[idx]}')
    names.pop(idx)

print(f'Last is {names[0]}')