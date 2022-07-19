numbers = int(input())

for number in range(numbers):
    current_num = int(input())

    if current_num > 88:
        print('Bye.')
    elif current_num < 86 or current_num == 87:
        print('GREAT!')
    elif current_num == 88:
        print('Hello')
    elif current_num == 86:
        print('How are you?')

