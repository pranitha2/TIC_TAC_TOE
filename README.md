
# TIC_TAC_TOE:

This Repository contains Source CODE of Tic Tac Toe Game in Python

## Requirements:

To Run the Source Code of Tic Tac Toe Game you would need Python3 Installed in our computer

## Instructions for the game:
    
	
	1: YOU CAN MAKE YOUR MOVE BY ENTERING A NUMBER IN BETWEEN 0-8. 
	2: THE NUMBER WILL CORRESPOND TO THE BOARD POSITION AS ILLUSTRATED.


                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

	3: CONDITION OF WINNING THE GAME:
	   WINNER WILL BE DECIDED ON THE BASIS OF WHOEVER SO FIRST FILL THEIR RESPECTIVE SIGN ON THE BOARD'S POSITION
	   THREE CONSECUTIVE IN ROW OR COLUMN OR EITHER IN DIAGONAL.
	4: PLAY YOUR WITH YOUR BEST MOVES.

   
   ## Functions used in source code:
   
 **1.def instructions():** -  This function displays the set of instructions after starting the game.
   
 **2.def display_board():** - This function will help in displaying the board of tic tac toe in instructions as well as after choosing user  and computer choice.
   
 **3.def choose_player():** -This helps in choosing the character of user which they want to pick in 'x' or 'o' with in a range of 0-8. And also check that given input is valid or not and asks to enter a valid choice if the character is other than 'x' or'o'
   
 **4.def choose_computer():** -After the player choice computer will automatically choose the move and displays the board.
  
**5.def win_vertical():** - This function checks the vertical columns of the board and returns who won the game either computer or player.
 
**6. def win_horizontal():** -This function checks the horizontal rows of the board and returns who won the game either computer or player.
   
**7. def win_diagonal():** -This function checks the diagonals of  board and returns who won the game either computer or player.
   
**8.def main_tic_tac_toe():** -This is main function of the code, under this main block there are many functions in it.


