n = int(input())

direction = input().split()

matrix = [[el for el in input().split()] for row in range(n)]

coal = 0
total_coal = 0

is_over = False
for row in range(n):
    for el in matrix[row]:
        if el == "c":
            total_coal += 1

position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            position = row, col
            position = list(position)

for command in direction:

    if command == "left":
        if not position[1] == 0:
            position[1] -= 1
    elif command == "right":
        if not position[1] == n-1:
            position[1] += 1
    elif command == "up":
        if not position[0] == 0:
            position[0] -= 1
    elif command == "down":
        if not position[0] == n-1:
            position[0] += 1

    if matrix[position[0]][position[1]] == "c":
        coal += 1
        matrix[position[0]][position[1]] = "*"

    if matrix[position[0]][position[1]] == "e":
        is_over = True
        print(f"Game over! {tuple(position)}")
        break
    if coal == total_coal:
        print(f"You collected all coal! {tuple(position)}")
        break

if not coal == total_coal and not is_over:
    print(f"{total_coal - coal} pieces of coal left. {tuple(position)}")

