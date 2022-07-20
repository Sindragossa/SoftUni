command = input()

double_char = ''
new_text = ''

while command != 'End':

    if command == 'SoftUni':
        command = input()
        continue

    for index, letter in enumerate(command):
        double_char = letter * 2
        new_text += double_char

    print(new_text)
    double_char = ''
    new_text = ''

    command = input()