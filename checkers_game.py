#Main file for checkers game

from checkers_class import Checkers_Piece
import ast

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

def update_board(piece, old_location, new_location):
      temp_string_old = ""
      temp_string_new = ""
      
      piece_number = int(piece[1:])

      if piece_number <= 9:
            temp_string_new = board[new_location[0]*3 + new_location[0] - 1][:((new_location[1]*2 - 1) * 3)-1] + " " + piece[0] + str(piece_number) + "  " + board[new_location[0]*3 + new_location[0] - 1][((new_location[1]*2 - 1) * 3)+4:]
      else:
            temp_string_new = board[new_location[0]*3 + new_location[0] - 1][:((new_location[1]*2 - 1) * 3)-1] + " " + piece[0] + str(piece_number) + " " + board[new_location[0]*3 + new_location[0] - 1][((new_location[1]*2 - 1) * 3)+4:]      
      board[new_location[0]*3 + new_location[0] - 1] = temp_string_new

      temp_string_old = board[old_location[0]*3 + old_location[0] - 1][:((old_location[1]*2 - 1) * 3)-1] + "# # #" + board[old_location[0]*3 + old_location[0] - 1][((old_location[1]*2 - 1) * 3)+4:]
      board[old_location[0]*3 + old_location[0] - 1] = temp_string_old

      for g in range(len(board)):
            print(board[g])

#begin playing the game
print("The black pieces get to start, so " + black_player + " will go first.")

turn_count = 0

