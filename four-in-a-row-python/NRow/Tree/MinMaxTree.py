from __future__ import annotations
from ..Tree.Tree import Tree
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic

class MinMaxTree(Tree):

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int):
        super().__init__(board, depth, playerId, heuristic, evaluationPlayer)

    def getValueAndMove(self, playerId:int, evaluationPlayer:int, children:list('Tree')) -> tuple(int, int):
        childrenValues:list(int) = self.getChildrenValues(children)
        if playerId == evaluationPlayer:
            maxValue = max(childrenValues)
            return (maxValue, childrenValues.index(maxValue)+1)
        else:
            minValue = min(childrenValues)
            return (minValue, childrenValues.index(minValue)+1)