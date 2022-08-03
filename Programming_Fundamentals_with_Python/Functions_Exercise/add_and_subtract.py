def sum_numbers(first, second):
    return first + second


def subtract(cost, third):
    return cost - third


def add_and_subtract(first, second, third):
    cost_of_first_and_second_numbers = sum_numbers(first, second)
    result = subtract(cost_of_first_and_second_numbers, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))