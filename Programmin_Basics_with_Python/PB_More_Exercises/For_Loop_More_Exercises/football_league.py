capacity_of_stadium = int(input())
num_of_fans = int(input())

fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for fan in range(1, num_of_fans + 1):
    sector = input()
    if sector == 'A':
        fans_a += 1
    elif sector == 'B':
        fans_b += 1
    elif sector == 'V':
        fans_v += 1
    elif sector == 'G':
        fans_g += 1

print(f'{(fans_a / num_of_fans):.2%}')
print(f'{(fans_b / num_of_fans):.2%}')
print(f'{(fans_v / num_of_fans):.2%}')
print(f'{(fans_g / num_of_fans):.2%}')
print(f'{(num_of_fans / capacity_of_stadium):.2%}')