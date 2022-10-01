from __future__ import annotations
from ..Tree.Tree import Tree
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic

class MinMaxTree(Tree):

    def __init__(self, board:Board, depth:int, player_id:int, heuristic:Heuristic, evaluation_player:int, game_n:int):
        super().__init__(board, depth, player_id, heuristic, evaluation_player, game_n)

    def get_children(self) -> list(tuple('Tree', int)):
        children = []
        next_player = 1 if self.evaluation_player == 2 else 2 
        for col in range(0, self.board.width):
            if self.board.is_valid(col):
                newTree = MinMaxTree(self.board.get_new_board(col, self.evaluation_player), self.depth-1, self.player_id, self.heuristic, next_player, self.game_n)
                children.append((newTree, col))
        return children