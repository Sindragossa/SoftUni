from collections import deque

string_expression = input().split()

numbers = deque()

for operator in string_expression:
    if operator in '+-*/':
        while len(numbers) > 1:
            num_one = numbers.popleft()
            num_two = numbers.popleft()

            result = 0

            if operator == '+':
                result = num_one + num_two

            elif operator == '-':
                result = num_one - num_two

            elif operator == '*':
                result = num_one * num_two

            else:
                result = num_one // num_two

            numbers.appendleft(result)

    else:
        numbers.append(int(operator))

print(numbers.popleft())