number = input().split(' ')

abs_number = []

for num in number:
    abs_number.append(abs(float(num)))

print(abs_number)