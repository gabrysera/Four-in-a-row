from __future__ import annotations
import sys
from abc import ABC, abstractmethod
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic
from ..Game import Game

class Tree(ABC):

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int, gameN:int):
        self.value = 0
        self.board = board
        self.depth = depth
        self.playerId = playerId
        self.heuristic = heuristic
        self.evaluationPlayer = evaluationPlayer
        self.gameN = gameN

        if depth != 0 and not self.someoneWon(board, gameN):
            self.value, self.move = self.getValueAndMove()
        else:
            self.value = heuristic.evaluateBoard(playerId, board)
            self.move = -1

    @abstractmethod
    def getValueAndMove(self, playerId:int, evaluationPlayer:int, children:list('Tree')) -> tuple(int, int):
        pass
    
    @abstractmethod
    def getChildren(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int, gameN:int) -> list('Tree'):
        pass

    def getChildrenValues(self, children:list()):
        return list(map(lambda x: x.getValue() if x != None else None, children))

    def getValue(self):
        return self.value

    def getMove(self):
        return self.move

    def someoneWon(self, board:Board, gameN:int) -> bool:
        return Game.winning(board.getBoardState(), gameN) != 0
        pass