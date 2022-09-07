numbers_values = list(map(int, input().split()))
command = input()

while command != 'end':
    command_split = command.split()
    command_value = command_split[0]

    if command_value == 'swap':
        first_index = int(command_split[1])
        second_index = int(command_split[2])
        numbers_values[first_index], numbers_values[second_index] = numbers_values[second_index], numbers_values[first_index]

    elif command_value == 'multiply':
        first_index = int(command_split[1])
        second_index = int(command_split[2])
        result = numbers_values[first_index] * numbers_values[second_index]
        numbers_values.pop(first_index)
        numbers_values.insert(first_index, result)

    elif command_value == 'decrease':
        for num in range(len(numbers_values)):
            numbers_values[num] -= 1

    command = input()

print(', '.join(list(map(str, numbers_values))))
