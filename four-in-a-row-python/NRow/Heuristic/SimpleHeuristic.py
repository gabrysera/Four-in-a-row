from __future__ import annotations
import sys
from . import Heuristic
from ..Board import Board
from ..Game import Game
from .Heuristic import Heuristic


class SimpleHeuristic(Heuristic):
    
    def __init__(self, game_n) -> None:
        super().__init__(game_n)
        self.name = "Simple"

    def __str__(self) -> str:
        return super().__str__() + self.name

    def evaluate(self, player:int, board:Board) -> int:
        """Determinte utility of a board state

        Args:
            player (int): the player for which to compute the heuristic values
            board (Board): the board to be evaluated

        Returns:
            int: the utility
        """

        board_state = board.get_board_state()
        winning = Game.winning(board_state, self.game_n)
        if winning == player:
            return sys.maxsize
        elif winning != 0:
            return -sys.maxsize-1

        # If not winning or losing, return highest number of claimed squares in a row

        max_in_row = 0
        for i in range(0, len(board_state)):
            for j in range(0, len(board_state[i])):
                if board_state[i][j] == player:
                    max_in_row =  max(max_in_row, 1)
                    for x in range(1, len(board_state) - i):
                        if board_state[i + x][j] == player:
                            max_in_row = max(max_in_row, x + 1)
                        else:
                            break
                    for y in range(1, len(board_state[0]) - j):
                        if board_state[i][j + y] == player:
                            max_in_row = max(max_in_row, y + 1)
                        else:
                            break
                    for d in range(1, min(len(board_state) - i, len(board_state[0]) - j)):
                        if board_state[i + d][j + d] == player:
                            max_in_row = max(max_in_row, d + 1)
                        else:
                            break
                    for a in range(1, min(len(board_state) - i, j)):
                        if board_state[i + a][j - a] == player:
                            max_in_row = max(max_in_row, a + 1)
                        else:
                            break
        return max_in_row
