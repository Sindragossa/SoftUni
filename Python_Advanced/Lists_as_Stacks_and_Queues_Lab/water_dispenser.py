water_quantity = int(input())
queue = []

while True:
    command = input()
    if command == 'Start':
        break
    else:
        queue.append(command)


while True:
    command = input()
    if command == 'End':
        break
    else:
        command = command.split()
        if command[0] == 'refill':
            water_quantity += int(command[1])
        else:
            liters = int(command[0])
            name = queue.pop(0)
            if water_quantity >= liters:
                print(f'{name} got water')
                water_quantity -= liters
            else:
                print(f'{name} must wait')

print(f'{water_quantity} liters left')