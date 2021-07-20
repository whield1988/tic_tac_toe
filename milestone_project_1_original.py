"""
A simple Tic-Tac-Toe game.
"""

BOARD = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

CURRENT_PLAYER = "X"

GAME_ON = True

WINNER = " "


def display_board():
    print("Game board      Position Guide")
    print("  " + BOARD[0] + "|" + BOARD[1] + "|" + BOARD[2] + "             1|2|3")
    print("  -----             -----")
    print("  " + BOARD[3] + "|" + BOARD[4] + "|" + BOARD[5] + "             4|5|6")
    print("  -----             -----")
    print("  " + BOARD[6] + "|" + BOARD[7] + "|" + BOARD[8] + "             7|8|9")


def handle_turn():
    print(CURRENT_PLAYER + "'s turn!")
    position = int(input("Choose a position from 1-9: "))

    position_valid = False
    while not position_valid:
        while position not in range(1, 10):
            position = int(input("Invalid number, please try again: "))

        position = int(position) - 1

        if BOARD[position] == ' ':
            position_valid = True
        else:
            print("Position taken! Choose another one.")

    BOARD[position] = CURRENT_PLAYER

    display_board()


def check_if_win():
    global WINNER
    # Check rows
    if BOARD[0] == BOARD[1] == BOARD[2] != ' ':
        WINNER = BOARD[0]
        return True
    if BOARD[3] == BOARD[4] == BOARD[5] != ' ':
        WINNER = BOARD[3]
        return True
    if BOARD[6] == BOARD[7] == BOARD[8] != ' ':
        WINNER = BOARD[6]
        return True
    # Check columns
    if BOARD[0] == BOARD[3] == BOARD[6] != ' ':
        WINNER = BOARD[0]
        return True
    if BOARD[1] == BOARD[4] == BOARD[7] != ' ':
        WINNER = BOARD[1]
        return True
    if BOARD[2] == BOARD[5] == BOARD[8] != ' ':
        WINNER = BOARD[2]
        return True
    # Check diagonals
    if BOARD[0] == BOARD[4] == BOARD[8] != ' ':
        WINNER = BOARD[0]
        return True
    if BOARD[2] == BOARD[4] == BOARD[6] != ' ':
        WINNER = BOARD[2]
        return True
    return False


def check_if_tie():
    if ' ' not in BOARD:
        return True


def flip_player():
    global CURRENT_PLAYER

    if CURRENT_PLAYER == 'X':
        CURRENT_PLAYER = 'O'

    elif CURRENT_PLAYER == 'O':
        CURRENT_PLAYER = 'X'


if __name__ == "__main__":
    display_board()

    while GAME_ON:
        handle_turn()

        if check_if_win():
            GAME_ON = False
            print(WINNER + " won.")

        elif check_if_tie():
            GAME_ON = False
            print("Tie.")

        else:
            flip_player()
