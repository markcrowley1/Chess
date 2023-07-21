
from game.pieces.enums import PieceEnums
import game.pieces as pieces

class PieceFactory:
    def __init__(self):
        self._pieces = {
            PieceEnums.WHITE_PAWN: pieces.Pawn,
            PieceEnums.BLACK_PAWN: pieces.Pawn,
            PieceEnums.WHITE_ROOK: pieces.Rook,
            PieceEnums.BLACK_ROOK: pieces.Rook,
            PieceEnums.WHITE_KNIGHT: pieces.Knight,
            PieceEnums.BLACK_KNIGHT: pieces.Knight,
            PieceEnums.WHITE_BISHOP: pieces.Bishop,
            PieceEnums.BLACK_BISHOP: pieces.Bishop,
            PieceEnums.WHITE_QUEEN: pieces.Queen,
            PieceEnums.BLACK_QUEEN: pieces.Queen,
            PieceEnums.WHITE_KING: pieces.King,
            PieceEnums.BLACK_KING: pieces.King
        }

    def create_piece(self, piece_id: pieces.PieceEnums):
        """ Create Piece object for storing piece locations 
            and determining possible moves """
        return self._pieces[piece_id](piece_id)