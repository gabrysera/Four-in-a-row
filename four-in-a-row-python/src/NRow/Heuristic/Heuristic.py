from abc import ABC, abstractmethod

from sympy import evaluate
from ..Board import Board
class Heuristic(ABC):
    #missing name attribute (which is an abstract attribute in Java)
    #missing __str__ implementation

    def __init__(self, gameN) -> None:
        self.gameN = gameN
        self.evalCount = 0
    
    def get_best_action(self, player:int, board:Board) -> int:
        pass

    def eval_actions(self, player:int, board:Board) -> list(int):
        pass

    def evaluate_action(self, player:int, action:int, board:Board) -> int:
        if board.isValid:
            self.evalCount += 1
            value = self.evaluate_board(player, board.getNewBoard(action, player))
            return value
        else:
            return -1 #this has to be min value

    def evaluate_board(self, player:int, board:Board) -> int:
        self.evalCount += 1
        return evaluate(player, board)

    @abstractmethod
    def evaluate(self, player:int, board:Board) -> int:
        pass

