from __future__ import annotations
from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController
from ..Tree.MinMaxTree import MinMaxTree

class MinMaxPlayer(PlayerController):

    def __init__(self, player_id:int, game_n:int, depth:int, heuristic:Heuristic):
        super().__init__(player_id, game_n, heuristic)
        self.depth = depth

    def make_move(self, board:Board) -> int:
        """Use the MinMax algorithm to fill the game tree and select the best move according to the heuristic

        Args:
            board (Board): the board where the move will be played

        Returns:
            int: the columm where the piece will be placed
        """
        tree = MinMaxTree(Board(board=board), self.depth, self.player_id, self.heuristic, self.player_id, self.game_n)
        column = tree.get_move()

        return column - 1

