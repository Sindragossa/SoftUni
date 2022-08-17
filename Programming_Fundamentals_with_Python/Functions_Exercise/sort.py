numbers = input()


def sorted_numbers(number: str):
    number = [int(element) for element in number.split()]
    sorted_list = sorted(number)
    return sorted_list


print(sorted_numbers(numbers))