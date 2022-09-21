matrix = []
rows = int(input())

for _ in range(rows):
    row = ([int(x) for x in input().split(',')])
    matrix.append([x for x in row if x % 2 == 0])

print(matrix)