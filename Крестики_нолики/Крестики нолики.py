print("Игра: Крестики-нолики\n")
matrix_ = [
    [" ", "0", "1", "2"],
    ["0", "-", "-", "-"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"]
]


def check_victory():
    global player
    if matrix_[1][1] == player and matrix_[2][2] == player and matrix_[3][3] == player:
        return 1
    if matrix_[1][3] == player and matrix_[2][2] == player and matrix_[3][1] == player:
        return 1
    if matrix_[2][1] == player and matrix_[2][2] == player and matrix_[2][3] == player:
        return 1
    if matrix_[1][2] == player and matrix_[2][2] == player and matrix_[3][2] == player:
        return 1


def matrix_output():
    for row in matrix_:
        for element in row:
            print(element, end="  ")
        print()


def input_row():
    global player
    print("_________________________________")
    while True:
        row_ = int(input(f"Введите номер строки где ставите '{player}': "))
        if 0 <= row_ <= 2:
            return row_
        else:
            print("\n! Введите корректную строку !\n")


def input_col():
    global player
    while True:
        col_ = int(input(f"Введите номер столбца где ставите '{player}': "))
        if 0 <= col_ <= 2:
            return col_
        else:
            print("\n! Введите корректный столбец !\n")


matrix_output()
cn_end = 0
cn_draw = 0
while True:
    if cn_end == 1:
        break
    if cn_draw == 9:
        break
    else:
        while True:
            player = "x"
            print("_________________________________")
            print("Ход крестиков")
            row_game = input_row()
            col_game = input_col()
            if matrix_[row_game + 1][col_game + 1] == "x" or matrix_[row_game + 1][col_game + 1] == "o":
                print("\n! Данная клетка уже занята !")
                print("! Попробуйте еще раз !")
                continue
            matrix_[row_game + 1][col_game + 1] = "x"
            cn_draw += 1
            matrix_output()
            victory = check_victory()
            if victory == 1:
                print("_________________________________")
                print("Игра окончена\nПобедил игрок на крестиках")
                cn_end = 1
                break
            break
        if cn_end == 1:
            break
        if cn_draw == 9:
            print("_________________________________")
            print("\nИгра закончилась вничью")
            break
        while True:
            player = "o"
            print("_________________________________")
            print("Ход ноликов")
            row_game = input_row()
            col_game = input_col()
            if matrix_[row_game + 1][col_game + 1] == "x" or matrix_[row_game + 1][col_game + 1] == "o":
                print("\n! Данная клетка уже занята !")
                print("! Попробуйте еще раз !")
                continue
            matrix_[row_game + 1][col_game + 1] = "o"
            cn_draw += 1
            matrix_output()
            victory = check_victory()
            if victory == 1:
                print("_________________________________")
                print("Игра окончена\nПобедил игрок на ноликах")
                cn_end = 1
                break
            break
