friends_list = input().split(', ')
command = input().split()

black_names = 0
lost_names = 0

while not command[0] == 'Report':
    if command[0] == 'Blacklist':
        if command[1] in friends_list:
            index = friends_list.index(command[1])
            friends_list[index] = 'Blacklisted'
            print(f'{command[1]} was blacklisted.')
            black_names += 1
        else:
            print(f'{command[1]} was not found.')

    elif command[0] == 'Error':
        index = int(command[1])
        if 0 <= index < len(friends_list):
            if not friends_list[index] == 'Blacklisted' and not friends_list[index] == 'Lost':
                print(f'{friends_list[index]} was lost due to an error.')
                friends_list[index] = 'Lost'
                lost_names += 1

    elif command[0] == 'Change':
        index = int(command[1])
        if 0 <= index < len(friends_list):
            print(f'{friends_list[index]} changed his username to {command[2]}.')
            friends_list[index] = command[2]

    command = input().split()

print(f'Blacklisted names: {black_names}')
print(f'Lost names: {lost_names}')
print(*friends_list)