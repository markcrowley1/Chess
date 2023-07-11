"""
Description:
    Main script for chess program
"""

from game.gui import GUI
from game.gamestate import GameState

def main():
    gui = GUI()
    gs = GameState()

    while gui.running is True:
        gui.update(gs.get_mailbox64())
    
if __name__ == "__main__":
    main()