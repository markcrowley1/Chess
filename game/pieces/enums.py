
from enum import Enum

class PieceEnums(Enum):
    WHITE_PAWN = 1
    BLACK_PAWN = 2
    WHITE_ROOK = 3
    BLACK_ROOK = 4
    WHITE_KNIGHT = 5
    BLACK_KNIGHT = 6
    WHITE_BISHOP = 7
    BLACK_BISHOP = 8
    WHITE_QUEEN = 9
    BLACK_QUEEN = 10
    WHITE_KING = 11
    BLACK_KING = 12

class PieceMapping:
    enum_to_char = {
        PieceEnums.WHITE_PAWN: "P",
        PieceEnums.BLACK_PAWN: "p",
        PieceEnums.WHITE_ROOK: "R",
        PieceEnums.BLACK_ROOK: "r",
        PieceEnums.WHITE_KNIGHT: "N",
        PieceEnums.BLACK_KNIGHT: "n",
        PieceEnums.WHITE_BISHOP: "B",
        PieceEnums.BLACK_BISHOP: "b",
        PieceEnums.WHITE_QUEEN: "Q",
        PieceEnums.BLACK_QUEEN: "q",
        PieceEnums.WHITE_KING: "K",
        PieceEnums.BLACK_KING: "k"
    }