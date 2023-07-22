"""
Description:
    Main script for chess program
"""

from game.gui import GUI
from game.gamestate import GameState

def main():
    gui = GUI()
    gs = GameState("8/q7/8/8/8/8/8/6K1 w KQkq - 0 1")

    while gui.running is True:
        gui.update(gs)
    
if __name__ == "__main__":
    main()