initial_energy = int(input())
count = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f'Won battles: {count}. Energy left: {initial_energy}')
        break

    distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        count += 1

        if count % 3 == 0:
            initial_energy += count
    else:
        print(f'Not enough energy! Game ends with {count} won battles and {initial_energy} energy')
        break

