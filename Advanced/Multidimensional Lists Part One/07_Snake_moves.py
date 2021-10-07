from collections import deque
rows, cols = [int(i) for i in input().split()]

text = input()

matrix = []

working_text = deque(text)

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        if working_text:
            matrix[row].append(working_text.popleft())
            #matrix[row].append(working_text[0])
            #working_text.append(working_text.popleft())
        else:
            working_text = deque(text)
            matrix[row].append(working_text.popleft())

for row in range(rows):
    if row % 2 == 1:
        matrix[row].reverse()

for i in range(rows):
    print("".join(matrix[i]))