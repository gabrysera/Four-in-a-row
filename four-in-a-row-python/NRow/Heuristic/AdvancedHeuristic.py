from __future__ import annotations
import sys
from . import Heuristic
from ..Board import Board
from ..Game import Game
from .Heuristic import Heuristic

class AdvancedHeuristic(Heuristic):

    def __init__(self, game_n) -> None:
        super().__init__(game_n)
        self.name = "Advanced"
        self.scalar = int(len(self.board_state)/2) 
        self.board_values = self.compute_board_heuristic()

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
        self.board_state = board_state
        winning = Game.winning(board_state, self.game_n)
        if winning == player:
            return sys.maxsize
        elif winning != 0:
            return -sys.maxsize-1
        

        
        max_in_row = 0
        self.opponent_player = 1 if player == 2 else 2
        for i in range(0, len(board_state)):
            for j in range(0, len(board_state[i])):
                if board_state[i][j] == player:
                    max_in_row = max(max_in_row, self.scalar + self.board_values[i][j])
                    for x in range(1, len(board_state) - i):
                        if board_state[i + x][j] == player:
                            max_in_row = max(max_in_row, self.scalar * (x + 1) + self.board_values[i+x][j])
                        else:
                            break
                    for y in range(1, len(board_state[0]) - j):
                        if board_state[i][j + y] == player:
                            max_in_row = max(max_in_row, self.scalar * (y + 1) + self.board_values[i][j+y])
                        else:
                            break
                    for d in range(1, min(len(board_state) - i, len(board_state[0]) - j)):
                        if board_state[i + d][j + d] == player:
                            max_in_row = max(max_in_row, self.scalar * (d + 1) + self.board_values[i+d][j+d])
                        else:
                            break
                    for a in range(1, min(len(board_state) - i, j)):
                        if board_state[i + a][j - a] == player:
                            max_in_row = max(max_in_row, self.scalar * (a + 1) + self.board_values[i+a][j-a])
                        else:
                            break
        return max_in_row

    def compute_board_heuristic(self) -> list(list(int)):
        
        if len(self.board_state) % 2 == 0:
            i_values = [x for x in range(int(len(self.board_state)/2))]
            i_values = list(map(lambda x: x*self.scalar, i_values + i_values.copy()[::-1]))
        else:
            i_values = [x for x in range(int(len(self.board_state)/2))]
            i_values = list(map(lambda x: x*self.scalar, i_values + [i_values[-1]] + i_values.copy()[::-1]))

        if len(self.board_state[0]) % 2 == 0:
            j_values = [x for x in range(int(len(self.board_state[0])/2))]
            j_values = list(map(lambda x: x*self.scalar, j_values + j_values.copy()[::-1]))
        else:
            j_values = [x for x in range(int(len(self.board_state[0])/2))]
            j_values = list(map(lambda x: x*self.scalar, j_values + [j_values[-1]] + j_values.copy()[::-1]))

        board_values = []
        for i in range(0,len(self.board_state)):
            board_values.append([])
            for j in range(0,int(len(self.board_state[0]))):
                board_values[i].append((i_values[i] + j_values[j]))
        return board_values