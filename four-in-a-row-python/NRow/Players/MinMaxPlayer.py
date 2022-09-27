from __future__ import annotations
from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController
from ..Tree.MinMaxTree import MinMaxTree

class minMaxPlayer(PlayerController):

    def __init__(self, playerId:int, gameN:int, depth:int, heuristic:Heuristic):
        super().__init__(playerId, gameN, heuristic)
        self.depth = depth

    def makeMove(self, board:Board) -> int:
        """_summary_

        Args:
            board (Board): _description_

        Returns:
            int: _description_
        """
        board.printBoard()
        tree = MinMaxTree(Board(board=board), self.depth, self.playerId, self.heuristic, self.playerId)
        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(tree.getMove()))
        print("Player " + self.__str__() + "\nWhich column would you like to play in?")
        
        column = int(input())
        print(f"Selected Column: {column}")
        return column - 1

