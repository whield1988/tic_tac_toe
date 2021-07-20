"""
A simple Tic-Tac-Toe game.
"""

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

current_player = "X"

game_on = True

winner = " "


def display_board():
    print("Game Board      Position Guide")
    print("  " + board[0] + "|" + board[1] + "|" + board[2] + "             1|2|3")
    print("  -----             -----")
    print("  " + board[3] + "|" + board[4] + "|" + board[5] + "             4|5|6")
    print("  -----             -----")
    print("  " + board[6] + "|" + board[7] + "|" + board[8] + "             7|8|9")


def handle_turn():
    print(current_player + "'s turn!")
    position = int(input("Choose a position from 1-9: "))

    position_valid = False
    while not position_valid:
        while position not in range(1, 10):
            position = int(input("Invalid number, please try again: "))

        position = int(position) - 1

        if board[position] == ' ':
            position_valid = True
        else:
            print("Position taken! Choose another one.")

    board[position] = current_player

    display_board()


def check_win():
    global winner
    # Check rows
    if board[0] == board[1] == board[2] != ' ':
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] != ' ':
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] != ' ':
        winner = board[6]
        return True
    # Check columns
    if board[0] == board[3] == board[6] != ' ':
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] != ' ':
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] != ' ':
        winner = board[2]
        return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != ' ':
        winner = board[2]
        return True
    return False


def check_tie():
    if ' ' not in board:
        return True


def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'

    elif current_player == 'O':
        current_player = 'X'


if __name__ == "__main__":
    display_board()

    while game_on:
        handle_turn()

        if check_if_win():
            game_on = False
            print(winner + " won.")

        elif check_if_tie():
            game_on = False
            print("Tie.")

        else:
            flip_player()
