import numpy as np
import sys
from termcolor import colored, cprint



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
    welcome_message = print(f"Welcome {player_one} and {player_two}, lets play Connect Four!\n\n How to play:\n\n ##Take it in turns to add a piece to a column. When you have 4 pieces next to eachtoher you win! \n\n ##The pieces can be vertical, horizontal or diagonal. \n\n Good luck! \n\n\n\n" )
    return welcome_message



def create_board():
    """
    Create grid 6x7 
    """
    global board
    board = np.zeros((6, 7))
    return board



def start_game():
    open_message()
    players_name()
    create_board()
    print(board)

start_game()



def validate_data(value):
        try:
            int(value)
            if int(value) > 6:
                raise ValueError(f"You can only choose a column from 0 and upto 6")
        except ValueError as e:
            cprint(f"Invalid data: {e}, please try again.\n", 'red')
            return False

        return True

def next_row(board, col): 
        """ looking for the next available row on the column that the user selected. An available row will have a value fo 0 which will be chnaged to the users number"""       
        for row in range(6):
            if board[row][col] == 0:
                return row
        

        
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
                user_choice = input(f"{player_one.capitalize()}, choose a column to drop a piece (0-6):\n")
                col = int(user_choice)
                if validate_data(user_choice):
                    if board[5][col] == 0:
                        row = next_row(board, col)
                        board[row][col] = 1
                        break
                    else:
                         cprint("uh oh! Choose a column that isn't full of pieces", 'red')
                    
                    
                
            else:
                user_choice = input(f"{player_two.capitalize()} choose a column to drop a piece (0-6):\n")
                col = int(user_choice)
                if validate_data(user_choice):
                    if board[5][col] == 0:
                        row = next_row(board, col)
                        board[row][col] = 2
                        break
                    else:
                         cprint("uh oh! Choose a column that isn't full of pieces", 'red')
                    
               
               
    print(np.flip(board, 0))           
    turn += 1
    turn = turn % 2











