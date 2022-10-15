number = int(input())
first_two_letters = 0
second_two_letters = 0
compiler = 0
is_time = False
for car_number in range(1000, 10000):
    symbol = str(car_number)
    first_two_letters = 0
    second_two_letters = 0
    compiler = 0
    for index, digit in enumerate(symbol):
        digit = int(digit)
        if digit != 0:
            if index <= 1:
                first_two_letters += digit
                compiler += 1
            else:
                second_two_letters += digit
                compiler += 1
            if first_two_letters == 0 and compiler == 4:
                break
            else:
                if number % first_two_letters == 0 and first_two_letters == second_two_letters and compiler == 4:
                    print(symbol, end=' ')
