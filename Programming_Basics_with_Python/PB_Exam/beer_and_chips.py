import math

football_fan = str(input())
budget = float(input())
beer = int(input())
chips = int(input())

beer_price = 1.20 * beer
chips_price = beer_price * 0.45
chips_sum = math.ceil(chips_price * chips)

total_price = beer_price + chips_sum

if budget >= total_price:
    cost = budget - total_price
    print(f"{football_fan} bought a snack and has {cost:.2f} leva left.")
elif total_price > budget:
    cost_2 = total_price - budget
    print(f"{football_fan} needs {cost_2:.2f} more leva!")
