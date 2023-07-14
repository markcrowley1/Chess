

import numpy as np
from game.pieces.piece import Piece

class King(Piece):
    def __init__(self, id, colour):
        super().__init__(id, colour)

    def update_bitboard(self):
        return super().update_bitboard()
    
    def find_legal_moves(self, position: list) -> list:
        return super().find_legal_moves(position)
    
    def get_bitboard(self):
        """Return bitboard for piece type"""
        return self.bitboard
    
    def get_colour(self):
        return super().get_colour()
    
    def get_piece_id(self):
        return super().get_piece_id()