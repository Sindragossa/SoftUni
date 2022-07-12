budget = float(input())
category = input()
group = int(input())

vip = 499.99
normal = 249.99

price = 0

if group <= 4:
    price = (75 / 100) * budget
elif 5 <= group <= 9:
    price = (60 / 100) * budget
elif 10 <= group <= 24:
    price = (50 / 100) * budget
elif 25 <= group <= 49:
    price = (40 / 100) * budget
else:
    price = (25 / 100) * budget

if category == 'VIP':
    money = budget - price
    money_1 = vip * group

    if money >= money_1:
        more_money = money - money_1
        print(f'Yes! You have {more_money:.2f} leva left.')
    else:
        less_money = money_1 - money
        print(f'Not enough money! You need {less_money:.2f} leva.')

elif category == 'Normal':
    money = budget - price
    money_1 = normal * group
    if money >= money_1:
        more_money = money - money_1
        print(f'Yes! You have {more_money:.2f} leva left.')
    else:
        less_money = money_1 - money
        print(f'Not enough money! You need {less_money:.2f} leva.')
