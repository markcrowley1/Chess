"""
Description:
    Miscellaneous functions - converting board representations
"""

import numpy as np
import game.pieces as pieces

def parse_fen_string(fen_string: str):
    """Read fen string and convert to manageable format"""
    # Split the fen string
    split_str: list = fen_string.split()
    print(split_str)
    # Transform data
    # Seperate piece placement string from FEN
    piece_placement = split_str[0]
    # Set side to move
    side_char: str = split_str[1]
    if side_char == "w":
        side_to_move = False
    else:
        side_to_move = True
    # Represent castling rights for both sides
    castling_rights_str = split_str[2]
    wk = wq = bk = bq = False
    if "K" in castling_rights_str:
        wk = True
    if "Q" in castling_rights_str:
        wq = True
    if "k" in castling_rights_str:
        bk = True
    if "q" in castling_rights_str:
        bq = True
    castling_rights = ((wk, wq), (bk, bq))
    # Note square available for en passant
    enpassant_target_str = split_str[3]
    if enpassant_target_str == "-":
        enpassant_target_sq_no = -1
    else:
        file, rank = list(enpassant_target_str)
        file = ord(file) - 97
        enpassant_target_sq_no = (rank - 1)*8 + file
    # Handle 50 move capture rule
    half_move_clock = int(split_str[4])
    # Count move number
    full_move_counter = int(split_str[5])
    # Package data
    parsed_data = (
        piece_placement,
        side_to_move,
        castling_rights, 
        enpassant_target_sq_no,
        half_move_clock,
        full_move_counter
    )
    return parsed_data

def fen_to_mailbox64(fen_piece_string: str) -> np.ndarray:
    mailbox64 = []
    ranks: list = fen_piece_string.split("/")
    ranks.reverse()
    for rank in ranks:
        for char in rank:
            if char.isnumeric():
                mailbox64 = mailbox64 + [0 for i in range(int(char))]
            elif char in pieces.PieceMapping.char_to_enum:
                mailbox64.append(pieces.PieceMapping.char_to_enum[char].value)
    return np.array(mailbox64, np.int8)


def mailbox64_to_fen(mailbox: np.ndarray, fen_string: str):
    """Convert mailbox repr back to fen string --- unfinished"""
    count = 0
    fen_string = ""
    for i, val in enumerate(mailbox):
        if val == 0:
            count += 1
        else:
            fen_string += str(count)
            count = 0

"""--- Bitboard related conversions ---"""

def fen_to_bitboard(piece: pieces.PieceEnums, fen_pieces: str) -> np.ndarray:
    """Take first part of fen string and convert to bitboard for single piece type."""
    piece_char: str = pieces.PieceMapping.enum_to_char[piece]
    fen_pieces: list = fen_pieces.split("/")
    fen_pieces.reverse()
    bitboard = []
    for rank in fen_pieces:
        if piece_char in rank:
            for element in rank:
                if element.isnumeric():
                    bitboard = bitboard + [0 for i in range(int(element))]
                elif element is not piece_char:
                    bitboard = bitboard + [0]
                else:
                    bitboard = bitboard + [1]
        else:
            bitboard = bitboard + [0 for i in range(8)]
            
    return np.array(bitboard)


def bitboard_to_mailbox64(piece_id: pieces.PieceEnums, bitboard: np.ndarray, mailbox: np.ndarray) -> np.ndarray:
    """Update mailbox with bitboard info"""
    single_piece_mailbox = piece_id.value * bitboard
    mailbox += single_piece_mailbox
    return mailbox

def mailbox64_to_bitboard(mailbox: np.ndarray, piece_id: pieces.PieceEnums) -> np.ndarray:
    bitboard = []
    for val in mailbox:
        if val == piece_id.value:
            bitboard.append(1)
        else:
            bitboard.append(0)
    return np.array(bitboard)