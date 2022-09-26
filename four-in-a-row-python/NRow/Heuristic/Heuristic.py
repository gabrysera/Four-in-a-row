from __future__ import annotations
import sys
from abc import ABC, abstractmethod
from ..Board import Board

class Heuristic(ABC):

    def __init__(self, gameN) -> None:
        self.gameN = gameN
        self.evalCount = 0
    
    def getEvalCount(self) -> int:
        return self.evalCount


    def getBestAction(self, player:int, board:Board) -> int:
        """Determines the best column for the next move

        Args:
            player (int): the player for which to compute the heuristic values
            board (Board): the board to evaluate

        Returns:
            int: column integer
        """
        utilities = self.evalActions(player, board)
        best_action = 0
        for i in range(0, len(utilities)):
            best_action = i if utilities[i] > utilities[best_action] else best_action

        return best_action

    def evalActions(self, player:int, board:Board) -> list(int):
        """Helper function to determines the utility of each column

        Args:
            player (int): the player for which to compute the heuristic values
            board (int): the board to evaluate

        Returns:
            list(int): list of size boardWidth with utilities
        """
        utilities = []
        for i in range(0, board.width):
            utilities.append(self.evaluateAction(player, i, Board(board=board)))
        return utilities

    def evaluateAction(self, player:int, action:int, board:Board) -> int:
        """Helper function to assign a utility to an action

        Args:
            player (int): the player for which to compute the heuristic values
            action (int): the action to evaluate
            board (Board): the board to evaluate

        Returns:
            int: the utility, negative 'infinity' if the move is invalid
        """

        if board.isValid:
            self.evalCount += 1
            value = self.evaluateBoard(player, board.getNewBoard(action, player))
            return value
        else:
            return -sys.maxint-1

    def evaluateBoard(self, player:int, board:Board) -> int:
        """Helper function to assign a utility to a board

        Args:
            player (int): the player for which to compute the heuristic values
            board (Board): the board to evaluate

        Returns:
            int: the utility
        """

        self.evalCount += 1
        return self.evaluate(player, board)

    def __str__(self) -> str:
        return ""

    @abstractmethod
    def evaluate(self, player:int, board:Board) -> int:
        pass