while (Checkers_Piece.black_piece_count != 0 and Checkers_Piece.red_piece_count != 0):
      pieces_to_jump = []
      if turn_count % 2 == 0:
            piece_to_move = input(black_player + ", which piece would you like to move? (B1, B2,...):  ")
            where_to_move = ast.literal_eval(input("Where would you like to move to? eg.(4,5):  "))
            is_jump = input("Are you jumping an opponent's piece? (y/n):  ")
            if is_jump == "y":
                  multi_jump = input("Are you jumping more than one piece? (y/n):  ")
                  if multi_jump == "y":
                        jump_count = input("How many jumps are you making?:  ")
                        for i in range(jump_count):
                              pieces_to_jump.append(input("Name a piece you are jumping (R1, R2, ...):  "))
                  else:
                        pieces_to_jump.append(input("Name the piece you are jumping (R1, R2, ...):  "))


            piece_number = int(piece_to_move[1:])
            current_location = Checkers_Piece.black_piece_location_list[piece_number-1]
            
            
            #need to identify status of checker piece being moved
            if piece_to_move == "B1":
                  king_status = B1.king
            elif piece_to_move == "B2":
                  king_status = B2.king
            elif piece_to_move == "B3":
                  king_status = B3.king
            elif piece_to_move =="B4":
                  king_status = B4.king
            elif piece_to_move == "B5":
                  king_status = B5.king
            elif piece_to_move == "B6":
                  king_status = B6.king
            elif piece_to_move == "B7":
                  king_status = B7.king
            elif piece_to_move == "B8":
                  king_status = B8.king
            elif piece_to_move == "B9":
                  king_status = B9.king
            elif piece_to_move == "B10":
                  king_status = B10.king
            elif piece_to_move == "B11":
                  king_status = B11.king
            else:
                  king_status = B12.king
            
            #movement direction
            if abs(int(where_to_move[1]) - int(current_location[1])) != 1 and is_jump == "n":
                  print("Sorry, that is not a valid move. Please try again.")
            else:
                  if (int(where_to_move[0]) - int(current_location[0]) > 0):
                        movement_direction = "down"
                  else:
                        movement_direction = "up"

            #Black pieces where king = False can only move "down" on the board and cannot be where there is already a piece, check if move is valid
            if (where_to_move in Checkers_Piece.black_piece_location_list or where_to_move in Checkers_Piece.red_piece_location_list or (movement_direction == "up" and not king_status)):
                  print("Sorry, that is not a valid move. Please try again.")
            elif movement_direction == "down" and is_jump == "y":
                  for piece in pieces_to_jump:                    #need to find a way to simplify all these if statements
                        if piece_to_move == "B1":
                              if piece == "R1":
                                    B1.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B1.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B1.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B1.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B1.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B1.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B1.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B1.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B1.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B1.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B1.jump_enemy(R11, where_to_move)
                              else:
                                    B1.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B2":
                              if piece == "R1":
                                    B2.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B2.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B2.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B2.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B2.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B2.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B2.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B2.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B2.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B2.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B2.jump_enemy(R11, where_to_move)
                              else:
                                    B2.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B3":
                              if piece == "R1":
                                    B3.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B3.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B3.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B3.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B3.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B3.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B3.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B3.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B3.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B3.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B3.jump_enemy(R11, where_to_move)
                              else:
                                    B3.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B4":
                              if piece == "R1":
                                    B4.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B4.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B4.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B4.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B4.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B4.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B4.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B4.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B4.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B4.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B4.jump_enemy(R11, where_to_move)
                              else:
                                    B4.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B5":
                              if piece == "R1":
                                    B5.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B5.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B5.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B5.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B5.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B5.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B5.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B5.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B5.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B5.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B5.jump_enemy(R11, where_to_move)
                              else:
                                    B5.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B6":
                              if piece == "R1":
                                    B6.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B6.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B6.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B6.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B6.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B6.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B6.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B6.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B6.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B6.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B6.jump_enemy(R11, where_to_move)
                              else:
                                    B6.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B7":
                              if piece == "R1":
                                    B7.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B7.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B7.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B7.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B7.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B7.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B7.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B7.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B7.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B7.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B7.jump_enemy(R11, where_to_move)
                              else:
                                    B7.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B8":
                              if piece == "R1":
                                    B8.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B8.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B8.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B8.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B8.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B8.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B8.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B8.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B8.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B8.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B8.jump_enemy(R11, where_to_move)
                              else:
                                    B8.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B9":
                              if piece == "R1":
                                    B9.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B9.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B9.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B9.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B9.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B9.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B9.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B9.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B9.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B9.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B9.jump_enemy(R11, where_to_move)
                              else:
                                    B9.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B10":
                              if piece == "R1":
                                    B10.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B10.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B10.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B10.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B10.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B10.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B10.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B10.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B10.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B10.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B10.jump_enemy(R11, where_to_move)
                              else:
                                    B10.jump_enemy(R12, where_to_move)
                        elif piece_to_move == "B11":
                              if piece == "R1":
                                    B11.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B11.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B11.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B11.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B11.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B11.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B11.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B11.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B11.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B11.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B11.jump_enemy(R11, where_to_move)
                              else:
                                    B11.jump_enemy(R12, where_to_move)
                        else:
                              if piece == "R1":
                                    B12.jump_enemy(R1, where_to_move)
                              elif piece == "R2":
                                    B12.jump_enemy(R2, where_to_move)
                              elif piece == "R3":
                                    B12.jump_enemy(R3, where_to_move)
                              elif piece == "R4":
                                    B12.jump_enemy(R4, where_to_move)
                              elif piece == "R5":
                                    B12.jump_enemy(R5, where_to_move)
                              elif piece == "R6":
                                    B12.jump_enemy(R6, where_to_move)
                              elif piece == "R7":
                                    B12.jump_enemy(R7, where_to_move)
                              elif piece == "R8":
                                    B12.jump_enemy(R8, where_to_move)
                              elif piece == "R9":
                                    B12.jump_enemy(R9, where_to_move)
                              elif piece == "R10":
                                    B12.jump_enemy(R10, where_to_move)
                              elif piece == "R11":
                                    B12.jump_enemy(R11, where_to_move)
                              else:
                                    B12.jump_enemy(R12, where_to_move)
            elif movement_direction == "down":
                  if piece_to_move == "B1":
                        B1.move_piece(where_to_move)
                  elif piece_to_move == "B2":
                        B2.move_piece(where_to_move)
                  elif piece_to_move == "B3":
                        B3.move_piece(where_to_move)
                  elif piece_to_move == "B4":
                        B4.move_piece(where_to_move)
                  elif piece_to_move == "B5":
                        B5.move_piece(where_to_move)
                  elif piece_to_move == "B6":
                        B6.move_piece(where_to_move)
                  elif piece_to_move == "B7":
                        B7.move_piece(where_to_move)
                  elif piece_to_move == "B8":
                        B8.move_piece(where_to_move)
                  elif piece_to_move == "B9":
                        B9.move_piece(where_to_move)
                  elif piece_to_move == "B10":
                        B10.move_piece(where_to_move)
                  elif piece_to_move == "B11":
                        B11.move_piece(where_to_move)
                  else:
                        B12.move_piece(where_to_move)
            else:
                  print("Something went wrong. Please try again.")

            update_board(piece_to_move, current_location, where_to_move)
            turn_count += 1
      #Red player's turn      
      else:
            piece_to_move = input(red_player + ", which piece would you like to move? (R1, R2,...):  ")
            where_to_move = ast.literal_eval(input("Where would you like to move to? eg.(4,5):  "))
            is_jump = input("Are you jumping an opponent's piece? (y/n):  ")
            if is_jump == "y":
                  multi_jump = input("Are you jumping more than one piece? (y/n):  ")
                  if multi_jump == "y":
                        jump_count = input("How many jumps are you making?:  ")
                        for i in range(jump_count):
                              pieces_to_jump.append(input("Name a piece you are jumping (B1, B2, ...):  "))
                  else:
                        pieces_to_jump.append(input("Name the piece you are jumping (B1, B2, ...):  "))

            
            piece_number = int(piece_to_move[1:])
            current_location = Checkers_Piece.red_piece_location_list[piece_number-1]
            
            print(current_location)
            #need to identify which checker piece is being moved
            if piece_to_move == "R1":
                  king_status = R1.king
            elif piece_to_move == "R2":
                  king_status = R2.king
            elif piece_to_move == "R3":
                  king_status = R3.king
            elif piece_to_move =="R4":
                  king_status = R4.king
            elif piece_to_move == "R5":
                  king_status = R5.king
            elif piece_to_move == "R6":
                  king_status = R6.king
            elif piece_to_move == "R7":
                  king_status = R7.king
            elif piece_to_move == "R8":
                  king_status = R8.king
            elif piece_to_move == "R9":
                  king_status = R9.king
            elif piece_to_move == "R10":
                  king_status = R10.king
            elif piece_to_move == "R11":
                  king_status = R11.king
            else:
                  king_status = R12.king
            
            #movement direction
            if abs(int(where_to_move[1]) - int(current_location[1])) != 1:
                  print("Sorry, that is not a valid move. Please try again.")
            else:
                  if (int(where_to_move[0]) - int(current_location[0]) > 0):
                        movement_direction = "down"
                  else:
                        movement_direction = "up"

            #Red pieces where king = False can only move "up" on the board and cannot be where there is already a piece, check if move is valid
            if (where_to_move in Checkers_Piece.black_piece_location_list or where_to_move in Checkers_Piece.red_piece_location_list or (movement_direction == "down" and not king_status)):
                  print("Sorry, that is not a valid move. Please try again.")
            elif movement_direction == "up":
                  if piece_to_move == "R1":
                        R1.move_piece(where_to_move)
                  elif piece_to_move == "R2":
                        R2.move_piece(where_to_move)
                  elif piece_to_move == "R3":
                        R3.move_piece(where_to_move)
                  elif piece_to_move == "R4":
                        R4.move_piece(where_to_move)
                  elif piece_to_move == "R5":
                        R5.move_piece(where_to_move)
                  elif piece_to_move == "R6":
                        R6.move_piece(where_to_move)
                  elif piece_to_move == "R7":
                        R7.move_piece(where_to_move)
                  elif piece_to_move == "R8":
                        R8.move_piece(where_to_move)
                  elif piece_to_move == "R9":
                        R9.move_piece(where_to_move)
                  elif piece_to_move == "R10":
                        R10.move_piece(where_to_move)
                  elif piece_to_move == "R11":
                        R11.move_piece(where_to_move)
                  else:
                        R12.move_piece(where_to_move)
                  
                  update_board(piece_to_move, current_location, where_to_move)
                  turn_count += 1

