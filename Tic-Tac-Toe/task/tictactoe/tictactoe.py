cells = [cell for cell in "         "]
matrix_cells = [cell for row in range(3) for cell in [cells[row * 3:row * 3 + 3]]]

check_matrix = [[[0, 0], [0, 1], [0, 2]],
                [[1, 0], [1, 1], [1, 2]],
                [[2, 0], [2, 1], [2, 2]],
                [[0, 0], [1, 0], [2, 0]],
                [[0, 1], [1, 1], [2, 1]],
                [[0, 2], [1, 2], [2, 2]],
                [[0, 0], [1, 1], [2, 2]],
                [[2, 0], [1, 1], [0, 2]]]

x_wins = 0
o_wins = 0

number_of_o = 0
number_of_x = 0

numbers = set("0123456789")
valid_coordinates = set("123")
valid_cells = ["X", "O"]
number_of_steps = -1

impossible_check = False

print("---------")
for i in range(3):
    print("|", matrix_cells[i][0], matrix_cells[i][1], matrix_cells[i][2], "|")
print("---------")

while True:

    number_of_steps += 1
    actual_player = valid_cells[number_of_steps % 2]

    empty_gap = False

    while True:

        coordinate_in_number = []
        not_numbers = False
        not_valid_numbers = False

        print("Enter the coordinates:")
        coordinate = input().split()

        if len(coordinate) != 2:
            print("You should enter numbers!")
            continue

        for i in range(2):
            for character in coordinate[i]:
                if character not in numbers:
                    not_numbers = True
            if not not_numbers:
                if coordinate[i] in valid_coordinates:
                    coordinate_in_number.append(int(coordinate[i]) - 1)
                else:
                    not_valid_numbers = True

        if not_numbers:
            print("You should enter numbers!")
            continue

        if not_valid_numbers:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            if matrix_cells[coordinate_in_number[0]][coordinate_in_number[1]] in valid_cells:
                print("This cell is occupied! Choose another one!")
                continue
            else:
                matrix_cells[coordinate_in_number[0]][coordinate_in_number[1]] = actual_player
                break

    print("---------")
    for i in range(3):
        print("|", matrix_cells[i][0], matrix_cells[i][1], matrix_cells[i][2], "|")
        for j in range(3):
            if matrix_cells[i][j] == "O":
                number_of_o += 1
            elif matrix_cells[i][j] == "X":
                number_of_x += 1
    print("---------")

    if abs(number_of_x - number_of_o) > 1:
        impossible_check = True

    for case in check_matrix:
        x_case_check = True
        o_case_check = True
        for coordinate in case:
            if matrix_cells[coordinate[0]][coordinate[1]] != "X":
                x_case_check = x_case_check & False
            if matrix_cells[coordinate[0]][coordinate[1]] != "O":
                o_case_check = o_case_check & False
            if matrix_cells[coordinate[0]][coordinate[1]] == " ":
                empty_gap |= True
        if x_case_check:
            x_wins += 1
        if o_case_check:
            o_wins += 1

    if (x_wins > 0) & (x_wins > o_wins):
        print("X wins")
        break

    if (o_wins > 0) & (o_wins > x_wins):
        print("O wins")
        break

    if (x_wins == o_wins) & (empty_gap is False):
        print("Draw")
        break
