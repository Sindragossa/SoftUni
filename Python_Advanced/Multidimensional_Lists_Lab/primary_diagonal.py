n = int(input())
matrix = [list(map(int, input().split())) for x in range(n)]

counter = 0
total = 0

for x in range(n):
    total += matrix[x][x]

print(total)