budget = float(input())
number_of_statist = int(input())
one_dress_price = float(input())
decor = budget * 0.1  #budget * 10/100
dresses_price = number_of_statist * one_dress_price
if number_of_statist > 150:
    dresses_price *= 0.9  #dreses_price = dreses_price * 90/100
needed_money = decor + dresses_price
difference = abs(needed_money - budget)
if needed_money > budget: #Парите не стигат
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else: #Парите стигат -> budget >= needed_money
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
