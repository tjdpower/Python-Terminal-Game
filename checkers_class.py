#Class file for the checkers pieces

class Checkers_Piece:
    red_piece_count = 0
    black_piece_count = 0
    red_piece_location_list = []
    black_piece_location_list = []

    def __init__(self, name, colour, location, king = False):
        self.name = name
        self.colour = colour
        self.location = location
        self.king = king

        if self.colour == "red":
            Checkers_Piece.red_piece_count += 1
            Checkers_Piece.red_piece_location_list.append(self.location)
            self.list_position = Checkers_Piece.red_piece_count
        else:
            Checkers_Piece.black_piece_count += 1
            Checkers_Piece.black_piece_location_list.append(self.location)
            self.list_position = Checkers_Piece.black_piece_count
        
        
    
    def move_piece(self, new_location):
        self.location = new_location
        if self.colour == "red":
            Checkers_Piece.red_piece_location_list[self.list_position] = new_location
        else:
            Checkers_Piece.black_piece_location_list[self.list_position] = new_location
    
    def jump_enemy(self, enemy_piece, end_location):
        self.move_piece(end_location)
        if enemy_piece.colour == "red":
            Checkers_Piece.red_piece_count -= 1
            Checkers_Piece.red_piece_location_list.remove(self.location)
        else:
            Checkers_Piece.black_piece_count -= 1
            Checkers_Piece.black_piece_location_list.remove(self.location)

