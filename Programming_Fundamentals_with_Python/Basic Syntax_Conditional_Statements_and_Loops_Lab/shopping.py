budget = int(input())
command = input()

while command != 'End':
    price_command = int(command)
    budget -= price_command
    if budget < 0:
        print(f'You went in overdraft!')
        break
    command = input()
else:
    print(f'You bought everything needed.')