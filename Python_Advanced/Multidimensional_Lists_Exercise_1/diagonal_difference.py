number = int(input())
matrix = []
diagonal_one = []
diagonal_two = []

for _ in range(number):
    row = list(map(lambda x: int(x), input().split()))
    matrix.append(row)

for i in range(number):
    diagonal_one.append(matrix[i][i])
    diagonal_two.append(matrix[i][number - 1 - i])

print(abs(sum(diagonal_one) - sum(diagonal_two)))