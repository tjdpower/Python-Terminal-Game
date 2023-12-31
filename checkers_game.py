#Main file for checkers game

from checkers_class import Checkers_Piece
import ast

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
white_player = input("Who will play the white pieces?: ")
black_player = input("Who will play the black pieces?: ")

print("Thank you " + white_player + " and " + black_player + ", let's begin!")

#initialize pieces
B1 = Checkers_Piece("Black1", "black", (1,1)) #can this process be done with a loop?
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
W1 = Checkers_Piece("white1", "white", (8,8))
W2 = Checkers_Piece("white2", "white", (8,6))
W3 = Checkers_Piece("white3", "white", (8,4))
W4 = Checkers_Piece("white", "white", (8,2))
W5 = Checkers_Piece("white5", "white", (7,7))
W6 = Checkers_Piece("white6", "white", (7,5))
W7 = Checkers_Piece("white7", "white", (7,3))
W8 = Checkers_Piece("white8", "white", (7,1))
W9 = Checkers_Piece("white9", "white", (6,8))
W10 = Checkers_Piece("white10", "white", (6,6))
W11 = Checkers_Piece("white11", "white", (6,4))
W12 = Checkers_Piece("white12", "white", (6,2))

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

#placing white pieces on board

for d in range(len(Checkers_Piece.white_piece_location_list)):
      temp_string = ""
      location = Checkers_Piece.white_piece_location_list[d]
      if d < 9:
            temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " W" + str(d+1) + "  " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]
      else:
            temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " W" + str(d+1) + " " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]
      board[location[0]*3 + location[0] - 1] = temp_string

#Placing black pieces on board

for e in range(len(Checkers_Piece.black_piece_location_list)):
      temp_string = ""
      location = Checkers_Piece.black_piece_location_list[e]
      if e < 9:
            temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " B" + str(e+1) + "  " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]
      else:
            temp_string = board[location[0]*3 + location[0] - 1][:((location[1]*2 - 1) * 3)-1] + " B" + str(e+1) + " " + board[location[0]*3 + location[0] - 1][((location[1]*2 - 1) * 3)+4:]
      board[location[0]*3 + location[0] - 1] = temp_string

#printing starting board
for f in range(len(board)):
      print(board[f])

#a function to adjust and redraw the board
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

#determine which variable is described by the user's response
def identify_piece(piece_to_identify):
      if piece_to_identify == "B1":
            return B1
      elif piece_to_identify == "B2":
            return B2
      elif piece_to_identify == "B3":
            return B3
      elif piece_to_identify =="B4":
            return B4
      elif piece_to_identify == "B5":
            return B5
      elif piece_to_identify == "B6":
            return B6
      elif piece_to_identify == "B7":
            return B7
      elif piece_to_identify == "B8":
            return B8
      elif piece_to_identify == "B9":
            return B9
      elif piece_to_identify == "B10":
            return B10
      elif piece_to_identify == "B11":
            return B11
      elif piece_to_identify == "B12":
            return B12
      elif piece_to_identify == "W1":
            return W1
      elif piece_to_identify == "W2":
            return W2
      elif piece_to_identify == "W3":
            return W3
      elif piece_to_identify =="W4":
            return W4
      elif piece_to_identify == "W5":
            return W5
      elif piece_to_identify == "W6":
            return W6
      elif piece_to_identify == "W7":
            return W7
      elif piece_to_identify == "W8":
            return W8
      elif piece_to_identify == "W9":
            return W9
      elif piece_to_identify == "W10":
            return W10
      elif piece_to_identify == "W11":
            return W11
      else:
            return W12

#begin playing the game
print("The black pieces get to start, so " + black_player + " will go first.")

turn_count = 0

