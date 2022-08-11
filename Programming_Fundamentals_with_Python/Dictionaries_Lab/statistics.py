all_product = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])

    if product not in all_product:
        all_product[product] = quantity
    else:
        all_product[product] += quantity

print('Products in stock:')
for (product, quantity) in all_product.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(all_product.keys())}')
print(f'Total Quantity: {sum(all_product.values())}')

