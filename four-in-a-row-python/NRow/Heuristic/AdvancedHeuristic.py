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
        
        opponent_player = 1 if player == 2 else 2
        max_in_row = 0
        local_max = 0
        for i in range(0, len(board_state)):
            for j in range(0, len(board_state[i])):
                if board_state[i][j] == player:
                    max_in_row =  max(max_in_row, 1)
                    for x in range(1, len(board_state) - i): #horizontal
                        if board_state[i + x][j] == player:# and self.horizontal_not_blocked(board_state,i,j,x,opponent_player): #not blocked 
                            local_max = max(max_in_row, x+1, local_max)
                            #max_in_row = max(max_in_row, x + 1)
                        else:
                            if self.horizontal_not_blocked(board_state,i,j,x,opponent_player):
                                max_in_row = max(max_in_row, local_max)
                                local_max = 0
                            break
                    for y in range(1, len(board_state[0]) - j): #vertical
                        if board_state[i][j + y] == player:# and self.vertical_not_blocked(board_state, i, j, y, opponent_player):
                            local_max = max(max_in_row, y+1, local_max)
                            #max_in_row = max(max_in_row, y + 1)
                        else:
                            if board_state[i][j+y] == 0 or y == self.game_n:#self.vertical_not_blocked(board_state, i, j, y, opponent_player):
                                max_in_row = max(max_in_row, local_max)
                                local_max = 0
                            break
                    for d in range(1, min(len(board_state) - i, len(board_state[0]) - j)): #ascending diagonal 
                        if board_state[i + d][j + d] == player and self.ascending_diagonal_not_blocked(board_state, i, j, d, opponent_player):
                            max_in_row = max(max_in_row, d + 1)
                        else:
                            break
                    for a in range(1, min(len(board_state) - i, j)): #descending diagonal
                        if board_state[i + a][j - a] == player:
                            max_in_row = max(max_in_row, a + 1)
                        else:
                            break
        return max_in_row

    def horizontal_not_blocked(self, board_state:list(list(int)), col:int, row:int, number_of_squares:int, opponent_player:int) -> bool:
        return (
            number_of_squares == self.game_n or 
            not(
                (col-1 < 0 or board_state[col - 1][row] == opponent_player) and 
                (col + number_of_squares + 1 >= len(board_state) or board_state[col+number_of_squares+1][row] == opponent_player)
            )
        )

    def vertical_not_blocked(self, board_state:list(list(int)), col:int, row:int, number_of_squares:int, opponent_player:int) -> bool:
        print(row + number_of_squares)
        return (
            number_of_squares == self.game_n or
            not(
                row + number_of_squares  >= len(board_state[0] or board_state[col][row + number_of_squares] == opponent_player)
            )
        )
        
    def ascending_diagonal_not_blocked(self, board_state:list(list(int)), col:int, row:int, number_of_squares:int, opponent_player:int) -> bool:
        return (
            number_of_squares == self.game_n or
            not(
                (row + number_of_squares + 1 >= len(board_state[0]) or col + number_of_squares + 1 >= len(board_state) or board_state[col+number_of_squares + 1][row + number_of_squares + 1] == opponent_player) and
                (col-1 < 0 or row - 1 < 0 or board_state[col - 1][row - 1] == opponent_player)

            )
        )

    def discending_diagonal_not_blocked(self, board_state:list(list(int)), col:int, row:int, number_of_squares:int, opponent_player:int) -> bool:
        pass