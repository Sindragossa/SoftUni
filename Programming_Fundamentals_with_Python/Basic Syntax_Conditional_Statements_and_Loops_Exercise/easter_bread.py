budget = float(input())
kg_flour_price = float(input())
one_pack_of_eggs_price = kg_flour_price * 0.75
liter_milk = kg_flour_price + (kg_flour_price * 0.25)
recipe = one_pack_of_eggs_price + kg_flour_price + (liter_milk * 0.250)
colored_eggs = 0
counter_breads = 0

while budget > recipe:
    budget -= recipe
    colored_eggs += 3
    counter_breads += 1

    if counter_breads % 3 == 0:
        colored_eggs -= (counter_breads - 2)

print(f"You made {counter_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")