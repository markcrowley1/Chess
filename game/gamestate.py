"""
Description:
    Class for monitoring gamestate and determining legal moves.
"""

from game.legal_moves import LegalMoves
import game.utils as utils
import game.pieces as pieces
import numpy as np

class GameState:
    # FEN string for starting position
    sp_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    legal_moves = []    # List for keeping track of legal moves
    move_list = []      # List of previously made moves
    position_list = []  # List for keeping track of previous positions

    def __init__(self, fen_string=sp_fen):
        """Set up game based on fen string, recording all important info."""
        # Save fen string which will be converted to mailbox repr
        self.fen_string = fen_string
        parsed_fen = utils.parse_fen_string(fen_string)
        piece_placement_str = parsed_fen[0]

        # Create piece object for each piece
        # These objects are used to calculate pseudo legal moves
        pf = pieces.PieceFactory()
        self.piece_dict = {}
        for piece_id in pieces.PieceEnums:
                piece = pf.create_piece(piece_id)
                self.piece_dict[piece_id.value] = piece

        # Create object for testing legality of pseudo legal moves
        # and handling other miscellaneous rules
        self.lm = LegalMoves()

        # Game status info
        self.mailbox64 = utils.fen_to_mailbox64(piece_placement_str)
        self.side_to_move: bool = parsed_fen[1] # Side to move
        self.castling_rights = parsed_fen[2]    # Castling rights for both sides
        self.enpassant_target = parsed_fen[3]   # En passant target square
        self.half_move_clock = parsed_fen[4]    # Half move clock
        self.full_move_counter = parsed_fen[5]  # Full move counter
        self.game_over = False                  # Boolean - is game over
        self.en_passant_moves = []              # Keep track of possible en passant moves
        self.find_legal_moves()
        
    def find_legal_moves(self):
        """Return a list of legal moves"""
        # Pseudo legal calculations
        pl_moves = []
        for i in range(64):
            piece_id_value = self.mailbox64[i]
            if (piece_id_value*self.side_to_move > 0 and 
                    piece_id_value in self.piece_dict):
                piece: pieces.Piece = self.piece_dict[piece_id_value]
                moves = piece.pseudo_legal_moves(i, self.mailbox64)
                pl_moves += moves
        # En passant
        if len(self.move_list) > 0:
            previous_move = self.move_list[-1]
            temp_mailbox64 = self.mailbox64.copy()
            self.enpassant_target, ep_moves = self.lm.en_passant(previous_move, 
                                                            temp_mailbox64)
            pl_moves += ep_moves
        elif self.enpassant_target >= 0:
            exit("Not implemented")
        else:
            ep_moves = []
            self.enpassant_target = -1
            self.en_passant_moves = []
            
        # Ensure king is not in check after move
        legal_moves = []
        for pl_move in pl_moves:
            origin, destination = pl_move
            temp_mailbox64 = self.mailbox64.copy()
            piece_id = temp_mailbox64[origin]
            temp_mailbox64[origin] = 0
            temp_mailbox64[destination] = piece_id
            in_check = self.lm.is_king_in_check(self.side_to_move,
                                                    temp_mailbox64)
            if not in_check:
                legal_moves.append(pl_move)

        # Castling
        
        # Check that en passant moves are still legal after extra checks
        for move in ep_moves:
            if move in legal_moves:
                self.en_passant_moves.append(move)
        if len(self.en_passant_moves) == 0:
            self.enpassant_target = -1
            self.en_passant_moves = []

        # Update object variable and quit
        self.legal_moves = legal_moves
        return
    
    def is_legal_move(self, origin: int, destination: int) -> bool:
        move = (origin, destination)
        if move in self.legal_moves:
            is_legal = True
        else:
            is_legal = False
        return is_legal

    def make_move(self, origin: int, destination: int):
        """Update board according to new move"""
        # Check if suggested move is castling
        # Check if suggested move is en passant
        if (origin, destination) in self.en_passant_moves:
            self.__take_en_passant(origin, destination)
        # Update mailbox64
        else:
            piece_id = self.mailbox64[origin]
            self.mailbox64[origin] = 0
            self.mailbox64[destination] = piece_id
        # Keep track of move made
        self.move_list.append((origin, destination))
        # Update side to move and move count
        self.side_to_move = -self.side_to_move
        if self.side_to_move > 0:
            self.full_move_counter += 1
        print(f"Side to move is: {self.side_to_move}")
        print(f"Move count is: {self.full_move_counter}")
        return
    
    def __castle(self, origin: int, destination: int):
        """Make castling move"""
        pass

    def __take_en_passant(self, origin: int, destination: int):
        """Make en passant move"""
        piece_id = self.mailbox64[origin]
        self.mailbox64[origin] = 0
        self.mailbox64[destination] = piece_id
        opponent_pawn = destination - 8*self.side_to_move
        self.mailbox64[opponent_pawn] = 0
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
    
    def get_legal_moves(self):
        return self.legal_moves
    
    def get_full_move_count(self):
        return self.full_move_counter
    
    def get_side_to_move(self):
        return self.side_to_move

