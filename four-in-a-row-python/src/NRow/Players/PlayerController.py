import abc
from NRow.Board import Board
from NRow.Heuristic import Heuristic

from __future__ import annotations

class PlayerController(abc.ABCMeta):
    
    #constructor
    def __init__(self, playerId:int, gameN:int, heuristic:Heuristic):
        self.playerId = playerId
        self.gameN = gameN
        self.heuristic = heuristic

    #how many time the heuristic was used to evaluate a boardstate
    def getEvalCount(self):
        return Heuristic.getEvalCount()

    #string representation of player for board
    def toString(self):
        if self.playerId == 2:
            return "O"
        else:
            return "X"

    #abstract method for player classes
    @abc.abstractmethod
    def makeMove(self, board:Board) -> int:
        pass
