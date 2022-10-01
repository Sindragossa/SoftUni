rows, cols = [int(x) for x in input().split(',')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(',')])


for row in range(cols):
    matrix.append([int(x) for x in input().split(',')])

print(matrix)