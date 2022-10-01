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
        board.print_board()
        tree = MinMaxTree(Board(board=board), self.depth, self.player_id, self.heuristic, self.player_id, self.game_n)
        column = tree.get_move()
        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(column))

        return column - 1

