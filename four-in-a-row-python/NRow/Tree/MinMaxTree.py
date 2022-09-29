from __future__ import annotations
from ..Tree.Tree import Tree
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic
import sys
class MinMaxTree(Tree):

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int, gameN:int):
        super().__init__(board, depth, playerId, heuristic, evaluationPlayer, gameN)

    def getValueAndMove(self) -> tuple(int, int):
        childrenValues:list(int) = self.getChildrenValues(self.getChildren())
        if self.playerId == self.evaluationPlayer:
            maxValue = max(map(lambda x: -sys.maxsize-1 if x is None else x, childrenValues))
            return (maxValue, childrenValues.index(maxValue)+1)
        else:
            minValue = min(map(lambda x: sys.maxsize if x is None else x, childrenValues))
            return (minValue, childrenValues.index(minValue)+1)

    def getChildren(self) -> list('Tree'):
        children = []
        nextPlayer = 1 if self.evaluationPlayer == 2 else 2 
        for col in range(0, self.board.width):
            if self.board.isValid(col):
                newTree = MinMaxTree(self.board.getNewBoard(col, self.evaluationPlayer), self.depth-1, self.playerId, self.heuristic, nextPlayer, self.gameN)
                children.append(newTree)
            else:
                children.append(None)
        return children