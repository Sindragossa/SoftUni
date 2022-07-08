price_of_vegetables = float(input())
price_of_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

price_all = ((price_of_vegetables * kg_vegetables) + (kg_fruits * price_of_fruits)) / 1.94

print(f'{price_all:.2f}')

