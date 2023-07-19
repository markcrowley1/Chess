"""
Description:
    Class for providing graphical user interface
"""

import pygame
import numpy as np
import game.pieces as pieces
from game.gamestate import GameState

class GUI:
    # Boolean to check if game running
    running: bool = True
    # Define Constants
    WIDTH = HEIGHT = 400
    DIMENSION = 8
    SQ_SIZE = WIDTH/DIMENSION
    MAX_FPS = 15

    def __init__(self):
        # Load in images as dictionary
        self.piece_imgs: dict = self.__load_imgs()

        # Initialise pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.fill(pygame.Color("white"))

        # Selected squares for movement and highlighting
        self.highlighted_squares: list = []
        self.move_origin: int = -1
        self.move_destination: int = -1

    def update(self, gs: GameState):
        """Update game window. Position argument used for drawing pieces on squares"""
        # Draw baseline board
        self.__draw_board()
        
        # Check for any in game actions - moving piece, highlighting, quitting
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                # Left Click - Move
                if e.button == 1 and (0 <= self.move_origin < 64):
                    self.move_destination = self.__get_square()
                    self.highlighted_squares = []
                    if self.move_destination == self.move_origin:
                        print("Deselecting")
                    else:
                        # Check if move is allowed and make move if so
                        # After move is made find next set of legal moves
                        gs.make_move(self.move_origin, self.move_destination)
                        game_over = gs.is_game_over()
                        gs.find_legal_moves()
                        print(f"Moving piece to {self.move_destination}")
                    self.move_origin = -1
                    self.move_destination = -1
                # Left Click - Select Piece
                elif e.button == 1:
                    self.move_origin = self.__get_square()
                    self.highlighted_squares.append(self.move_origin)
                    print(f"Selected piece at {self.move_origin}")
                # Right Click
                elif e.button == 3:
                    square = self.__get_square()
                    if square in self.highlighted_squares:
                        self.highlighted_squares.remove(square)
                    else:
                        self.highlighted_squares.append(square)

        # Draw current position and refresh
        self.__highlight_squares("gold")
        self.__draw_pieces(gs.get_mailbox64())
        self.clock.tick(self.MAX_FPS)
        pygame.display.flip()

    def __draw_board(self):
        """Draw the 8x8 board"""
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                color = colors[((i+j)%2)]
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(j*self.SQ_SIZE, i*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE)
                )

    def __draw_pieces(self, position: np.ndarray):
        """Draw pieces on board according to current position"""
        for i, key in enumerate(position):
            if key in self.piece_imgs:
                img = self.piece_imgs[key]
                file = i % self.DIMENSION
                rank = self.DIMENSION - int(i / self.DIMENSION) - 1
                self.screen.blit(img, pygame.Rect(file*self.SQ_SIZE, rank*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def __get_square(self):
        pos = pygame.mouse.get_pos()
        file = int(pos[0] / self.SQ_SIZE)
        rank = self.DIMENSION - 1 - int(pos[1] / self.SQ_SIZE)
        square = file + rank*self.DIMENSION
        return square

    def __highlight_squares(self, color: str):
        for square in self.highlighted_squares:
            file = square % self.DIMENSION
            rank = self.DIMENSION - int(square / self.DIMENSION) - 1
            pygame.draw.rect(self.screen, color, pygame.Rect(file*self.SQ_SIZE, rank*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def __load_imgs(self) -> dict:
        """Load images of pieces and map with dictionary"""
        piece_imgs = {}
        for piece in pieces.PieceEnums:
            key = piece.value
            item_str = f"game/imgs/{pieces.PieceEnums(piece).name}.png"
            piece_imgs[key] = pygame.transform.scale(
                pygame.image.load(item_str),
                (self.SQ_SIZE, self.SQ_SIZE)
            )
        return piece_imgs