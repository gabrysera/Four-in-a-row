from __future__ import annotations
from ..Tree.Tree import Tree
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic

class MinMaxTree(Tree):

    def __init__(self, board:Board, depth:int, player_id:int, heuristic:Heuristic, evaluation_player:int, game_n:int):
        super().__init__(board, depth, player_id, heuristic, evaluation_player, game_n)

    def get_children(self) -> list(tuple('Tree', int)):
        """Gets the possible game states that can be transitioned to from the current state

        Returns:
            list(tuple('Tree', int)): the list of game states along with the move that transitions to them
        """
        children = []
        next_player = 1 if self.evaluation_player == 2 else 2 
        for col in range(0, self.board.width):
            if self.board.is_valid(col):
                new_tree = MinMaxTree(self.board.get_new_board(col, self.evaluation_player), self.depth-1, self.player_id, self.heuristic, next_player, self.game_n)
                children.append((new_tree, col))
        return children