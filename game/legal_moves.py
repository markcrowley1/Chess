"""
Description:
    Extra checks. Ensure legality of pseudo legal moves generated in piece classes.
    Check if en passant occured on previous turn. Check if castling rights have
    been used up on the previous turn.
"""

import numpy as np
import game.pieces as pieces

class LegalMoves:
    # Mailbox mapping
    mailbox120 = [
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
     -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
     -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
     -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
     -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
     -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
     -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
     -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
    ]
    mailbox64_to_120 = [
        21, 22, 23, 24, 25, 26, 27, 28,
        31, 32, 33, 34, 35, 36, 37, 38,
        41, 42, 43, 44, 45, 46, 47, 48,
        51, 52, 53, 54, 55, 56, 57, 58,
        61, 62, 63, 64, 65, 66, 67, 68,
        71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98
    ]
    # Offsets to determine if king is in check
    diagonal_offset_values = [9, -9, 11, -11]
    rank_file_offset_values = [1, -1, 10, -10]
    knight_offset_values = [19, -19, 21, -21]
    pawn_offset_values = [9, 11]
    white_king_value: int = pieces.PieceEnums.WHITE_KING.value
    diagonal_ids = [pieces.PieceEnums.BLACK_QUEEN.value, pieces.PieceEnums.BLACK_BISHOP.value]
    rank_file_ids = [pieces.PieceEnums.BLACK_QUEEN.value, pieces.PieceEnums.BLACK_ROOK.value]

    def __init__(self):
        pass

    def is_king_in_check(self, side_to_move: int, mailbox: np.ndarray) -> bool:
        """Determine whether or not the king is in check"""
        print("func")
        in_check = False
        for i in range(64):
            piece_value = mailbox[i]
            if piece_value == self.white_king_value*side_to_move:
                in_check = self.__is_square_attacked(i, side_to_move, mailbox)
                print("if")
                break
        return in_check

    def castling(self, side_to_move: int, castling_rights: list,  mailbox: np.ndarray):
        """Check if castling is allowed"""
        pass

    def __is_square_attacked(self, square: int, side_to_move: int, mailbox: np.ndarray) -> bool:
        """Determine whether or not any particular square is attacked by enemy"""
        is_attacked = False
        # Check for diagonal sliding piece attacks
        for offset in self.diagonal_offset_values:
            full_offset = offset
            while True:
                destination = self.mailbox120[self.mailbox64_to_120[square] + full_offset]
                if destination < 0:
                    break
                elif mailbox[destination] * side_to_move > 0:
                    break
                elif mailbox[destination]*side_to_move in self.diagonal_ids:
                    is_attacked = True
                    return is_attacked
                else:
                    full_offset += offset

        # Check for rank/file sliding piece attacks
        for offset in self.rank_file_offset_values:
            full_offset = offset
            while True:
                destination = self.mailbox120[self.mailbox64_to_120[square] + full_offset]
                if destination < 0:
                    break
                elif mailbox[destination] * side_to_move > 0:
                    break
                elif mailbox[destination]*side_to_move in self.rank_file_ids:
                    is_attacked = True
                    return is_attacked
                else:
                    full_offset += offset

        # Check for knight attacks
        for offset in self.knight_offset_values:
                destination = self.mailbox120[self.mailbox64_to_120[square] + offset]
                if destination < 0:
                    pass
                elif mailbox[destination]*side_to_move == pieces.PieceEnums.BLACK_KNIGHT.value:
                    is_attacked = True
                    return is_attacked
                
        # Check for pawn atacks
        for offset in self.pawn_offset_values:
            destination = square + side_to_move*offset
            if (0 <= destination < 64) and mailbox[destination]*destination == pieces.PieceEnums.BLACK_PAWN.value:
                is_attacked = True

        return is_attacked

    def en_passant(self, en_passant_square: int, mailbox: np.ndarray):
        pass