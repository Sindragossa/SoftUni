animals = input()

is_pet = animals == 'dog'
is_wild_animal = animals == 'crocodile' or animals == 'tortoise' or animals == 'snake'

if is_pet:
    print('mammal')
elif is_wild_animal:
    print('reptile')
else:
    print('unknown')