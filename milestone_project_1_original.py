"""
A simple Tic-Tac-Toe game.
"""


def display_board():
    """Display board"""
    print("Game board      Position Guide")
    print("  " + BOARD[0] + "|" + BOARD[1] + "|" + BOARD[2] + "             1|2|3")
    print("  -----             -----")
    print("  " + BOARD[3] + "|" + BOARD[4] + "|" + BOARD[5] + "             4|5|6")
    print("  -----             -----")
    print("  " + BOARD[6] + "|" + BOARD[7] + "|" + BOARD[8] + "             7|8|9")


def handle_turn():
    """Ask for player's input and place the mark on the board"""
    while True:
        try:
            print(CURRENT_PLAYER + "'s turn.")
            position = int(input("Choose a number from 1-9: "))
            index = int(position) - 1
            if 0 > int(index) <= 8:
                raise Exception("Please enter a number from 1-9 only.")
            elif BOARD[index] != ' ':
                raise Exception("Please enter a number in an empty space only.")
        except ValueError:
            print("Please enter numbers only.")
        except Exception as e:
            print(e)
        else:
            BOARD[index] = CURRENT_PLAYER
            display_board()
            break


def check_if_win():
    """Check if there is a win"""
    # Check rows
    if BOARD[0] == BOARD[1] == BOARD[2] != ' ':
        return True
    elif BOARD[3] == BOARD[4] == BOARD[5] != ' ':
        return True
    elif BOARD[6] == BOARD[7] == BOARD[8] != ' ':
        return True
    # Check columns
    elif BOARD[0] == BOARD[3] == BOARD[6] != ' ':
        return True
    elif BOARD[1] == BOARD[4] == BOARD[7] != ' ':
        return True
    elif BOARD[2] == BOARD[5] == BOARD[8] != ' ':
        return True
    # Check diagonals
    elif BOARD[0] == BOARD[4] == BOARD[8] != ' ':
        return True
    elif BOARD[2] == BOARD[4] == BOARD[6] != ' ':
        return True
    else:
        return False


def check_if_tie():
    """Check if there is a tie"""
    if ' ' not in BOARD:
        return True


def flip_player():
    """Change between players when there is no win or tie"""
    global CURRENT_PLAYER

    if CURRENT_PLAYER == 'X':
        CURRENT_PLAYER = 'O'

    elif CURRENT_PLAYER == 'O':
        CURRENT_PLAYER = 'X'


if __name__ == "__main__":

    BOARD = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']

    CURRENT_PLAYER = "X"

    display_board()

    game_on = True

    while game_on:
        handle_turn()

        if check_if_win():
            game_on = False
            print(CURRENT_PLAYER + " won!")
        elif check_if_tie():
            game_on = False
            print("Tie!")
        else:
            flip_player()
