
import numpy as np
from game.pieces.enums import PieceEnums
from game.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, id: PieceEnums):
        self.id = id.value

    def pseudo_legal_moves(self, square: int, mailbox: np.ndarray) -> list:
        return super().pseudo_legal_moves(square, mailbox)
    