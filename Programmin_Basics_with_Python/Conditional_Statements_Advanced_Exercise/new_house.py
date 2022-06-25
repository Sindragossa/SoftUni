type = str(input())
count = int(input())
budget = int(input())

needed_money = 0

if type == "Roses":
    needed_money = count * 5

    if count > 80:
        needed_money -= needed_money * 0.1

elif type == "Dahlias":
    needed_money = count * 3.80

    if count > 90:
        needed_money -= needed_money * 0.15

elif type == "Tulips":
    needed_money = count * 2.80

    if count > 80:
        needed_money -= needed_money * 0.15

elif type == "Narcissus":
    needed_money = count * 3

    if count < 120:
        needed_money += needed_money * 0.15

elif type == "Gladiolus":
    needed_money = count * 2.50

    if count < 80:
        needed_money += needed_money * 0.2

if budget >= needed_money:
    print(f"Hey, you have a great garden with {count} {type} and {(budget - needed_money):.2f} leva left.")
elif budget < needed_money:
    print(f"Not enough money, you need {(needed_money - budget):.2f} leva more.")