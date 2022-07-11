text = str(input())
liters = float(input())
card = str(input())

benzine = 2.22
diesel = 2.33
gas = 0.93
cost = 0
price = 0

if text == "Gasoline":
    if card == "Yes":
        discount = benzine - 0.18
        price = liters * discount
        if 20 <= liters <= 25:
            second_discount = (8 / 100) * price
            cost = price - second_discount
        elif liters > 25:
            second_discount = (10 / 100) * price
            cost = price - second_discount
        else:
            cost = price
    if card == "No":
        price = benzine * liters
        if 20 <= liters <= 25:
            second_discount = (8 / 100) * price
            cost = price - second_discount
        elif liters > 25:
            second_discount = (10 / 100) * price
            cost = price - second_discount
        else:
            cost = price

if text == "Diesel":
    if card == "Yes":
        discount = diesel - 0.12
        price = liters * discount
        if 20 <= liters <= 25:
            second_discount = (8 / 100) * price
            cost = price - second_discount
        elif liters > 25:
            second_discount = (10 / 100) * price
            cost = price - second_discount
        else:
            cost = price
    if card == "No":
        price = diesel * liters
        if 20 <= liters <= 25:
            second_discount = (8 / 100) * price
            cost = price - second_discount
        elif liters > 25:
            second_discount = (10 / 100) * price
            cost = price - second_discount
        else:
            cost = price
if text == "Gas":
    if card == "Yes":
        discount = gas - 0.08
        price = liters * discount
        if 20 <= liters <= 25:
            second_discount = (8 / 100) * price
            cost = price - second_discount
        elif liters > 25:
            second_discount = (10 / 100) * price
            cost = price - second_discount
        else:
            cost = price
    if card == "No":
        price = gas * liters
        if 20 <= liters <= 25:
            second_discount = (8 / 100) * price
            cost = price - second_discount
        elif liters > 25:
            second_discount = (10 / 100) * price
            cost = price - second_discount
        else:
            cost = price
print(f"{cost:.2f} lv.")