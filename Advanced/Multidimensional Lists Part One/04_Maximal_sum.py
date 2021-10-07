import sys
rows, cols = [int(i) for i in input().split()]

matrix = [[int(el) for el in input().split()]for row in range(rows)]

max_sum = -sys.maxsize
position = None
for row in range(rows-1, 1, -1):
    for col in range(cols-1, 1, -1):
        current_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row][col - 2] +\
                      matrix[row - 1][col] + matrix[row - 1][col - 1] + matrix[row - 1][col - 2] + \
                      matrix[row - 2][col-2] + matrix[row-2][col-1] + matrix[row-2][col]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)
row, col = position
print(f"Sum = {max_sum}")
print(matrix[row - 2][col - 2], matrix[row - 2][col - 1], matrix[row - 2][col])
print(matrix[row - 1][col - 2], matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 2], matrix[row][col - 1], matrix[row][col])