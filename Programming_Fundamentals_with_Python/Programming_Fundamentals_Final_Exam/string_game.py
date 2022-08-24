text = input()

while True:
    data = input().split()
    command = data[0]

    if command == 'Done':
        break

    if command == 'Change':
        char = data[1]
        replacement = data[2]
        text = text.replace(char, replacement)
        print(text)

    elif command == 'Includes':
        string_value = data[1]
        if string_value in text:
            print('True')
        else:
            print('False')

    elif command == 'End':
        string_value = data[1]
        if text.endswith(string_value):
            print('True')
        else:
            print('False')

    elif command == 'Uppercase':
        text = text.upper()
        print(text)

    elif command == 'FindIndex':
        char = data[1]
        if char in text:
            print(text.index(char))

    elif command == 'Cut':
        str_index = int(data[1])
        count = int(data[2])
        text = text[str_index:str_index+count]
        print(text)
