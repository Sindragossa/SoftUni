my_chats_list = []

command = input()

while command != 'end':
    command = command.split()
    if command[0] == 'Chat':
        my_chats_list.append(command[1])

    elif command[0] == 'Delete':
        if command[1] in my_chats_list:
            position = my_chats_list.index(command[1])
            my_chats_list.pop(position)

    elif command[0] == 'Edit':
        if command[1] in my_chats_list:
            position = my_chats_list.index(command[1])
            my_chats_list[position] = command[2]

    elif command[0] == 'Spam':
        for com in command[1:]:
            my_chats_list.append(com)

    elif command[0] == 'Pin':
        if command[1] in my_chats_list:
            position = my_chats_list.index(command[1])
            my_chats_list.append(my_chats_list.pop(position))

    command = input()

print('\n'.join(my_chats_list))