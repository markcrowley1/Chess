
from enum import Enum

class PieceEnums(Enum):
    WHITE_PAWN = 1
    WHITE_ROOK = 2
    WHITE_KNIGHT = 3
    WHITE_BISHOP = 4
    WHITE_QUEEN = 5
    WHITE_KING = 6
    BLACK_PAWN = -1
    BLACK_ROOK = -2
    BLACK_KNIGHT = -3
    BLACK_BISHOP = -4
    BLACK_QUEEN = -5
    BLACK_KING = -6

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

    char_to_enum = {
        "P": PieceEnums.WHITE_PAWN,
        "p": PieceEnums.BLACK_PAWN,
        "R": PieceEnums.WHITE_ROOK,
        "r": PieceEnums.BLACK_ROOK,
        "N": PieceEnums.WHITE_KNIGHT,
        "n": PieceEnums.BLACK_KNIGHT,
        "B": PieceEnums.WHITE_BISHOP,
        "b": PieceEnums.BLACK_BISHOP,
        "Q": PieceEnums.WHITE_QUEEN,
        "q": PieceEnums.BLACK_QUEEN,
        "K": PieceEnums.WHITE_KING,
        "k": PieceEnums.BLACK_KING
    }