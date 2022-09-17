my_stack = []
n = int(input())

for _ in range(n):
    current_parts = input().split()
    command = current_parts[0]

    if command == '1':
        current_num = int(current_parts[1])
        my_stack.append(current_num)

    elif command == '2' and my_stack:
        my_stack.pop()

    elif command == '3' and my_stack:
        print(max(my_stack))

    elif command == '4' and my_stack:
        print(min(my_stack))

while my_stack:
    el = my_stack.pop()

    if my_stack:
        print(el, end=', ')
    else:
        print(el)