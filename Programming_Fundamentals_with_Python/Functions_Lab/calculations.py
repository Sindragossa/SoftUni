def calculation_func(numb_a, numb_b, operation):
    if operation == 'multiply':
        return numb_a * numb_b
    elif operation == 'divide':
        return int(numb_a / numb_b)
    elif operation == 'add':
        return numb_a + numb_b
    elif operation == 'subtract':
        return numb_a - numb_b


type_of_operation = input()
first_num = int(input())
second_num = int(input())

print(calculation_func(first_num, second_num, type_of_operation))