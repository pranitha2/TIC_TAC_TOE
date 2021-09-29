def instructions():
    print(""" *WELCOME TO THE*
___   _   ___             ___   __    __             ___    ___    ____
/_  _\ / \ /   _/           /_   _\ /  _  \  /  __/           /_   _\  /  __  \  /   ___\  
   / \     | | |  /       __       / \     |  _  | |  /        __      / \     |  /   \  | |   \     
   | |     | | |  \__    \_\     | |     | |  | | |  \_    \__\     | |     |  \_/  | |   /_
   \_/     \_/ \___\               \/     \_/  \_/  \___\               \/      \___/   \____\


    *GAME* CODED BY: ERUDITE					 
    THIS WILL BE A BATTLE BETWEEN A HUMAN MIND AND AN ARTIFICIAL INTELLIGENCE(COMPUTER)	

    INSTRUCTIONS:
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


    """)


instructions()
ttt_Board = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Creating Dummy Board


def display_board(ttt_Board):  # Display board function definition
    print(" ____")
    print("||", ttt_Board[0], "||", ttt_Board[1], "||", ttt_Board[2])
    print(" ____")
    print("||", ttt_Board[3], "||", ttt_Board[4], "||", ttt_Board[5])
    print(" ____")
    print("||", ttt_Board[6], "||", ttt_Board[7], "||", ttt_Board[8])
    print(" ____")


display_board(ttt_Board)


# Chance given to Player to enter the choice
def choose_player(ttt_Board, char):
    valid_move = False
    while (not valid_move):
        choice = int(input("PLAYER: PLEASE SELECT YOUR CHOICE TO MAKE A MOVE ON THE BOARD: \n >> "))
        if choice < 9:
            if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
                ttt_Board[choice] = char
                valid_move = True



            else:
                print("SORRY THE POSTION IS ALREADY OCCUPIED BY :,", ttt_Board[choice])
                print("pls enter the valid move between 0 and 8:")
        else:
            print("pls enter the number within range 0- 8:")
    return win_direction(ttt_Board)

    # Chance given to Computer to enter the choice


import random


def choose_computer(ttt_board, char):
    valid_move = False
    while (not valid_move):
        random.seed()
        choice = random.randint(0, 8)
        if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
            if char.upper() == 'X':
                ttt_Board[choice] = "O"
                print("COMPUTER MADE THE MOVE")
                valid_move = True
            else:
                ttt_Board[choice] = "X"
                print("COMPUTER MADE THE MOVE")
                valid_move = True

    return win_direction(ttt_Board)

    # Deciding the Vertical Winning Conditions


def win_vertical(ttt_board):
    winner = False
    if (ttt_Board[0] == ttt_Board[3] == ttt_Board[6]):
        winner = True
    elif (ttt_Board[1] == ttt_Board[4] == ttt_Board[7]):
        winner = True
    elif (ttt_Board[2] == ttt_Board[5] == ttt_Board[8]):
        winner = True

    return winner

    # Deciding the Horizontal Winning Conditions


def win_horizontal(ttt_board):
    winner = False
    if (ttt_Board[0] == ttt_Board[1] == ttt_Board[2]):
        winner = True
    elif (ttt_Board[3] == ttt_Board[4] == ttt_Board[5]):
        winner = True
    elif (ttt_Board[6] == ttt_Board[7] == ttt_Board[8]):
        winner = True

    return winner

    # Deciding the Diagonal Winning Conditions


def win_diagonal(ttt_board):
    winner = False
    if (ttt_Board[0] == ttt_Board[4] == ttt_Board[8]):
        winner = True
    elif (ttt_Board[2] == ttt_Board[4] == ttt_Board[6]):
        winner = True

    return winner

    # Which Direction you won the game


def win_direction(ttt_board):
    game_winner = False
    if (win_vertical(ttt_board) == True):
        game_winner = True
    elif (win_horizontal(ttt_board) == True):
        game_winner = True
    elif (win_diagonal(ttt_board) == True):
        game_winner = True

    return game_winner

    # DECISION MAKING ON WHO SHOULD START THE GAME


def main_tic_tac_toe():
    start = input("DO YOU LIKE START THE GAME HERE: (Y/N) \n>> ")
    char = input("choose the char u want ' x ' or 'O' ")
    while (char != 'X' or char != 'O'):
        char = input("enter valid choice:")
        char = char.upper()
        if (char == 'X' or char == 'O'):
            break

    if start.upper() == "Y":
        print("GREAT YOU ARE THE ONE WHO IS GOING TO GO FIRST:  ")

    elif start.upper() == "N":
        print("AS YOU DECIDED TO NOT START FIRST, GIVING COMPUTER THE FIRST MOVE:  ")
    turn = 0
    won = False
    while (not won and turn < 9):
        if start.upper() == "Y":
            if turn % 2 == 0:

                won = choose_player(ttt_Board, char)
            else:
                won = choose_computer(ttt_Board, char)
            turn = turn + 1
            display_board(ttt_Board)

    if start.upper() == "N":
        if turn % 2 == 0:
            won = choose_computer(ttt_Board, char)
        else:
            won = choose_player(ttt_Board)

        turn = turn + 1
        display_board(ttt_Board)

    print(turn)
    turn = turn - 1
    if (not won):
        print("HELLO IT IS A TIE!!!")
        n = input("if u want to play again press y else press n:")
        if n.upper() == 'Y':
            main_tic_tac_toe()
        else:
            print("thankyou for playing")

    if start.upper() == "Y":
        if turn % 2 == 0 and (won):
            print("CONGRATULATIONS !!!! YOU WON THE GAME")
            n = input("if u want to play again press y else press n:")
            if n.upper() == 'Y':
                main_tic_tac_toe()
            else:
                print("thankyou for playing")

        elif won:
            print("COMPUTER AGAIN DID IT, AND WON THE GAME")
            if start == "N":
                if turn % 2 == 0 and (won):
                    print("COMPUTER AGAIN DID IT, AND WON THE GAME")
                elif won:
                    print("CONGRATULATIONS !!!! YOU WON THE GAME")
                    n = input("if u want to play again press y else press n:")
                    if n.upper() == 'Y':
                        main_tic_tac_toe()
                    else:
                        print("thankyou for playing")


main_tic_tac_toe()