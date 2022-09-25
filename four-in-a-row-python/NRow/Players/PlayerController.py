from __future__ import annotations
from abc import ABC, abstractmethod
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic


class PlayerController(ABC):
    
    #constructor
    def __init__(self, playerId:int, gameN:int, heuristic:Heuristic):
        self.playerId = playerId
        self.gameN = gameN
        self.heuristic = heuristic

    #how many time the heuristic was used to evaluate a boardstate
    def getEvalCount(self):
        return self.heuristic.getEvalCount()

    #string representation of player for board
    def __str__(self):
        if self.playerId == 2:
            return "O"
        else:
            return "X"

    #abstract method for player classes
    @abstractmethod
    def makeMove(self, board:Board) -> int:
        pass
