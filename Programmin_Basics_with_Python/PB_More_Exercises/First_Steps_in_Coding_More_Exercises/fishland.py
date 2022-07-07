mackerel_price = float(input())
small_fish_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_price = (mackerel_price * 0.60) + mackerel_price
bonito = bonito_kg * bonito_price

horse_mackerel_price = (small_fish_price * 0.80) + small_fish_price
horse_price = horse_mackerel_price * horse_mackerel_kg

mussels_price = mussels_kg * 7.50

needed_money = bonito + horse_price + mussels_price
print(f'{needed_money:.2f}')


