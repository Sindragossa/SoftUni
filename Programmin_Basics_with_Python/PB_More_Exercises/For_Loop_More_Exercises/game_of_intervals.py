result_of_game = int(input())

point = 0
from_zero_to_nine = 0
from_ten_to_nineteen = 0
from_twenty_to_twenty_nine = 0
from_thirty_to_thirty_nine = 0
from_forty_to_fifty = 0
invalid_number = 0

for moves in range(1, result_of_game + 1):
    move = int(input())

    if 0 <= move <= 9:
        point += 0.2 * move
        from_zero_to_nine += 1
    elif 10 <= move <= 19:
        point += 0.3 * move
        from_ten_to_nineteen += 1
    elif 20 <= move <= 29:
        point += 0.4 * move
        from_twenty_to_twenty_nine += 1
    elif 30 <= move <= 39:
        point += 50
        from_thirty_to_thirty_nine += 1
    elif 40 <= move <= 50:
        point += 100
        from_forty_to_fifty += 1
    else:
        point /= 2
        invalid_number += 1

print(f'{point:.2f}')
print(f'From 0 to 9: {(from_zero_to_nine / result_of_game):.2%}')
print(f'From 10 to 19: {(from_ten_to_nineteen / result_of_game):.2%}')
print(f'From 20 to 29: {(from_twenty_to_twenty_nine / result_of_game):.2%}')
print(f'From 30 to 39: {(from_thirty_to_thirty_nine / result_of_game):.2%}')
print(f'From 40 to 50: {(from_forty_to_fifty / result_of_game):.2%}')
print(f'Invalid numbers: {(invalid_number / result_of_game):.2%}')

