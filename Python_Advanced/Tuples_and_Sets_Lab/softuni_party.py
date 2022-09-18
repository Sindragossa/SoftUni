number_of_guest = int(input())
reservation = set()

for _ in range(number_of_guest):
    reservation.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        reservation.remove(guest)

print(len(reservation))
print('\n'.join(sorted(reservation)))