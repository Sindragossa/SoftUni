resource = {}

while True:
    command = input()

    if command == 'stop':
        break

    quantity = int(input())

    if command not in resource.keys():
        resource[command] = 0
    resource[command] += quantity

for resource, quantity in resource.items():
    print(f'{resource} -> {quantity}')
