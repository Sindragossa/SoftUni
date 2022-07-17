number = int(input())

minibus = 0
truck = 0
train = 0
count1 = 0
count2 = 0
count3 = 0
tons_count = 0

for b in range(1, number + 1):
    tons = int(input())
    if tons <= 3:
        minibus += 200 * tons
        count1 += tons
        tons_count += tons
    elif 4 <= tons <= 11:
        truck += tons * 175
        count2 += tons
        tons_count += tons
    elif tons >= 12:
        train += tons * 120
        count3 += tons
        tons_count += tons

print(f'{((minibus + truck + train) / tons_count):.2f}')
print(f'{(count1 / tons_count):.2%}')
print(f'{(count2 / tons_count):.2%}')
print(f'{(count3 / tons_count):.2%}')
