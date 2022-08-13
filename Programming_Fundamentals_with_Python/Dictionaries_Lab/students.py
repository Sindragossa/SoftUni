students = {}

command = input()

while ':' in command:

    info = command.split(':')
    name, id_1, course = info[0], info[1], info[2]

    if course not in students:
        students[course] = {}
    students[course][id_1] = name
    command = input()

course = ' '.join(command.split('_'))
for key, value in students.items():
    if key == course:
        for id_1, name in value.items():
            print(f'{name} - {id_1}')
