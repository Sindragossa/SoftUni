price_per_kg = 12.45

number_of_cats = int(input())

group1 = 0
group2 = 0
group3 = 0

total_amount_of_food = 0

for cat in range(number_of_cats):
    amount_of_food = int(input())
    total_amount_of_food += amount_of_food
    if 100 <= amount_of_food < 200:
        group1 += 1
    elif 200 <= amount_of_food < 300:
        group2 += 1
    elif 300 <= amount_of_food < 400:
        group3 += 1

food_per_day = total_amount_of_food / 1000 * price_per_kg

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {food_per_day:.2f} lv.")