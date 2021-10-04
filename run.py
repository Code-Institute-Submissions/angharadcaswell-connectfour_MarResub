import numpy as np

def players_name():
    """
    Function to get players names and print instructions
    """
    player_one = input("Player one, what is your name?\n")
    player_two = input("Player two, what is your name?\n")
    welcome_message = print(f"Welcome {player_one} and {player_two}, lets play Connect Four!\n How to play:\n Take it in turns to add a piece to a column. When you have 4 pieces next to eachtoher you win! \n The pieces can be vertical, horizontal or diagonal. Good luck!" )
    return welcome_message
    
    

players_name()


def create_board():
    """
    Create grid 6x7 
    """
    board = print(np.zeros((6, 7)))
    return board

board = create_board()

game_over = False
turn = 0

while not game_over:
    
        if turn == 0:  
            player_choice_one = int(input("Player One choose a column to drop a piece (0-6):\n"))
            
            if validate_data(player_choice_one):
                print("Data is valid!")
        else:
            player_choice_two = int(input("Player Two choose a column to drop a piece (0-6):\n"))
            if validate_data(player_choice_two):
                print("Data is valid!")

        # turn += 1
        # turn = turn % 2


    # def input_validate:

def validate_data(value):
        try:
            if value > 6:
                raise ValueError
                (
                    f"You can choose a column from 0 and up to 6"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True


    # def win_game:

