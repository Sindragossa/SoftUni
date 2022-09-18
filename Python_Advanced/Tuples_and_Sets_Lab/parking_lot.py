lines = int(input())
cars = set()

for i in range(lines):
    direction, plate = input().split(', ')

    if direction == 'IN':
        cars.add(plate)

    if direction == 'OUT':
        cars.remove(plate)

if len(cars) > 0:
    for plate in cars:
        print(plate)
else:
    print('Parking Lot is Empty')