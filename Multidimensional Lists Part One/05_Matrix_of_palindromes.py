rows, cols = [int(i) for i in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        first_and_third_letter = chr(97+row)
        second_letter = chr(ord(first_and_third_letter)+col)
        element = first_and_third_letter + second_letter + first_and_third_letter
        matrix[row].append(element)
for row in range(rows):
    print(*matrix[row])