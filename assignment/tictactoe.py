board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_is_still_going = True

winner = None
current_player = "X"


def dispaly_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    dispaly_board()

    while game_is_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner == "Won.")
    elif winner is None:
        print("Tie.")


def handle_turn(player):
    position = input("choose a position from 1 -9: ")
    position = int(position) - 1

    board[position] = "X"
    dispaly_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    row_winner =check_row()
    columns_winner = check_columns()
    diagonal_winner =check_diagonals()
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_row():
    global game_is_still_going
    row_1 = board[0]== board[1] ==board[2] != "_"
    row_2 = board[3]== board[4] ==board[5] != "_"
    row_3 = board[6]== board[7] ==board[8] != "_"
    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_is_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_is_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_is_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "_"
    diagonals_2 = board[6] == board[4] == board[2] != "_"

    if diagonals_1 or diagonals_2 :
        game_is_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]

    return



def check_if_tie():
    return


def flip_player():
    return


play_game()
