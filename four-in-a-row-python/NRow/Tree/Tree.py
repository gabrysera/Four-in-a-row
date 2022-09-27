from __future__ import annotations
import sys
from abc import ABC, abstractmethod
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic
from ..Game import Game

class Tree(ABC):

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int, gameN:int):
        self.value = 0

        if depth != 0 and not self.someoneWon(board, gameN):
            self.children = self.getChildren(board, depth, playerId, heuristic, evaluationPlayer, gameN)
            self.value, self.move = self.getValueAndMove(playerId, evaluationPlayer, self.children)
        else:
            self.value = heuristic.evaluateBoard(playerId, board)
            self.move = -1
        
    def getChildren(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int, gameN:int) -> list('Tree'):
        children = []
        nextPlayer = 1 if evaluationPlayer == 2 else 2 
        for col in range(0, board.width):
            if board.isValid(col):
                newTree = self.__class__(board.getNewBoard(col, evaluationPlayer), depth-1, playerId, heuristic, nextPlayer, gameN)
                children.append(newTree)
                self.value = max(self.value, children[-1].getValue())
            else:
                children.append(None)
        return children

    @abstractmethod
    def getValueAndMove(self, playerId:int, evaluationPlayer:int, children:list('Tree')) -> tuple(int, int):
        pass

    def getChildrenValues(self, children:list()):
        return list(map(lambda x: x.getValue() if x != None else -sys.maxsize-1, children))

    def getValue(self):
        return self.value

    def getMove(self):
        return self.move

    def someoneWon(self, board:Board, gameN:int) -> bool:
        return Game.winning(board.getBoardState(), gameN) != 0
        pass