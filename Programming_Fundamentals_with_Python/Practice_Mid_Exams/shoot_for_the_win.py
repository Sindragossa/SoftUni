targets = [int(el) for el in input().split()]
shots_targets = 0

command = input()
while not command == 'End':
    command = int(command)

    if command not in range(len(targets)):
        command = input()
        continue

    value = targets[command]

    if value == -1:
        command = input()
        continue

    targets[command] = -1
    shots_targets += 1

    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        if targets[i] > value:
            targets[i] -= value
        else:
            targets[i] += value

    command = input()

print(f"Shot targets: {shots_targets} -> {' '.join(str(el) for el in targets)}")