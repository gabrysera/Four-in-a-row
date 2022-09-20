from . import Heuristic
from ..Board import Board
class SimpleHeuristic(Heuristic):
    def __init__(self, gameN) -> None:
        super().__init__(gameN)
        self.name = "Simple"

    def __str__(self) -> str:
        return super().__str__() + self.name

    def evaluate(self, player:int, board:Board) -> int:
        pass
