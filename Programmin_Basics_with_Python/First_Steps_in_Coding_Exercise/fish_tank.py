lenght = int(input())
wide = int(input())
haight = int(input())
percent = float(input()) #1l=1dm
aquarium_size = lenght * wide * haight
litres = aquarium_size * 0.001
taken_space = 0.17
needed_litre = litres * (1 - 0.17)
print(needed_litre)