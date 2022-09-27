from __future__ import annotations
from abc import ABC, abstractmethod
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic


class Tree(ABC):

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int):
      
        self.board = board
        self.depth = depth
        if depth != 0:
            self.children = self.getChildren(board, depth, playerId, heuristic, evaluationPlayer)
            self.value, self.move = self.getValueAndMove(playerId, evaluationPlayer, self.children)
        else:
            self.value = heuristic.evaluateBoard(playerId, board)
            self.move = -1
        
    def getChildren(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int) -> list('Tree'):
        children = []
        nextPlayer = 1 if evaluationPlayer == 2 else 2 
        for col in range(0, board.width):
            newTree = self.__class__(board.getNewBoard(col, evaluationPlayer), depth-1, playerId, heuristic, nextPlayer)
            children.append(newTree)
        return children

    @abstractmethod
    def getValueAndMove(self, playerId:int, evaluationPlayer:int, children:list('Tree')) -> tuple(int, int):
        pass

    def getChildrenValues(self, children:list()):
        return list(map(lambda x: x.getEvaluation(), children))

    def getEvaluation(self):
        return self.value

    def getMove(self):
        return self.move