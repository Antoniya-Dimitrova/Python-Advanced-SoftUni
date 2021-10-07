n = int(input())

matrix = [[int(el) for el in input().split(", ")] for i in range(n)]

elements_primary = []
elements_secondary = []

for row in range(n):
    for col in range(n):
        if row == col:
            elements_primary.append(str(matrix[row][col]))
        if (row + col) == (n - 1):
            elements_secondary.append(str(matrix[row][col]))

print(f"Primary diagonal: {', '.join(elements_primary)}. ", end="")
elements_primary = [int(i) for i in elements_primary]
print(f"Sum: {sum(elements_primary)}")

print(f"Primary diagonal: {', '.join(elements_secondary)}. ", end="")
elements_secondary = [int(i) for i in elements_secondary]
print(f"Sum: {sum(elements_secondary)}")