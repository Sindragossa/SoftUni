numbers = int(input())
num = 0
sum = 0

while numbers != num:
    number = int(input())
    num += 1
    sum += number
cost = sum / num
print(f'{cost:.2f}')