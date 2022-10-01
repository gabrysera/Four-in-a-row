from __future__ import annotations
from abc import ABC, abstractmethod
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic
from ..Game import Game

class Tree(ABC):

    def __init__(self, board:Board, depth:int, player_id:int, heuristic:Heuristic, evaluation_player:int, game_n:int):
        self.value = 0
        self.board = board
        self.depth = depth
        self.player_id = player_id
        self.heuristic = heuristic
        self.evaluation_player = evaluation_player
        self.game_n = game_n

        if depth != 0 and not self.someone_won(board, game_n):
            self.value, self.move = self.get_value_and_move()
        else:
            self.value = heuristic.evaluate_board(player_id, board)
            self.move = -1

    def get_value_and_move(self) -> tuple(int, int):
        """Returns the best move and its value

        Returns:
            tuple(int, int): the best value obtainable and the move that has that evaluation
        """
        children_values:list(tuple(int, int)) = self.get_children_values(self.get_children())
        if self.player_id == self.evaluation_player:
            max_value = max(children_values, key=lambda x: x[0]) # wouldn't python already sort based on the first elem of the tuple? (--->int<---, int)
            return max_value
        else:
            min_value = min(children_values, key=lambda x: x[0])
            return min_value
    
    @abstractmethod
    def get_children(self, board:Board, depth:int, player_id:int, heuristic:Heuristic, evaluation_player:int, game_n:int) -> list('Tree'):
        pass

    def get_children_values(self, children:list()) -> list(tuple(int, int)):
        return list(map(lambda child: (child[0].get_value(), child[1]), children))

    def get_value(self):
        return self.value

    def get_move(self):
        return self.move + 1

    def someone_won(self, board:Board, game_n:int) -> bool:
        return Game.winning(board.get_board_state(), game_n) != 0