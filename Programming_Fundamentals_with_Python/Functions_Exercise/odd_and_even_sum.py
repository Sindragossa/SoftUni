def odd_and_even_sum(number: int):
    even_sum = 0
    odd_sum = 0
    num_of_str = str(number)
    for element in num_of_str:
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


digit = int(input())
print(odd_and_even_sum(digit))