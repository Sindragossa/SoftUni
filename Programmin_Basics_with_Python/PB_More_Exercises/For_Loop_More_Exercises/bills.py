months = int(input())

water = 20
all_water = months * 20
internet = 15
all_internet = months * 15
other = 0
all_other = 0
all_electricity = 0

for i in range(1, months + 1):
    electricity = float(input())
    other += internet + water + electricity + (internet + water + electricity) * 0.2
    all_electricity += electricity
average = (all_electricity + all_water + all_internet + other) / months

print(f'Electricity: {all_electricity:.2f} lv')
print(f'Water: {all_water:.2f} lv')
print(f'Internet: {all_internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')