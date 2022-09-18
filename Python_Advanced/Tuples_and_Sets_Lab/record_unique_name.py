names = int(input())
unique_names = set()

for i in range(names):
    unique_names.add(input())

for name in unique_names:
    print(name)