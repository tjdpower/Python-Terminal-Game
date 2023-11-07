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
# red_player = input("Who will play the red pieces?: ")
# black_player = input("Who will play the black pieces?: ")

#print("Thank you " + red_player + " and " + black_player + ", let's begin!")

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

#Building game board
header_string = "    "
for a in range(1,9):
      header_string += str(a) + "     "
header_string += "   "
vertical_border = " " + str("+-----" * 8) + "+"

odd_rows = str("|# # #|     " * 4) + "|"
even_rows = str("|     |# # #" * 4) + "|"

board.append(header_string)
board.append(vertical_border)
for b in range(8):
      if b%2 == 0:
            board.append(" " + odd_rows)
            board.append(str(b+1) + odd_rows)
            board.append(" " + odd_rows)
      else:
            board.append(" " + even_rows)
            board.append(str(b+1) + even_rows)
            board.append(" " + even_rows)
      board.append(vertical_border)

#placing red pieces on board
def place_red():
      for d in range(len(Checkers_Piece.red_piece_location_list)):
            temp_string = ""
            location = Checkers_Piece.red_piece_location_list[d]
            if location == "null":
                  temp_string = board[location[0]*3 + location[0] - 1]     
            elif d < 9:
                  temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " R" + str(d+1) + "  " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]
            else:
                  temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " R" + str(d+1) + " " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]      
            board[location[0]*3 + location[0] - 1] = temp_string

place_red()

#Placing black pieces on board
def place_black():
      for e in range(len(Checkers_Piece.black_piece_location_list)):
            temp_string = ""
            location = Checkers_Piece.black_piece_location_list[e]
            if location == "null":
                  temp_string = board[location[0]*3 + location[0] - 1]     
            elif e < 9:
                  temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " B" + str(e+1) + "  " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]
            else:
                  temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " B" + str(e+1) + " " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]      
            board[location[0]*3 + location[0] - 1] = temp_string

place_black()

for f in range(len(board)):
      print(board[f])


#for testing
