#Class file for the checkers pieces

class Checkers_Piece:
    red_piece_count = 0
    black_piece_count = 0
    red_piece_list = []
    black_piece_list = []

    def __init__(self, name, colour, location, king = False):
        self.name = name
        self.colour = colour
        self.location = location
        self.king = king

        if self.colour == "red":
            red_piece_count += 1
            red_piece_list.append(self.name)
        else:
            black_piece_count += 1
            black_piece_list.append(self.name)
    
    def move_piece(self, new_location):
        self.location = new_location
    
    def jump_enemy(self, enemy_piece, end_location):
        move_piece(end_location)
        if enemy_piece.colour == "red":
            red_piece_count -= 1
            red_piece_list.remove(self.name)
        else:
            black_piece_count -= 1
            black_piece_list.remove(self.name)

