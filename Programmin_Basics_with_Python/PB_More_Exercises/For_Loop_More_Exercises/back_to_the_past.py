family_money = float(input())

age = 18

for year in range(1800, int(input()) + 1):
    if year % 2 == 0:
        family_money -= 12000
    else:
        family_money -= 12000 + 50 * age

    age += 1

if family_money >= 0:
    print(f'Yes! He will live a carefree life and will have {family_money:.2f} dollars left.')
else:
    print(f'He will need {abs(family_money):.2f} dollars to survive.')