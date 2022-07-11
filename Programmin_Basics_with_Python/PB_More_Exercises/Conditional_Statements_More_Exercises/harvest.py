import math
vine_m = int(input())
grapes = float(input())
litre_wine = int(input())
workers = int(input())

all_grapes = vine_m * grapes
wine = (40 / 100) * all_grapes
kg_grapes = wine / 2.5

if kg_grapes < litre_wine:
    sort = litre_wine - kg_grapes
    print(f'It will be a tough winter! More {math.floor(sort)} liters wine needed.')
else:
    everything = kg_grapes - litre_wine
    everything_workers = everything / workers
    print(f'Good harvest this year! Total wine: {math.floor(kg_grapes)} liters.')
    print(f"{math.ceil(everything)} liters left -> {math.ceil(everything_workers)} liters per person.")

