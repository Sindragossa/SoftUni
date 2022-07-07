import math

radius = float(input())

area = radius * radius * math.pi
perimeter = 2 * math.pi * radius

print(f'{area:.2f}')
print(f'{perimeter:.2f}')