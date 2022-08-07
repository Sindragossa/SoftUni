number_of_electrons = int(input())
final = []
index = 1

while number_of_electrons >= 2 * index ** 2:
    number_of_electrons -= 2 * index ** 2
    final.append(2 * index ** 2)
    index += 1

if number_of_electrons:
    final.append(number_of_electrons)

print(final)