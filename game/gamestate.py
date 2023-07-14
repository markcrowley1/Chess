"""
Description:
    Class for monitoring gamestate and determining legal moves.
"""

import game.utils as utils
import game.pieces as pieces
import numpy as np

class GameState:
    # FEN string for starting position
    sp_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def __init__(self, fen_string=sp_fen):
        # Save fen string, soon converted to bitboard representation
        self.fen_string = fen_string
        self.mailbox64 = np.zeros(64, np.int8)
        parsed_fen = utils.parse_fen_string(fen_string)
        piece_placement_str = parsed_fen[0]

        # Create piece objects
        self.piece_list = []
        for piece_id in pieces.PieceEnums:
            piece_factory = pieces.PieceFactory()
            piece: pieces.Piece = piece_factory.create_piece(piece_id)
            piece.set_bitboard(utils.fen_to_bitboard(piece_id, piece_placement_str))
            self.mailbox64 = utils.bitboard_to_mailbox64(piece_id, piece.get_bitboard(), self.mailbox64)
            self.piece_list.append(piece)

        # Additional info
        self.side_to_move: bool = parsed_fen[1] # Side to move
        self.castling_rights = parsed_fen[2]    # Castling rights for both sides
        self.enpassant_target = parsed_fen[3]   # En passant target square
        self.half_move_clock = parsed_fen[4]    # Half move clock
        self.full_move_counter = parsed_fen[5]  # Full move counter

    def find_legal_moves(self):
        """Return a list of legal moves"""
        # Bitboard
        # Castling
        # En passant
        pass

    def is_game_over(self):
        """Check if game is over due to checkmate, stalemate or other"""
        pass

    def make_move(self):
        """Update the position according to new move"""
        # Update bitboard representation
        # Update the mailbox repr
        # Update the fen string
        # Update side to move and move count
        pass

    def toggle_back(self):
        """Return to previous position"""
        pass

    def toggle_forwards(self):
        """Return to the following position"""
        pass

    def get_mailbox64(self):
        return self.mailbox64

