def board_true_check(row, column, board):
    if board[row][column] == "." or board[row][column] == "X" or board[row][column] == "O":
        return False
    else:
        return True

