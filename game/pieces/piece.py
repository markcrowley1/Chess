
import numpy as np
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, id, colour):
        # Create bitboard and id
        self.bitboard = np.zeros(0, np.int8)
        self.piece_id = id
        self.colour = colour

    @abstractmethod
    def find_legal_moves(self, position: list) -> list:
        """Determine the legal moves for this type of piece and return as list"""
        pass

    @abstractmethod
    def update_bitboard(self):
        """Read mailbox board position add bitboard representation for this piece"""
        pass

    def set_bitboard(self, bitboard: np.ndarray):
        """Set bitboard value"""
        self.bitboard = bitboard

    def get_bitboard(self):
        """Return bitboard for piece type"""
        return self.bitboard
    
    def get_piece_id(self):
        """Return piece_id"""
        return self.piece_id
    
    def get_colour(self):
        """Return piece_id"""
        return self.colour