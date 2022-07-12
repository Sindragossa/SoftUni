young_people = int(input())
adults_people = int(input())
route = input()

all_people = 0

if route == 'trail':
    juniors = young_people * 5.50
    seniors = adults_people * 7
    all_people = juniors + seniors

elif route == 'cross-country':
    juniors = young_people * 8
    seniors = adults_people * 9.50
    people = young_people + adults_people

    if people >= 50:
        price = juniors + seniors
        discount = (25 / 100) * price
        all_people = price - discount
    else:
        all_people = juniors + seniors
elif route == 'downhill':
    juniors = young_people * 12.25
    seniors = adults_people * 13.75
    all_people = juniors + seniors

elif route == 'road':
    juniors = young_people * 20
    seniors = adults_people * 21.50
    all_people = juniors + seniors

cost = (5 / 100) * all_people
cost_1 = all_people - cost
print(f'{cost_1:.2f}')