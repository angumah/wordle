from Model.board import Board

from View.gameView import GameView
class Wordle:

    def __init__(self, board, view):
        '''
        Constructor for Wordle gameplay. Takes in board object
        '''
        self.board = board
        self.view = view



    
    def run(self):
        self.view.renderBoard()
