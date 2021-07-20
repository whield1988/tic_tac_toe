"""
A simple Tic-Tac-Toe game.
"""

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

current_player = "Player_1"

game_on = True

player_1_mark, player_2_mark = ("O","X")

def display_board():
    print("Game Board      Position Guide")
    print("  " + board[0] + "|" + board[1] + "|" + board[2] + "             1|2|3")
    print("  -----             -----")
    print("  " + board[3] + "|" + board[4] + "|" + board[5] + "             4|5|6")
    print("  -----             -----")
    print("  " + board[6] + "|" + board[7] + "|" + board[8] + "             7|8|9")

def ask_player_1_input():
    print("Player_1's turn, your mark is 'X'")
    position = int(input("Please choose a number from 1-9: "))

    while position not in range(1,10) or board[position] == "X" or board[position] == "O":
        position = int(input("Invalid number or placement, please try again: "))

    board[position] = "X"

def ask_player_2_input():
    print("Player_2's turn, your mark is 'O'")
    position = int(input("Please choose a number from 1-9: "))

    while position not in range(1,10) or board[position] == "X" or board[position] == "O":
        position = int(input("Invalid number or placement, please try again: "))

    board[position] = "O"

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


def start_game():

    current_player = 'Player_1'
    play_game = ''

    print("Welcome to the Tic-Tac-Toe game!")
    print("How to play? : Enter numbers from 1-9 to place a mark on the 3x3 board!")
    print("How to win?  : The first player to get 3 mark in a line wins!")
    print(" ")

    while not play_game == 'YES':
        play_game = input('Enter "YES" to start: ').upper()
        if play_game == 'YES':
            game_on = True

    while game_on:

        display_board()

        if current_player == 'Player_1':
            ask_player_1_input()
            if check_win() == True:
                display_board()
                print(current_player+" wins!")
                game_on = False

            else:
                if check_tie() == True:
                    display_board()
                    print("Tie!")
                    game_on = False

                else:
                    current_player = 'Player_2'

        elif current_player == 'Player_2':
            ask_player_2_input()
            if check_win() == True:
                display_board()
                print(current_player + " wins!")
                game_on = False

            else:
                if check_tie() == True:
                    display_board()
                    print("Tie!")
                    game_on = False

                else:
                    current_player = 'Player_1'

start_game()
