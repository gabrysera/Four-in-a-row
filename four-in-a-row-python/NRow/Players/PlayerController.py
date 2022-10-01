from __future__ import annotations
from abc import ABC, abstractmethod
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic


class PlayerController(ABC):
    
    #constructor
    def __init__(self, player_id:int, game_n:int, heuristic:Heuristic):
        self.player_id = player_id
        self.game_n = game_n
        self.heuristic = heuristic

    #how many time the heuristic was used to evaluate a boardstate
    def get_eval_count(self):
        return self.heuristic.get_eval_count()

    #string representation of player for board
    def __str__(self):
        if self.player_id == 2:
            return "O"
        else:
            return "X"

    #abstract method for player classes
    @abstractmethod
    def make_move(self, board:Board) -> int:
        pass
