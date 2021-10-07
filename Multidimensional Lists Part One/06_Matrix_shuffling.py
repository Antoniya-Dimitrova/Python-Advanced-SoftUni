rows, cols = [int(i) for i in input().split()]

matrix = [[int(el) for el in input().split()]for row in range(rows)]

command = input()

while not command == "END":
    command_list = command.split()
    if len(command_list) == 5 and command_list[0] == "swap":
        row_1 = int(command_list[1])
        col_1 = int(command_list[2])
        row_2 = int(command_list[3])
        col_2 = int(command_list[4])
        if 0 <= row_1 <= rows and 0 <= row_2 <= rows and 0 <= col_1 <= cols and 0 <= col_2 <= cols:
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for row in range(rows):
                print(*matrix[row])
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
