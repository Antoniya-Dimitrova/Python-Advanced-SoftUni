n = int(input())

matrix = [[int(el) for el in input().split()] for row in range(n)]

elements_primary = []
elements_secondary = []

for row in range(n):
    for col in range(n):
        if row == col:
            elements_primary.append(matrix[row][col])
        if (row + col) == (n - 1):
            elements_secondary.append(matrix[row][col])

print(f"{abs(sum(elements_primary) - sum(elements_secondary))}")
