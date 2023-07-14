
from game.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, id, colour):
        super().__init__(id, colour)

    def find_legal_moves(self, position: list) -> list:
        return super().find_legal_moves(position)
    
    def update_bitboard(self):
        return super().update_bitboard()
    