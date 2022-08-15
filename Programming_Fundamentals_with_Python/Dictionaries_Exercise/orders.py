our_dict = {}
including_list = []

command = input()

while command != 'buy':
    key, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    including_list = [price, quantity]

    if key in our_dict:
        our_dict[key][0] = price
        our_dict[key][1] += quantity
    else:
        our_dict[key] = including_list

    command = input()

for key, price_and_quantity in our_dict.items():
    price, quantity = price_and_quantity
    total_price = price * quantity
    print(f'{key} -> {total_price:.2f}')