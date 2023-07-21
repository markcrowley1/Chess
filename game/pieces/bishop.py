
import numpy as np
from game.pieces.enums import PieceEnums
from game.pieces.piece import Piece

class Bishop(Piece):
    offset_values = [11, 9, -11, -9]

    def __init__(self, id: PieceEnums):
        self.id = id.value

    def pseudo_legal_moves(self, square: int, mailbox: np.ndarray) -> list:
        """ Determine the pseudo legal moves for this piece"""
        moves = []
        for offset in self.offset_values:
            full_offset = offset
            while True:
                destination = self.mailbox120[self.mailbox64_to_120[square] + full_offset]
                if destination < 0:
                    break
                elif mailbox[destination] * self.id > 0:
                    break
                elif mailbox[destination] * self.id < 0:
                    moves.append((square, destination))
                    break
                else:
                    moves.append((square, destination))
                    full_offset += offset
                    print("test")
        return moves