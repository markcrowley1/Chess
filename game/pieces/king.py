

import numpy as np
from game.pieces.enums import PieceEnums
from game.pieces.piece import Piece

class King(Piece):
    offset_values = [1, -1, 9, 10, 11, -9, -10, -11]

    def __init__(self, id: PieceEnums):
        self.id = id.value

    def pseudo_legal_moves(self, square: int, mailbox: np.ndarray) -> list:
        """ Determine the pseudo legal moves for this piece"""
        moves = []
        for offset in self.offset_values:
                destination = self.mailbox120[self.mailbox64_to_120[square] + offset]
                if destination < 0:
                    pass
                elif mailbox[destination] * self.id > 0:
                    pass
                elif mailbox[destination] * self.id < 0:
                    moves.append((square, destination))
                else:
                    moves.append((square, destination))
        return moves