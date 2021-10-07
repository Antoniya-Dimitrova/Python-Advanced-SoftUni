rows, cols = [int(i) for i in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

player_won = False
dead = False
position = None

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "P":
            position = row, col
            position = list(position)

moves = list(input())

for char in moves:
    if char == "L":
        if not position[1] == 0:
            matrix[position[0]][position[1]] = "."
            position[1] -= 1
            if matrix[position[0]][position[1]] == "B":
                dead = True
            else:
                matrix[position[0]][position[1]] = "P"
        else:
            player_won = True
            matrix[position[0]][position[1]] = "."

    elif char == "R":
        if not position[1] == rows - 1:
            matrix[position[0]][position[1]] = "."
            position[1] += 1
            if matrix[position[0]][position[1]] == "B":
                dead = True
            else:
                matrix[position[0]][position[1]] = "P"
        else:
            player_won = True
            matrix[position[0]][position[1]] = "."

    elif char == "U":
        if not position[0] == 0:
            matrix[position[0]][position[1]] = "."
            position[0] -= 1
            if matrix[position[0]][position[1]] == "B":
                dead = True
            else:
                matrix[position[0]][position[1]] = "P"
        else:
            player_won = True
            matrix[position[0]][position[1]] = "."

    elif char == "D":
        if not position[0] == rows - 1:
            matrix[position[0]][position[1]] = "."
            position[0] += 1
            if matrix[position[0]][position[1]] == "B":
                dead = True
            else:
                matrix[position[0]][position[1]] = "P"
        else:
            player_won = True
            matrix[position[0]][position[1]] = "."

    bunny_loc = []

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "B":
                bunny_loc.append((r, c))
    for bunny in bunny_loc:
        up = (bunny[0] - 1, bunny[1])
        down = (bunny[0] + 1, bunny[1])
        left = (bunny[0], bunny[1] - 1)
        right = (bunny[0], bunny[1] + 1)

        if 0 <= up[0] < rows and 0 <= up[1] < cols:
            if matrix[up[0]][up[1]] == "P":
                dead = True
            matrix[up[0]][up[1]] = "B"
        if 0 <= down[0] < rows and 0 <= down[1] < cols:
            if matrix[down[0]][down[1]] == "P":
                dead = True
            matrix[down[0]][down[1]] = "B"
        if 0 <= left[0] < rows and 0 <= left[1] < cols:
            if matrix[left[0]][left[1]] == "P":
                dead = True
            matrix[left[0]][left[1]] = "B"
        if 0 <= right[0] < rows and 0 <= right[1] < cols:
            if matrix[right[0]][right[1]] == "P":
                dead = True
            matrix[right[0]][right[1]] = "B"

    if player_won or dead:
        break

position = [str(i) for i in position]
if dead:
    [print(''.join([str(n) for n in matrix[r]])) for r in range(len(matrix))]
    print(f"dead: {' '.join(position)}")
if player_won:
    [print(''.join([str(n) for n in matrix[r]])) for r in range(len(matrix))]
    print(f"won: {' '.join(position)}")