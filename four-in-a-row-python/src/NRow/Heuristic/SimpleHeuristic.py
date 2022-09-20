from . import Heuristic
from ..Board import Board
class SimpleHeuristic(Heuristic):
    def __init__(self, gameN) -> None:
        super().__init__(gameN)

    def evaluate(self, player:int, board:Board) -> int:
        pass
