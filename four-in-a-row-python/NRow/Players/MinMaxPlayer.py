from NRow.Board import Board
from NRow.Heuristic import Heuristic
import PlayerController

class minMaxPlayer(PlayerController):

    def __init__(self, playerId:int, gameN:int, depth:int, heuristic:Heuristic):
        super().__init__(playerId, gameN, heuristic)
        self.depth = depth

    def makeMove(self, board:Board) -> int:
        #evaluate board
        #find best move based on player
        pass