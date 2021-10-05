import numpy as np



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
    welcome_message = print(f"Welcome {player_one} and {player_two}, lets play Connect Four!\n\n How to play:\n\n Take it in turns to add a piece to a column. When you have 4 pieces next to eachtoher you win! \n\n The pieces can be vertical, horizontal or diagonal. Good luck!" )
    return welcome_message



def create_board():
    """
    Create grid 6x7 
    """
    board = print(np.zeros((6, 7)))
    return board


def start_game():
    players_name()
    create_board()

start_game()

def validate_data(value):
        try:
            int(value)
            if int(value) > 6:
                raise ValueError(f"You can only choose a column from 0 and upto 6")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True
           

game_over = False
turn = 0

while not game_over:
    """
    Ask user 1 and 2 for the choice. Send the values to the validate function to check they are valid.
    """
    while True:
            if turn == 0:  
                player_choice_one = input(f"{player_one}, choose a column to drop a piece (0-6):\n")
                if validate_data(player_choice_one):
                    break
                    
                
            else:
                player_choice_two = input(f"{player_two} choose a column to drop a piece (0-6):\n")
                if validate_data(player_choice_two):
                    break
                    
                
    turn += 1
    turn = turn % 2



