from __future__ import annotations
import sys
from abc import ABC, abstractmethod
from ..Board import Board

class Heuristic(ABC):

    def __init__(self, game_n) -> None:
        self.game_n = game_n
        self.evalCount = 0
    
    def get_eval_count(self) -> int:
        return self.evalCount


    def get_best_action(self, player:int, board:Board) -> int:
        """Determines the best column for the next move

        Args:
            player (int): the player for which to compute the heuristic values
            board (Board): the board to evaluate

        Returns:
            int: column integer
        """
        utilities = self.eval_actions(player, board)
        best_action = 0
        for i in range(0, len(utilities)):
            best_action = i if utilities[i] > utilities[best_action] else best_action

        return best_action

    def eval_actions(self, player:int, board:Board) -> list(int):
        """Helper function to determines the utility of each column

        Args:
            player (int): the player for which to compute the heuristic values
            board (int): the board to evaluate

        Returns:
            list(int): list of size boardWidth with utilities
        """
        utilities = []
        for i in range(0, board.width):
            utilities.append(self.evaluate_action(player, i, Board(board=board)))
        return utilities

    def evaluate_action(self, player:int, action:int, board:Board) -> int:
        """Helper function to assign a utility to an action

        Args:
            player (int): the player for which to compute the heuristic values
            action (int): the action to evaluate
            board (Board): the board to evaluate

        Returns:
            int: the utility, negative 'infinity' if the move is invalid
        """

        if board.is_valid:
            self.evalCount += 1
            value = self.evaluate_board(player, board.get_new_board(action, player))
            return value
        else:
            return -sys.maxint-1

    def evaluate_board(self, player:int, board:Board) -> int:
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

