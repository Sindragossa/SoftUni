def tribonachi(times):
    result = ''
    first = 0
    second = 0
    third = 0

    for times in range(1, number + 1):
        if times == 1:
            first = 1
            result += f'{first} '
        elif times == 2:
            second = first
            result += f'{second} '
        elif times == 3:
            third = 2
            result += f'{third} '
        else:
            actual_first = first
            actual_second = second
            actual_third = third

            first = actual_second
            second = actual_third
            third = actual_second + actual_third + actual_first
            result += f'{third} '
    return result


number = int(input())
print(tribonachi(number))

