"""
Description:
    Simple testing script
"""

import numpy as np
from game.gui import GUI
import game.utils as utils
import game.pieces as pieces

def main():
    # Create bitboard
    mailbox64 = np.zeros(64)
    sp_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    for piece_id in pieces.PieceEnums:
            piece_factory = pieces.PieceFactory()
            piece: pieces.Piece = piece_factory.create_piece(piece_id)
            bitboard = utils.fen_to_bitboard(piece_id, sp_fen)
            piece.set_bitboard(bitboard)
            mailbox64 = utils.bitboard_to_mailbox64(piece_id, bitboard, mailbox64)
            print(f"--- {piece_id.value} ---")
            print(bitboard)
    # Convert bitboard to mailbox
    print(f"--- mailbox ---")
    print(mailbox64)
    
if __name__ == "__main__":
    main()