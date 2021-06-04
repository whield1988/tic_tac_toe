"""
1. Display a board
2. User can input 1-9
3. Check if the user input is taken, else, ask for another number
4. Add the mark to the board
5. Check if the user wins or tie, else, next player's turn
6. Play again?
"""

board = ['-',' ',' ',' ',' ',' ',' ',' ',' ',' ']
current_player = "Player_1"
player_1_mark, player_2_mark = ("O","X")

def display_board(board):
    print("Game Board      Position Guide")
    print("  " + board[1] + "|" + board[2] + "|" + board[3] + "             1|2|3")
    print("  -----             -----")
    print("  " + board[4] + "|" + board[5] + "|" + board[6] + "             4|5|6")
    print("  -----             -----")
    print("  " + board[7] + "|" + board[8] + "|" + board[9] + "             7|8|9")

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
    if board[1] == board[2] == board[3] == player_1_mark or board[1] == board[2] == board[3] == player_2_mark:
        return True
    if board[4] == board[5] == board[6] == player_1_mark or board[4] == board[5] == board[6] == player_2_mark:
        return True
    if board[7] == board[8] == board[9] == player_1_mark or board[7] == board[8] == board[9] == player_2_mark:
        return True
    if board[1] == board[4] == board[7] == player_1_mark or board[1] == board[4] == board[7] == player_2_mark:
        return True
    if board[2] == board[5] == board[8] == player_1_mark or board[2] == board[5] == board[8] == player_2_mark:
        return True
    if board[3] == board[6] == board[9] == player_1_mark or board[3] == board[6] == board[9] == player_2_mark:
        return True
    if board[1] == board[5] == board[9] == player_1_mark or board[1] == board[5] == board[9] == player_2_mark:
        return True
    if board[3] == board[5] == board[7] == player_1_mark or board[3] == board[5] == board[7] == player_2_mark:
        return True
    else:
        return False

def check_tie():
    if " " not in board:
        return True
    else:
        return False

def replay():
    pass


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

        display_board(board)

        if current_player == 'Player_1':
            ask_player_1_input()
            if check_win() == True:
                display_board(board)
                print(current_player+" wins!")
                game_on = False

            else:
                if check_tie() == True:
                    display_board(board)
                    print("Tie!")
                    game_on = False

                else:
                    current_player = 'Player_2'

        elif current_player == 'Player_2':
            ask_player_2_input()
            if check_win() == True:
                display_board(board)
                print(current_player + " wins!")
                game_on = False

            else:
                if check_tie() == True:
                    display_board(board)
                    print("Tie!")
                    game_on = False

                else:
                    current_player = 'Player_1'

start_game()
