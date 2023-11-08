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
print("To quit at any time, type \"quit\" at the start of your turn")

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

def update_board(piece_moved, old_location, new_location, is_king, pieces_to_jump_location = []):
      temp_string_old = ""
      temp_string_new = ""
      temp_string_jump = ""
      
      piece_number = int(piece_moved[1:])
      
      if len(pieces_to_jump) != 0:

            for jump_location in pieces_to_jump_location:
                  
                  temp_string_jump = board[jump_location[0]*3 + jump_location[0] - 1][:((jump_location[1]*2 - 1) * 3)-1] + "# # #" + board[jump_location[0]*3 + jump_location[0] - 1][((jump_location[1]*2 - 1) * 3)+4:]
                  board[jump_location[0]*3 + jump_location[0] - 1] = temp_string_jump
      if is_king:
            if piece_number <= 9:
                  temp_string_new = board[new_location[0]*3 + new_location[0] - 1][:((new_location[1]*2 - 1) * 3)-1] + " k" + piece_moved[0].upper() + str(piece_number) + " " + board[new_location[0]*3 + new_location[0] - 1][((new_location[1]*2 - 1) * 3)+4:]
            else:
                  temp_string_new = board[new_location[0]*3 + new_location[0] - 1][:((new_location[1]*2 - 1) * 3)-1] + " k" + piece_moved[0].upper() + str(piece_number) + board[new_location[0]*3 + new_location[0] - 1][((new_location[1]*2 - 1) * 3)+4:]      
      elif piece_number <= 9:
            temp_string_new = board[new_location[0]*3 + new_location[0] - 1][:((new_location[1]*2 - 1) * 3)-1] + " " + piece_moved[0].upper() + str(piece_number) + "  " + board[new_location[0]*3 + new_location[0] - 1][((new_location[1]*2 - 1) * 3)+4:]
      else:
            temp_string_new = board[new_location[0]*3 + new_location[0] - 1][:((new_location[1]*2 - 1) * 3)-1] + " " + piece_moved[0].upper() + str(piece_number) + " " + board[new_location[0]*3 + new_location[0] - 1][((new_location[1]*2 - 1) * 3)+4:]      
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
            try:
                  piece_to_move = input(black_player + ", which piece would you like to move? (B1, B2,...):  ")
                  where_to_move = ast.literal_eval(input("Where would you like to move to? eg.(4,5):  "))
                  is_jump = input("Are you jumping an opponent's piece? (y/n):  ")
                  if is_jump == "y":
                        multi_jump = input("Are you jumping more than one piece? (y/n):  ")
                        if multi_jump == "y":
                              jump_count = input("How many jumps are you making?:  ")
                              for i in range(int(jump_count)):
                                    pieces_to_jump.append(input("Name a piece you are jumping (R1, R2, ...):  "))
                        else:
                              pieces_to_jump.append(input("Name the piece you are jumping (R1, R2, ...):  "))
            except:
                  print("It looks like something was entered incorrectly. Try again!")
            else:
                  if piece_to_move == "quit":
                        break
                  
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
                        elif movement_direction == ("down" or (movement_direction == "up" and king_status)) and is_jump == "y":
                              pieces_to_jump_location = []
                              for piece in pieces_to_jump:                    #need to find a way to simplify all these if statements
                                    if piece_to_move == "B1":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B1.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B1.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B1.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B1.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B1.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B1.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B1.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B1.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B1.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B1.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B1.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B1.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B2":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B2.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B2.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B2.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B2.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B2.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B2.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B2.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B2.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B2.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B2.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B2.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B2.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B3":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B3.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B3.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B3.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B3.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B3.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B3.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B3.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B3.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B3.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B3.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B3.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B3.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B4":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B4.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B4.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B4.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B4.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B4.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B4.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B4.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B4.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B4.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B4.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B4.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B4.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B5":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B5.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B5.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B5.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B5.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B5.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B5.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B5.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B5.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B5.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B5.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B5.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B5.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B6":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B6.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B6.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B6.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B6.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B6.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B6.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B6.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B6.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B6.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B6.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B6.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B6.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B7":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B7.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B7.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B7.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B7.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B7.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B7.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B7.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B7.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B7.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B7.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B7.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B7.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B8":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B8.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B8.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B8.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B8.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B8.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B8.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B8.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B8.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B8.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B8.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B8.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B8.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B9":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B9.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B9.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B9.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B9.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B9.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B9.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B9.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B9.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B9.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B9.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B9.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B9.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B10":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B10.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B10.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B10.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B10.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B10.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B10.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B10.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B10.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B10.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B10.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B10.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B10.jump_enemy(R12, where_to_move)
                                    elif piece_to_move == "B11":
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B11.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B11.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B11.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B11.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B11.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B11.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B11.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B11.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B11.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B11.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B11.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B11.jump_enemy(R12, where_to_move)
                                    else:
                                          if piece == "R1":
                                                pieces_to_jump_location.append(R1.location)
                                                B12.jump_enemy(R1, where_to_move)
                                          elif piece == "R2":
                                                pieces_to_jump_location.append(R2.location)
                                                B12.jump_enemy(R2, where_to_move)
                                          elif piece == "R3":
                                                pieces_to_jump_location.append(R3.location)
                                                B12.jump_enemy(R3, where_to_move)
                                          elif piece == "R4":
                                                pieces_to_jump_location.append(R4.location)
                                                B12.jump_enemy(R4, where_to_move)
                                          elif piece == "R5":
                                                pieces_to_jump_location.append(R5.location)
                                                B12.jump_enemy(R5, where_to_move)
                                          elif piece == "R6":
                                                pieces_to_jump_location.append(R6.location)
                                                B12.jump_enemy(R6, where_to_move)
                                          elif piece == "R7":
                                                pieces_to_jump_location.append(R7.location)
                                                B12.jump_enemy(R7, where_to_move)
                                          elif piece == "R8":
                                                pieces_to_jump_location.append(R8.location)
                                                B12.jump_enemy(R8, where_to_move)
                                          elif piece == "R9":
                                                pieces_to_jump_location.append(R9.location)
                                                B12.jump_enemy(R9, where_to_move)
                                          elif piece == "R10":
                                                pieces_to_jump_location.append(R10.location)
                                                B12.jump_enemy(R10, where_to_move)
                                          elif piece == "R11":
                                                pieces_to_jump_location.append(R11.location)
                                                B12.jump_enemy(R11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(R12.location)
                                                B12.jump_enemy(R12, where_to_move)
                        elif movement_direction == "down" or (movement_direction == "up" and king_status):
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
                        
                        if where_to_move[0] == 8:
                              print("Congratulations! You have gotten your piece to the far side of the board. It is now a king and can move in any direction.")
                              if piece_to_move == "B1":
                                    B1.king = True
                              elif piece_to_move == "B2":
                                    B2.king = True
                              elif piece_to_move == "B3":
                                    B3.king = True
                              elif piece_to_move == "B4":
                                    B4.king = True
                              elif piece_to_move == "B5":
                                    B5.king = True
                              elif piece_to_move == "B6":
                                    B6.king = True
                              elif piece_to_move == "B7":
                                    B7.king = True
                              elif piece_to_move == "B8":
                                    B8.king = True
                              elif piece_to_move == "B9":
                                    B9.king = True
                              elif piece_to_move == "B10":
                                    B10.king = True
                              elif piece_to_move == "B11":
                                    B11.king = True
                              else:
                                    B12.king = True
                              is_king = True
                        elif king_status:
                              is_king = True
                        else:
                              is_king = False


                        if is_jump == "y":
                              update_board(piece_to_move, current_location, where_to_move, is_king, pieces_to_jump_location)
                        else:
                              update_board(piece_to_move, current_location, where_to_move, is_king)
                        turn_count += 1

      #Red player's turn      
      else:
            try:
                  piece_to_move = input(red_player + ", which piece would you like to move? (R1, R2,...):  ")
                  where_to_move = ast.literal_eval(input("Where would you like to move to? eg.(4,5):  "))
                  is_jump = input("Are you jumping an opponent's piece? (y/n):  ")
                  if is_jump == "y":
                        multi_jump = input("Are you jumping more than one piece? (y/n):  ")
                        if multi_jump == "y":
                              jump_count = input("How many jumps are you making?:  ")
                              for i in range(int(jump_count)):
                                    pieces_to_jump.append(input("Name a piece you are jumping (B1, B2, ...):  "))
                        else:
                              pieces_to_jump.append(input("Name the piece you are jumping (B1, B2, ...):  "))
            except:
                  print("It looks like something was entered incorrectly. Try again!")
            else:
                  if piece_to_move == "quit":
                        break

                  piece_number = int(piece_to_move[1:])            
                  current_location = Checkers_Piece.red_piece_location_list[piece_number-1]
                  
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
                  if abs(int(where_to_move[1]) - int(current_location[1])) != 1 and is_jump == "n":
                        print("Sorry, that is not a valid move. Please try again.")
                  else:
                        if (int(where_to_move[0]) - int(current_location[0]) > 0):
                              movement_direction = "down"
                        else:
                              movement_direction = "up"

                        #Red pieces where king = False can only move "up" on the board and cannot be where there is already a piece, check if move is valid
                        if (where_to_move in Checkers_Piece.black_piece_location_list or where_to_move in Checkers_Piece.red_piece_location_list or (movement_direction == "down" and not king_status)):
                              print("Sorry, that is not a valid move. Please try again.")
                        elif (movement_direction == "up" or (movement_direction == "down" and king_status)) and is_jump == "y":
                              pieces_to_jump_location = []
                              for piece in pieces_to_jump:                    #need to find a way to simplify all these if statements
                                    if piece_to_move == "R1":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R1.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R1.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R1.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R1.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R1.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R1.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R1.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R1.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R1.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R1.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R1.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R1.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R2":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R2.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R2.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R2.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R2.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R2.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R2.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R2.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R2.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R2.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R2.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R2.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R2.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R3":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R3.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R3.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R3.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R3.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R3.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R3.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R3.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R3.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R3.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R3.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R3.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R3.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R4":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R4.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R4.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R4.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R4.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R4.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R4.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R4.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R4.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R4.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R4.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R4.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R4.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R5":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R5.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R5.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R5.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R5.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R5.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R5.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R5.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R5.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R5.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R5.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R5.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R5.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R6":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R6.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R6.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R6.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R6.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R6.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R6.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R6.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R6.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R6.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R6.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":                                          
                                                pieces_to_jump_location.append(B11.location)
                                                R6.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R6.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R7":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R7.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R7.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R7.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R7.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R7.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R7.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R7.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R7.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R7.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R7.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R7.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R7.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R8":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R8.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R8.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R8.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R8.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R8.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R8.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R8.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R8.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R8.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R8.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R8.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R8.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R9":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R9.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R9.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R9.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R9.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R9.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R9.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R9.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R9.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R9.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R9.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R9.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R9.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R10":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B12.location)
                                                R10.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R10.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R10.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R10.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R10.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R10.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R10.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R10.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R10.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R10.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R10.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R10.jump_enemy(B12, where_to_move)
                                    elif piece_to_move == "R11":
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R11.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R11.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R11.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R11.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R11.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R11.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R11.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R11.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R11.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R11.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R11.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R11.jump_enemy(B12, where_to_move)
                                    else:
                                          if piece == "B1":
                                                pieces_to_jump_location.append(B1.location)
                                                R12.jump_enemy(B1, where_to_move)
                                          elif piece == "B2":
                                                pieces_to_jump_location.append(B2.location)
                                                R12.jump_enemy(B2, where_to_move)
                                          elif piece == "B3":
                                                pieces_to_jump_location.append(B3.location)
                                                R12.jump_enemy(B3, where_to_move)
                                          elif piece == "B4":
                                                pieces_to_jump_location.append(B4.location)
                                                R12.jump_enemy(B4, where_to_move)
                                          elif piece == "B5":
                                                pieces_to_jump_location.append(B5.location)
                                                R12.jump_enemy(B5, where_to_move)
                                          elif piece == "B6":
                                                pieces_to_jump_location.append(B6.location)
                                                R12.jump_enemy(B6, where_to_move)
                                          elif piece == "B7":
                                                pieces_to_jump_location.append(B7.location)
                                                R12.jump_enemy(B7, where_to_move)
                                          elif piece == "B8":
                                                pieces_to_jump_location.append(B8.location)
                                                R12.jump_enemy(B8, where_to_move)
                                          elif piece == "B9":
                                                pieces_to_jump_location.append(B9.location)
                                                R12.jump_enemy(B9, where_to_move)
                                          elif piece == "B10":
                                                pieces_to_jump_location.append(B10.location)
                                                R12.jump_enemy(B10, where_to_move)
                                          elif piece == "B11":
                                                pieces_to_jump_location.append(B11.location)
                                                R12.jump_enemy(B11, where_to_move)
                                          else:
                                                pieces_to_jump_location.append(B12.location)
                                                R12.jump_enemy(B12, where_to_move)
                        elif movement_direction == "up"or (movement_direction == "down" and king_status):
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
                        else:
                              print("Something went wrong. Please try again.")
                        
                        if where_to_move[0] == 1:
                              print("Congratulations! You have gotten your piece to the far side of the board. It is now a king and can move in any direction.")
                              if piece_to_move == "R1":
                                    R1.king = True
                              elif piece_to_move == "R2":
                                    R2.king = True
                              elif piece_to_move == "R3":
                                    R3.king = True
                              elif piece_to_move == "R4":
                                    R4.king = True
                              elif piece_to_move == "R5":
                                    R5.king = True
                              elif piece_to_move == "R6":
                                    R6.king = True
                              elif piece_to_move == "R7":
                                    R7.king = True
                              elif piece_to_move == "R8":
                                    R8.king = True
                              elif piece_to_move == "R9":
                                    R9.king = True
                              elif piece_to_move == "R10":
                                    R10.king = True
                              elif piece_to_move == "R11":
                                    R11.king = True
                              else:
                                    R12.king = True
                              is_king = True
                        elif king_status:
                              is_king = True
                        else:
                              is_king = False
                        
                        if is_jump == "y":
                              update_board(piece_to_move, current_location, where_to_move, is_king, pieces_to_jump_location)
                        else:
                              update_board(piece_to_move, current_location, where_to_move, is_king)
                        turn_count += 1
                  
if Checkers_Piece.black_piece_count == 0:
      print("Congratulations " + red_player + "! You won!")
elif Checkers_Piece.red_piece_count == 0:
      print("Congratulations " + black_player + "! You won!")
else:
      print("Sorry to see you go!")

print("Thanks for playing!")