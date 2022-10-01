from __future__ import annotations
import sys
from ..Tree.Tree import Tree
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic

class AlphaBetaTree(Tree):

    def __init__(self, board:Board, depth:int, player_id:int, heuristic:Heuristic, evaluation_player:int, game_n:int, alpha:int, beta:int):
        self.alpha = alpha
        self.beta = beta
        super().__init__(board, depth, player_id, heuristic, evaluation_player, game_n)
        
    def get_children(self) -> list('Tree'):
        next_player = 1 if self.evaluation_player == 2 else 2 
        if self.player_id == self.evaluation_player:
            return self.max_player_pruning(next_player)
        else:
            return self.min_player_pruning(next_player)

    def max_player_pruning(self, next_player:int):
        children = []
        best_value = -sys.maxsize-1
        for col in range(0, self.board.width):
            if self.board.is_valid(col):
                new_tree = AlphaBetaTree(self.board.get_new_board(col, self.evaluation_player), self.depth-1, self.player_id, self.heuristic, next_player, self.game_n, self.alpha, self.beta)
                value = new_tree.value
                best_value = max( best_value, value) 
                self.alpha = max( self.alpha, best_value)
                new_tree.value = best_value
                children.append((new_tree, col))
                if self.beta <= self.alpha:
                    break
        return children

    def min_player_pruning(self, next_player:int):
        children = []
        best_value = sys.maxsize
        for col in range(0, self.board.width): #[0..6]
            if self.board.is_valid(col):
                new_tree = AlphaBetaTree(self.board.get_new_board(col, self.evaluation_player), self.depth-1, self.player_id, self.heuristic, next_player, self.game_n, self.alpha, self.beta)
                value = new_tree.value
                best_value = min( best_value, value) 
                self.beta = min( self.beta, best_value)
                new_tree.value = best_value
                children.append((new_tree, col))
                if self.beta <= self.alpha:
                    break
        return children
    