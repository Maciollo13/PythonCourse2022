def player_row_selection():
    while True:
        row_choice = input("Select in wich row you want to put symbol. [A,B,C]")
        row_choice = row_choice.lower()
        row_choice = row_choice[0]
        if row_choice == "a":
            row_choice = 1
        if row_choice == "b":
            row_choice = 2
        if row_choice == "c":
            row_choice = 3
        if row_choice in [1, 2, 3]:
            break
        else:
            print("Choose one of given possibilities: [A,B,C]")
    return row_choice


def player_column_selection():
    while True:
        column = input("Select in wich column you want to put symbol. [1,2,3]")
        column = column[0]
        if column == "1":
            column = 1
        if column == "2":
            column = 3
        if column == "3":
            column = 5
        if column in [1, 3, 5]:
            break
        else:
            print("Choose one of given possibilities: [1,2,3]")
    return column


def board_true_check(row, column, board):
    if board[row][column] == "X" or board[row][column] == "O":
        return False
    else:
        return True


def board_fill(row, column, board, player_num):
    if player_num == 1:
        board[row][column] = "X"
    else:
        board[row][column] = "O"
    return board


def player_switch(player_num):
    if player_num == 1:
        player_num = 2
    else:
        player_num = 1
    return player_num


def game_board_og():
    game_board = [
        [" ", "1", " ", "2", " ", "3"],
        ["A", ".", "|", ".", "|", "."],
        ["B", ".", "|", ".", "|", "."],
        ["C", ".", "|", ".", "|", "."]
    ]
    return game_board


def game():
    player = 1
    tries = 1
    board_og = game_board_og()
    board_changed = game_board_og()
    while tries <= 10:
        print(f"****** round {tries} ******")
        while True:
            row_selection = player_row_selection()
            column_selection = player_column_selection()
            if board_true_check(row_selection, column_selection, board_og):
                board_changed = board_fill(row_selection, column_selection, board_og, player)
                for i in board_changed:
                    print(*i)
                break
            else:
                print("This spot is filled. Choose different one!")
        player = player_switch(player)

        board_og = board_changed
        tries += 1


game()
