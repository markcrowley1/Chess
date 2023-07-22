
import numpy as np
from game.pieces.enums import PieceEnums
from game.pieces.piece import Piece

class Pawn(Piece):
    offset_values = [9, 11] # Mailbox 120 attacking offsets

    def __init__(self, id: PieceEnums):
        self.id = id.value

    def pseudo_legal_moves(self, square: int, mailbox: np.ndarray) -> list:
        sign = self.id # White pawn is 1, black pawn is -1 - move pawn up/down board
        moves = []
        
        # Mailbox 64 offset
        forward_offset = 8
        take_offset = [7, 9] 
        # Move pawn forward one square
        destination = square + sign*forward_offset
        if (0 <= destination < 64) and mailbox[destination] == 0:
            moves.append((square, destination))
            # Check if pawn can be moved forward by 2 squares
            if self.id > 0 and int(square/8) == 1:
                origin = True
            elif self.id < 0 and int(square/8) == 6:
                origin = True
            else:
                origin = False     
            destination += sign*forward_offset
            if origin is True and mailbox[destination] == 0:
                moves.append((square, destination))
        # Check if pawn can take piece
        for offset in take_offset:
            destination = square + sign*offset
            if (0 <= destination < 64) and mailbox[destination]*self.id < 0:
                moves.append((square, destination))

        return moves
    

            