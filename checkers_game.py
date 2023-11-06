#Main file for checkers game

from checkers_class import Checkers_Piece

turn = 0
board = []

#Welcome screen and initial inputs
print("""
      *****  *   *  *****  *****  *    *  *****  ****   *****
      *      *   *  *      *      *   *   *      *   *  *
      *      *****  ***    *      * *     ***    ****   *****
      *      *   *  *      *      *   *   *      *  *       *
      *****  *   *  *****  *****  *    *  *****  *   *  *****
      =======================================================
      """)
print("Welcome to a classic two-player game of checkers.")

#get input for player names
red_player = input("Who will play the red pieces?: ")
black_player = input("Who will play the black pieces?: ")

print("Thank you " + red_player + " and " + black_player + ", let's begin!")

#initialize pieces
B1 = Checkers_Piece("Black1", "black", (1,1))
B2 = Checkers_Piece("Black2", "black", (1,3))
B3 = Checkers_Piece("Black3", "black", (1,5))
B4 = Checkers_Piece("Black4", "black", (1,7))
B5 = Checkers_Piece("Black5", "black", (2,2))
B6 = Checkers_Piece("Black6", "black", (2,4))
B7 = Checkers_Piece("Black7", "black", (2,6))
B8 = Checkers_Piece("Black8", "black", (2,8))
B9 = Checkers_Piece("Black9", "black", (3,1))
B10 = Checkers_Piece("Black10", "black", (3,3))
B11 = Checkers_Piece("Black11", "black", (3,5))
B12 = Checkers_Piece("Black12", "black", (3,7))
R1 = Checkers_Piece("Red1", "red", (8,8))
R2 = Checkers_Piece("Red2", "red", (8,6))
R3 = Checkers_Piece("Red3", "red", (8,4))
R4 = Checkers_Piece("Red4", "red", (8,2))
R5 = Checkers_Piece("Red5", "red", (7,7))
R6 = Checkers_Piece("Red6", "red", (7,5))
R7 = Checkers_Piece("Red7", "red", (7,3))
R8 = Checkers_Piece("Red8", "red", (7,1))
R9 = Checkers_Piece("Red9", "red", (6,8))
R10 = Checkers_Piece("Red10", "red", (6,6))
R11 = Checkers_Piece("Red11", "red", (6,4))
R12 = Checkers_Piece("Red12", "red", (6,2))

board_border = ["+-----"*8 + "+"]
print(board_border)