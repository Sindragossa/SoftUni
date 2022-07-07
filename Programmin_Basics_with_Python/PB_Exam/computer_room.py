mount = input()
hour = int(input())
people = int(input())
hour_of_day = input()

price = 0
if mount == 'march' or mount == 'april' or mount == 'may':
    if hour_of_day == 'day':
        price = 10.50
    elif hour_of_day == 'night':
        price = 8.40
elif mount == 'june' or mount == 'july' or mount == 'august':
    if hour_of_day == 'day':
        price = 12.60
    elif hour_of_day == 'night':
        price = 10.20

if people >= 4:
    price *= 0.9
if hour >= 5:
    price *= 0.50

total_hour = (price * people) / hour
total_sum = total_hour * hour * people

print(f'Price per person for one hour: {total_hour:.2f}')
print(f'Total cost of the visit: {total_sum:.2f}')
