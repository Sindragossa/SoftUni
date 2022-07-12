budget = float(input())
season = input()

price = 0

car_class = ''
car_type = ''

if budget <= 100:
    car_class = 'Economy class'

    if season == 'Summer':
        car_type = 'Cabrio'
        price = (35 / 100) * budget
    elif season == 'Winter':
        car_type = 'Jeep'
        price = (65 / 100) * budget

if 100 < budget <= 500:
    car_class = 'Compact class'

    if season == 'Summer':
        car_type = 'Cabrio'
        price = (45 / 100) * budget
    elif season == 'Winter':
        car_type = 'Jeep'
        price = (80 / 100) * budget

if budget > 500:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    price = (90 / 100) * budget

print(f'{car_class}')
print(f'{car_type} - {price:.2f}')