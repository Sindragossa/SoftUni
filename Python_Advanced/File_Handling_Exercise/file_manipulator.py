import os

command = input()

while command != 'End':
    command = command.split('-')
    if command[0] == 'Create':
        if os.path.exists(command[1]):
            os.remove(command[1])
        else:
            with open(command[1], 'w'):
                pass
    elif command[0] == 'Add':
        file_name = command[1]
        content = command[2]

        if os.path.exists(command[1]):
            with open(command[1], 'a') as file:
                file.write(f'\n{content}')
        else:
            with open(command[1], 'w') as file:
                file.write(content)
    elif command[0] == 'Replace':
        if os.path.exists(command[1]):
            with open(command[1], 'r') as file:
                lines = ''.join(file.readlines()).strip()
                lines = lines.replace(command[2], command[3])
                with open(command[1], 'w') as file1:
                    file1.write(lines)
        else:
            print('An error occurred')
    elif command[0] == 'Delete':
        if os.path.exists(command[1]):
            os.remove(command[1])
        else:
            print('An error occurred')

    command = input()