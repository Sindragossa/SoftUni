season = input()
kilometers = float(input())

price = 0

if kilometers <= 5000:
    if season == 'Spring':
        price = 0.75
    elif season == 'Summer':
        price = 0.90
    elif season == 'Autumn':
        price = 0.75
    elif season == 'Winter':
        price = 1.05
elif 5000 < kilometers <= 10000:
    if season == 'Spring':
        price = 0.95
    elif season == 'Summer':
        price = 1.10
    elif season == 'Autumn':
        price = 0.95
    elif season == 'Winter':
        price = 1.25
elif 10000 < kilometers <= 20000:
    if season == 'Spring':
        price = 1.45
    elif season == 'Summer':
        price = 1.45
    elif season == 'Autumn':
        price = 1.45
    elif season == 'Winter':
        price = 1.45

total_price = (kilometers * price) * 4
total_price -= (10/100) * total_price

print(f'{total_price:.2f}')