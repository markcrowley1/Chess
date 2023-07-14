
from game.pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, id, colour):
        super().__init__(id, colour)

    def find_legal_moves(self, position: list) -> list:
        return super().find_legal_moves(position)
    
    def update_bitboard(self):
        return super().update_bitboard()
    
    def get_bitboard(self):
        return super().get_bitboard()
    
    def get_colour(self):
        return super().get_colour()
    
    def get_piece_id(self):
        return super().get_piece_id()