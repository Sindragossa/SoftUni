import math

days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

dog = dog_food_kg * days
cat = cat_food_kg * days
turtle = (turtle_food_gr * days) / 1000

all_food = dog + cat + turtle

if all_food <= food_kg:
    food_left = food_kg - all_food
    print(f'{math.floor(food_left)} kilos of food left.')
else:
    food_more = all_food - food_kg
    print(f'{math.ceil(food_more)} more kilos of food are needed.')