#loop until one player has no pieces left
while (Checkers_Piece.black_piece_count != 0 and Checkers_Piece.white_piece_count != 0):

      pieces_to_jump = []
      if turn_count % 2 == 0:
            try:
                  piece_to_move = input(black_player + ", which piece would you like to move? (B1, B2,...):  ")

                  if piece_to_move == "quit":
                        break
                  
                  where_to_move = ast.literal_eval(input("Where would you like to move to? Please enter as (row#,Col#) eg.(4,5):  "))
                  is_jump = input("Are you jumping an opponent's piece? (y/n):  ")
                  if is_jump == "y":
                        multi_jump = input("Are you jumping more than one piece? (y/n):  ")
                        if multi_jump == "y":
                              jump_count = input("How many jumps are you making?:  ")
                              for i in range(int(jump_count)):
                                    pieces_to_jump.append(input("Name a piece you are jumping (W1, W2, ...):  "))
                        else:
                              pieces_to_jump.append(input("Name the piece you are jumping (W1, W2, ...):  "))
            except:
                  print("It looks like something was entered incorrectly. Try again!")
            else:
                  
                  piece_number = int(piece_to_move[1:])
                  current_location = Checkers_Piece.black_piece_location_list[piece_number-1]
                  piece_object = identify_piece(piece_to_move)
                                    
                  #need to identify if checker piece being moved is a king
                  king_status = piece_object.king
                  
                  #movement check and direction assignment
                  horizontal_change = abs(int(where_to_move[1]) - int(current_location[1]))
                  vertical_change = abs(int(where_to_move[0]) - int(current_location[0]))
                  if horizontal_change != vertical_change:
                        print("Sorry, that is not a valid move. Please try again.")
                  elif horizontal_change != 1 and is_jump == "n":
                        print("You can only move one space at a time unless you are jumping another piece!")
                  else:
                        if (int(where_to_move[0]) - int(current_location[0]) > 0):
                              movement_direction = "down"
                        else:
                              movement_direction = "up"

                        #Black pieces where king = False can only move "down" on the board and cannot be where there is already a piece, check if move is valid
                        if (where_to_move in Checkers_Piece.black_piece_location_list or where_to_move in Checkers_Piece.white_piece_location_list or (movement_direction == "up" and not king_status)):
                              print("Sorry, that is not a valid move. Please try again.")

                        elif movement_direction == ("down" or (movement_direction == "up" and king_status)) and is_jump == "y":
                              pieces_to_jump_location = []
                              for piece in pieces_to_jump:
                                    piece_object_enemy = identify_piece(piece)
                                    pieces_to_jump_location.append(piece_object_enemy.location)
                                    piece_object.jump_enemy(piece_object_enemy, where_to_move)

                        elif movement_direction == "down" or (movement_direction == "up" and king_status):
                              piece_object.move_piece(where_to_move)

                        else:
                              print("Something went wrong. Please try again.")
                        
                        #check if piece should become a king, or is already a king
                        if where_to_move[0] == 8:
                              print("Congratulations! You have gotten your piece to the far side of the board. It is now a king and can move in any direction.")
                              piece_object.king = True
                              is_king = True
                        elif king_status:
                              is_king = True
                        else:
                              is_king = False                        
                        
                        #update and redraw board with new piece positions
                        if is_jump == "y":
                              update_board(piece_to_move, current_location, where_to_move, is_king, pieces_to_jump_location)
                        else:
                              update_board(piece_to_move, current_location, where_to_move, is_king)
                        turn_count += 1

      #white player's turn      
      else:
            try:
                  piece_to_move = input(white_player + ", which piece would you like to move? (W1, W2,...):  ")
                  
                  if piece_to_move == "quit":
                        break
                  
                  where_to_move = ast.literal_eval(input("Where would you like to move to? Please enter as (row#,Col#) eg.(4,5):  "))
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
                  
                  piece_number = int(piece_to_move[1:])            
                  current_location = Checkers_Piece.white_piece_location_list[piece_number-1]
                  piece_object = identify_piece(piece_to_move)
                  
                  #need to identify which checker piece is being moved
                  king_status = piece_object.king
                  
                  
                  #movement check and direction assignment
                  horizontal_change = abs(int(where_to_move[1]) - int(current_location[1]))
                  vertical_change = abs(int(where_to_move[0]) - int(current_location[0]))
                  if horizontal_change != vertical_change:
                        print("Sorry, that is not a valid move. Please try again.")
                  elif horizontal_change != 1 and is_jump == "n":
                        print("You can only move one space at a time unless you are jumping another piece!")
                  else:
                        if (int(where_to_move[0]) - int(current_location[0]) > 0):
                              movement_direction = "down"
                        else:
                              movement_direction = "up"

                        #white pieces where king = False can only move "up" on the board and cannot be where there is already a piece, check if move is valid
                        if (where_to_move in Checkers_Piece.black_piece_location_list or where_to_move in Checkers_Piece.white_piece_location_list or (movement_direction == "down" and not king_status)):
                              print("Sorry, that is not a valid move. Please try again.")

                        elif (movement_direction == "up" or (movement_direction == "down" and king_status)) and is_jump == "y":
                              pieces_to_jump_location = []
                              for piece in pieces_to_jump:
                                    piece_object_enemy = identify_piece(piece)
                                    pieces_to_jump_location.append(piece_object_enemy.location)
                                    piece_object.jump_enemy(piece_object_enemy, where_to_move)

                        elif movement_direction == "up"or (movement_direction == "down" and king_status):
                              piece_object.move_piece(where_to_move)

                        else:
                              print("Something went wrong. Please try again.")
                        
                        #check if piece should become a king, or is already a king
                        if where_to_move[0] == 1:
                              print("Congratulations! You have gotten your piece to the far side of the board. It is now a king and can move in any direction.")
                              piece_object.king = True
                              is_king = True
                        elif king_status:
                              is_king = True
                        else:
                              is_king = False
                        
                        #update and redraw board with new piece positions
                        if is_jump == "y":
                              update_board(piece_to_move, current_location, where_to_move, is_king, pieces_to_jump_location)
                        else:
                              update_board(piece_to_move, current_location, where_to_move, is_king)
                        turn_count += 1
                  
if Checkers_Piece.black_piece_count == 0:
      print("Congratulations " + white_player + "! You won!")
elif Checkers_Piece.white_piece_count == 0:
      print("Congratulations " + black_player + "! You won!")
else:
      print("Sorry to see you go!")

print("Thanks for playing!")