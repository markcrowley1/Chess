"""
Description:
    Main script for chess program
"""

from game.gui import GUI
from game.gamestate import GameState

def main():
    gui = GUI()
    gs = GameState("8/8/8/4b3/8/8/4r3/Q7 w KQkq - 0 1")

    while gui.running is True:
        gui.update(gs)
    
if __name__ == "__main__":
    main()