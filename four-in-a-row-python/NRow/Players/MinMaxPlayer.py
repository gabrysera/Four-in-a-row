from __future__ import annotations
from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController
from ..Tree import Tree

class minMaxPlayer(PlayerController):

    def __init__(self, playerId:int, gameN:int, depth:int, heuristic:Heuristic):
        super().__init__(playerId, gameN, heuristic)
        self.depth = depth

    def makeMove(self, board:Board) -> int:
        #evaluate board
        #find best move based on player
        #we go for example with depth of 5 moves, then based on heuristic we evaluate and we evaluate all the 
        #board states till that depth and then choose
        board.printBoard()
        tree = Tree(Board(board=board), self.depth, self.playerId, self.heuristic, self.playerId)
        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(tree.getMove()))
        print("Player " + self.__str__() + "\nWhich column would you like to play in?")
        
        column = int(input())
        print(f"Selected Column: {column}")
        return column - 1





