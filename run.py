# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def players_name():
    player_one = input("Player one, what is your name?\n")
    player_two = input("Player two, what is your name?\n")
    welcome_message = print("Welcome " + player_one + " and " + player_two + ", lets play Connect Four!\n How to play:\n Take it in turns to add a piece to a column. When you have 4 pieces next to eachtoher you win! \n The pieces can be vertical, horizontal or diagonal. Good luck!" )
    return welcome_message

players_name()

