n_chrysanthemums = int(input())
n_roses = int(input())
n_tulips = int(input())
season = input()
holiday = input()

price = 0

if season == 'Spring':
    chrysanthemums = n_chrysanthemums * 2.00
    roses = n_roses * 4.10
    tulips = n_tulips * 2.50
    price = chrysanthemums + roses + tulips
    all_flowers = n_roses + n_tulips + n_chrysanthemums

    if holiday == 'Y':
        price += (15 / 100) * price

    if n_tulips > 7:
        price -= (5 / 100) * price

    if all_flowers > 20:
        price -= (20 / 100) * price

elif season == 'Summer':
    chrysanthemums = n_chrysanthemums * 2.00
    roses = n_roses * 4.10
    tulips = n_tulips * 2.50
    price = chrysanthemums + roses + tulips
    all_flowers = n_roses + n_tulips + n_chrysanthemums

    if holiday == 'Y':
        price += (15 / 100) * price

    if all_flowers > 20:
        price -= (20 / 100) * price

elif season == 'Autumn':
    chrysanthemums = n_chrysanthemums * 3.75
    roses = n_roses * 4.50
    tulips = n_tulips * 4.15
    price = chrysanthemums + roses + tulips
    all_flowers = n_roses + n_tulips + n_chrysanthemums

    if holiday == 'Y':
        price += (15 / 100) * price

    if all_flowers > 20:
        price -= (20 / 100) * price

elif season == 'Winter':
    chrysanthemums = n_chrysanthemums * 3.75
    roses = n_roses * 4.50
    tulips = n_tulips * 4.15
    price = chrysanthemums + roses + tulips
    all_flowers = n_roses + n_tulips + n_chrysanthemums

    if holiday == 'Y':
        price += (15 / 100) * price

    if n_roses > 10:
        price -= (10 / 100) * price

    if all_flowers > 20:
        price -= (20 / 100) * price

total_price = price + 2

print(f'{total_price:.2f}')



