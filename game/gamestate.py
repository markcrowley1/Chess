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
    # List for keeping track of legal moves
    legal_moves = []
    # List for keeping track of previous positions
    position_list = []

    def __init__(self, fen_string=sp_fen):
        """Set up game based on fen string, recording all important info."""
        # Save fen string, soon converted to bitboard representation
        self.fen_string = fen_string
        self.mailbox64 = np.zeros(64, np.int8)
        parsed_fen = utils.parse_fen_string(fen_string)
        piece_placement_str = parsed_fen[0]

        # Create piece objects
        self.white_pieces: list[pieces.Piece] = []
        self.black_pieces: list[pieces.Piece] = []
        for piece_id in pieces.PieceEnums:
            piece_factory = pieces.PieceFactory()
            piece: pieces.Piece = piece_factory.create_piece(piece_id)
            piece.set_bitboard(utils.fen_to_bitboard(piece_id, piece_placement_str))
            self.mailbox64 = utils.bitboard_to_mailbox64(piece_id, piece.get_bitboard(), self.mailbox64)
            if piece_id.value % 2 == 1:
                self.white_pieces.append(piece)
            else:
                self.black_pieces.append(piece)

        # Additional info
        self.side_to_move: bool = parsed_fen[1] # Side to move
        self.castling_rights = parsed_fen[2]    # Castling rights for both sides
        self.enpassant_target = parsed_fen[3]   # En passant target square
        self.half_move_clock = parsed_fen[4]    # Half move clock
        self.full_move_counter = parsed_fen[5]  # Full move counter
        self.game_over = False                  # Boolean - is game over
        self.piece_list: list[pieces.Piece] = self.white_pieces + self.black_pieces
        
    def find_legal_moves(self):
        """Return a list of legal moves"""
        # Bitboard calculations - pseudo legal
        white_pieces_bb = np.zeros(64, np.int8)
        black_pieces_bb = np.zeros(64, np.int8)
        for piece in self.white_pieces:
            white_pieces_bb += piece.get_bitboard()
        for piece in self.black_pieces:
            black_pieces_bb += piece.get_bitboard()

        if self.side_to_move is False:
            for piece in self.white_pieces:
                pass
        else:
            for piece in self.black_pieces:
                pass
        # Castling
        # En passant
        # Ensure king is not in check after move
        pass

    def make_move(self, origin: int, destination: int):
        """Update all board representations"""
        # Check if suggested move is castling
        # Check if suggested move is en passant
        # Update mailbox64
        piece_id = self.mailbox64[origin]
        self.mailbox64[origin] = 0
        self.mailbox64[destination] = piece_id
        # Update bitboard representations
        for piece in self.piece_list:
            bitboard = utils.mailbox64_to_bitboard(self.mailbox64,
                                                 piece.get_piece_id())
            piece.set_bitboard(bitboard)
        # Update side to move and move count
        self.side_to_move = not self.side_to_move
        if self.side_to_move is False:
            self.full_move_counter += 1
        # Update the fen string
        """--- unfinished function in utils ---"""
        return
    
    def is_game_over(self):
        """Check if game is over due to checkmate, stalemate or other"""
        pass

    def toggle_back(self):
        """Return to previous position"""
        pass

    def toggle_forwards(self):
        """Return to the following position"""
        pass

    def get_mailbox64(self):
        return self.mailbox64
    
    def get_full_move_count(self):
        return self.full_move_counter
    
    def get_side_to_move(self):
        return self.side_to_move

