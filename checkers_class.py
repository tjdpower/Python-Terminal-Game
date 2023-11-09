#Class file for the checkers pieces

class Checkers_Piece:
    white_piece_count = 0
    black_piece_count = 0
    white_piece_location_list = []
    black_piece_location_list = []

    def __init__(self, name, colour, location, king = False):
        self.name = name
        self.colour = colour
        self.location = location
        self.king = king

        if self.colour == "white":
            Checkers_Piece.white_piece_count += 1
            Checkers_Piece.white_piece_location_list.append(self.location)
            self.list_position = (Checkers_Piece.white_piece_count - 1)
        else:
            Checkers_Piece.black_piece_count += 1
            Checkers_Piece.black_piece_location_list.append(self.location)
            self.list_position = (Checkers_Piece.black_piece_count - 1)

    def __repr__(self):
        return f"{self.name} is {self.colour} and is at the location {self.location}. Is it a king? - {self.king}"

    def move_piece(self, new_location):
        self.location = new_location
        if self.colour == "white":
            Checkers_Piece.white_piece_location_list[self.list_position] = new_location
        else:
            Checkers_Piece.black_piece_location_list[self.list_position] = new_location
    
    def jump_enemy(self, enemy_piece, end_location):
        self.move_piece(end_location)
        if enemy_piece.colour == "white":
            Checkers_Piece.white_piece_count -= 1
            Checkers_Piece.white_piece_location_list[enemy_piece.list_position] = "null"
        else:
            Checkers_Piece.black_piece_count -= 1
            Checkers_Piece.black_piece_location_list[enemy_piece.list_position] = "null"
        enemy_piece.location = "null"

