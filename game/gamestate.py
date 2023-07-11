"""
Description:
    Class for monitoring gamestate and determining legal moves.
"""

import game.pieces as pieces
import numpy as np

class GameState:
    starting_position_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 "

    def __init__(self):
        self.mailbox64 = np.zeros(64)
        # self.mailbox64 = np.ndarray()
        pass

    def get_mailbox64(self):
        return self.mailbox64

