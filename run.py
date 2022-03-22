import numpy as np
import sys
from termcolor import colored, cprint

ROW_NUM = 6
COL_NUM = 7


def open_message():
    cprint("#######################################", 'blue')
    print("#                                     #")
    print("#  W E L C O M E  T O  C O N N E C T  #")
    print("#                                     #")
    print("#              **                     #")
    print("#              **                     #")
    print("#              **    **               #")
    print("#              **    **               #")
    print("#              **************         #")
    print("#              **************         #")
    print("#                    **               #")
    print("#                    **               #")
    print("#                                     #")
    cprint("#######################################", 'blue')


def players_name():
    """
    Function to get players names and print instructions
    """
    global player_one
    player_one = input("Player one, what is your name?\n")
    print("-" * 40)
    global player_two
    player_two = input("Player two, what is your name?\n")
    print("-" * 40)
    welcome_message = print(f"Welcome {player_one} and {player_two},"
                            "lets play Connect Four!"
                            " \n\n How to play:\n\n ##Take it in turns to add"
                            " a piece to a column. \n When you have 4 pieces"
                            " next to each other you win!"
                            " \n\n ##The pieces can be vertical, horizontal"
                            " or diagonal.\n\n Good luck! \n\n\n\n")
    return welcome_message


def create_board():
    """
    Create grid 6x7
    """
    global board
    board = np.zeros((ROW_NUM, COL_NUM))
    return board


def start_game():
    open_message()
    players_name()
    create_board()
    print(board)

start_game()


def validate_data(value):
    """ Validate data by checking for interger and number <= 6"""
    try:
        int(value)
        if int(value) > 6:
            raise ValueError(f"You can only choose a "
                             "column from 0 and upto 6")
    except ValueError as e:
        cprint(f"Invalid data: {e}, please try again.\n", 'red')
        return False

    return True


def next_row(board, col):
    """ looking for the next available row on the column "
        "that the user selected. An available row will "
        "have a value fo 0 which will be changed to the users number"""
    for row in range(ROW_NUM):
        if board[row][col] == 0:
            return row


def winning_move(board, piece):
    """ Credit for code: Keith Galli - Youtube """
    """ Check horizontal locations for win"""
    for c in range(COL_NUM-3):
        for r in range(ROW_NUM):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    """ Check vertical locations for win """
    for c in range(COL_NUM):
        for r in range(ROW_NUM-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    """ Check positively sloped diaganols """
    for c in range(COL_NUM-3):
        for r in range(ROW_NUM-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    """ Check negatively sloped diaganols """
    for c in range(COL_NUM-3):
        for r in range(3, ROW_NUM):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


""" End of Youtube Code """
game_over = False
turn = 0

while not game_over:
    """
    Ask user 1 and 2 for the choice. Send the values to the validate function to check they are valid.
    Check the colum selected still has a 0 at the top and is therefore not full of pieces.
    Link to new row function to find the next available row for the user to place a piece.
    """
    while True:
        if turn == 0:
            user_choice = input(
                f"{player_one.capitalize()}, choose a column to drop a piece (0-6):\n")
            if validate_data(user_choice):
                col = int(user_choice)
                if board[5][col] == 0:
                    row = next_row(board, col)
                    board[row][col] = 1
                    print(np.flip(board, 0))
                    winning_move(board, 1)
                    if winning_move(board, 1):
                        cprint(f"{player_one.capitalize()} wins!!!!", "green")
                        cprint(f"{player_two.capitalize()} unlucky!!!!", "red")
                        game_over = True
                    break
                else:
                    cprint("uh oh! Choose a column that isn't full of pieces", "red")

        else:
            user_choice = input(
                f"{player_two.capitalize()} choose a column to drop a piece (0-6):\n")
            if validate_data(user_choice):
                col = int(user_choice)
                if board[ROW_NUM-1][col] == 0:
                    row = next_row(board, col)
                    board[row][col] = 2
                    print(np.flip(board, 0))
                    winning_move(board, 2)
                    if winning_move(board, 2):
                        cprint(f"{player_two.capitalize()} wins!!!!", "green")
                        cprint(f"Unlucky, {player_one.capitalize()}!!!", "red")
                        game_over = True
                    break
                else:
                    cprint("uh oh! Choose a column that "
                           "isn't full of pieces", 'red')

    turn += 1
    turn = turn % 2
    if game_over:
        cprint("*************************", 'yellow')
        cprint("*************************", 'yellow')
        cprint("   G A M E    O V E R", 'yellow')
        cprint("*************************", 'yellow')
        cprint("*************************", 'yellow')
        continue_game = input("Would you like to play again? Y/N \n")
        if continue_game == "Y":
            game_over = False
            start_game()
        else:
            print("Thank you for playing!")
