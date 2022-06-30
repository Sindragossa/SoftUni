n = int(input())

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        group1 += 1
    elif 200 <= number <= 399:
        group2 += 1
    elif 400 <= number <= 599:
        group3 += 1
    elif 600 <= number <= 799:
        group4 += 1
    elif number >= 800:
        group5 += 1
p1 = (group1 / n) * 100
p2 = (group2 / n) * 100
p3 = (group3 / n) * 100
p4 = (group4 / n) * 100
p5 = (group5 / n) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")