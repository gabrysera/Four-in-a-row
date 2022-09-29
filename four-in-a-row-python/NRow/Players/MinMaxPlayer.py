from __future__ import annotations
from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController
from ..Tree.MinMaxTree import MinMaxTree

class MinMaxPlayer(PlayerController):

    def __init__(self, playerId:int, gameN:int, depth:int, heuristic:Heuristic):
        super().__init__(playerId, gameN, heuristic)
        self.depth = depth

    def makeMove(self, board:Board) -> int:
        board.printBoard()
        tree = MinMaxTree(Board(board=board), self.depth, self.playerId, self.heuristic, self.playerId, self.gameN)
        column = tree.getMove()
        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(column))

        return column - 1

