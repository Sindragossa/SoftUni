stack = []
is_no = False

for c in input():
    if c == '{' or c == '[' or c == '(':
        stack.append(c)
    else:

        if stack:
            if c == '}':
                if stack.pop() != '{':
                    print('NO')
                    is_no = True
                    break

            elif c == ']':
                if stack.pop() != '[':
                    print('NO')
                    is_no = True
                    break
            else:

                if stack.pop() != '(':
                    print('NO')
                    is_no = True
                    break
        else:
            print('NO')
            is_no = True
            break

if not is_no:
    print('YES')