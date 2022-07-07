import math

mongolia = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева

mongolia_price = mongolia * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.50
cactus_price = cactus * 8

all_flowers = mongolia_price + hyacinths_price + roses_price + cactus_price

taxes = (5 / 100) * all_flowers
left = all_flowers - taxes

if left >= gift_price:
    everything = left - gift_price
    print(f'She is left with {math.floor(everything)} leva.')
else:
    less = gift_price - left
    print(f'She will have to borrow {math.ceil(less)} leva.')