from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController

class HumanPlayer(PlayerController):

    def __init__(self, playerID:int, gameN:int, heuristic:Heuristic):
        super().__init__(playerID, gameN, heuristic)

    #Show the human player the current board and ask them for their next move
    def makeMove(self, board:Board) -> int:
        board.printBoard()

        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(self.heuristic.getBestAction(self.playerId, Board(board=board)) + 1))
        print("Player " + self.__str__() + "\nWhich column would you like to play in?")

        column = int(input())
        print(f"Selected Column: {column}")
        return column-1