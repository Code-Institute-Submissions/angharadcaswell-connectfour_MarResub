# CONNECT FOUR
![Mock up of home](readmeimages/homescreen.png)

[Link to LIVE game](https://connect-four-by-ange.herokuapp.com//)

# 1. Project Goals
Two players to be able to play Connect Four and for there to be one winner. The game is to be played in the Python Terminal and hosted on Heroku. 

The aim of the game is to be the first to get 4 pieces in a row. The pieces can be horizontal, vertical or diagonal. 

##  How to play:
1. Each player enters their name.
2. Player one selects a coloum (0-6) on the board to drop a piece. 
3. The piece will be marked on the board with a "1" or "2" depending on which player's turn it is. 
4. You can not add a piece to a full column. 
5. The players take it in turns to drop their pieces. 
6. The first player to get four in a row wins!!!

[Read more about the physical game](https://en.wikipedia.org/wiki/Connect_Four)


# 2. User Experience

## 2.1 User Stories 
1. As a user, I want to be able to play a digital version of Connect Four. 
2. As a user, I want instructions on how to play the game.
3. As a user, I want to feel excited to play when I start the game.
4. As a user, I need it to be clear whose turn is next. 
5. As a user, I want to celebrate if I win. 
6. As a user, I want the option to restart or quit the game easily when the game is over. 
7. As a user, I want to know if I have made an error and recieve feedback on how to correct this. 
8. As a user, I want the game to be easy to navigate and play. 
9. As a user, I want to know who has won the game. 

# 3. Features

## 3.1 All features

1. Welcome page:
![welcome page](readmeimages/welcome.png)
- Welcomes the players and asks for their names.

2. Instructions & first go:
![instructions page](readmeimages/instructions.png)
- Give instructions on ho to play Connect four to the players. 
- Print the board for the first player to use. 
- Ask the first player for their selection. They can choose a column from 0 to 6.
- The player needs to type the number into the terminal.

3. Players turn:
![piece drop](readmeimages/piecedrop.png)
- The players take it in turns to drop their pieces. 
- As you can see in the image above, Ange's pieces are "1" and Tom's pieces are "2".

4. Player wins:
![win](readmeimages/win.png)
- When a player gets 4 pieces in a row the game is over. 
- The terminal prints who the winner is.
- The terminal asks the players if they would like to play again. 
- If they select Y it will take them to the start. 
- If they select N it will thank them for playing. 


## 3.2 Features to implement:
1. Play agianst the computer
2. Users to recieve a message if the game is a draw. 
3. Score Board. 
4. Colour markers for players.



# 4. Technologies used 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Content and structure
* [Heroku](https://id.heroku.com/login) - Host
* [Gitpod](https://www.gitpod.io/) - Coding workspace
* [Github/ Github pages](https://github.com/)- Commit my code
* [Am I responsive?](http://ami.responsivedesign.is/#)- To see display the website as mock ups  
* [NumPy](https://numpy.org/) - To create a matrix for the board. 
* [termcolor](https://pypi.org/project/termcolor/) - To change the colors of the error messages and the welcome/end message. 



# 5. Testing  
The game was tested in Gitpod terminal and Heroku by users and myself. The game was also peer reviewed by the Code Institute community. 

## 5.1 Bugs
I discovered several bugs whilst building and testing the game. The following bugs were significant in fixing:

- Winning_move function was not being called correctly after previously working.
- **Solution: Moved the winning_move function call inside the if statement to check the validation of the input.**

- Changing the winning_move function meant the continue game function didn't reset properly.
- **Solution: I added game_over = False to reset the game.**

## 5.2 User testing:
The following issues were discovered during user testing. Users were asked to play the game and also to make intentional mistakes to help check for errors.
- If a user inputed a lowercase y when asked if they would like to play again, the command was not understood and the game would not restart.
- **Solution: I added .lower() function to their input and lowercase y to the if statement so it no longer mattered how the user entered y and game would restart as requested.**

- User suggested different error message for non int values inputted as it was currently quite techy language.
- **Solution: Changed the error message to "You must choose a number (0,1,2,3,4,5,6)! Please try again."**

- A user noticed you can input an empty username. This caused issues for players to be able to see whose turn it was.
- **Solution: Added if statement to check the username uses letter and wasn't empty**

[User Stories Tested](userstories.md)

## 5.3 Code Validation
- Used [PEP8 Python Validator](http://pep8online.com/) to check Python content.
![PEP8 Validator](readmeimages/pep.png)

## 5.4 Testing error messages 
I tested my error messages were showing correctly for validating user inputs. I also wanted to make sure that the flow of the game wasn't disrupted. I checked for the following:
- If a user inputed something other than an interger.
- If a user tried to add a counter to a full column. 
- If a user inputed a number outside of (0,1,2,3,4,5,6)


# 6. Deployment

Steps for deployment:
1. Clone this repository in Github
2. Create [Heroku](https://dashboard.heroku.com/apps) app
3. Under settings tab, add Python and Node.js buildpacks in this order
4. Under settings tab, add PORT and 8000 to config vars.
5. Under deploy tab, link the Heroku app to this repository.
6. Deploy app



# 7. Credits

* Keith Galli - Code to check if player has won. 

## Acknowledgments:
* My mentor [Precious](https://www.linkedin.com/in/precious-ijege-908a00168/?originalSubdomain=ng) for your help and guidance. 
* [Code Institute](https://codeinstitute.net/) student support, slack community and tutorials. 