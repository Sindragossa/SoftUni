divisor = int(input())
boundary = int(input())

max_number = 0

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        max_number = current_number
        break

print(max_number)