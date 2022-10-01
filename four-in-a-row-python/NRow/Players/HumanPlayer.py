from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController

class HumanPlayer(PlayerController):

    def __init__(self, player_id:int, game_n:int, heuristic:Heuristic):
        super().__init__(player_id, game_n, heuristic)

    #Show the human player the current board and ask them for their next move
    def make_move(self, board:Board) -> int:
        board.print_board()

        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(self.heuristic.get_best_action(self.player_id, Board(board=board)) + 1))
        print("Player " + self.__str__() + "\nWhich column would you like to play in?")

        column = int(input())
        print(f"Selected Column: {column}")
        return column-1