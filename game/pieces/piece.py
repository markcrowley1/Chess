
import numpy as np
from abc import ABC

class Piece:
    def __init__(self):
        self.bitboard = np.int64(0)