from __future__ import annotations
from ..Board import Board
from ..Heuristic import Heuristic
from .PlayerController import PlayerController


class minMaxPlayer(PlayerController):

    def __init__(self, playerId:int, gameN:int, depth:int, heuristic:Heuristic):
        super().__init__(playerId, gameN, heuristic)
        self.depth = depth

    def makeMove(self, board:Board) -> int:
        """_summary_

        Args:
            board (Board): _description_

        Returns:
            int: _description_
        """
        board.printBoard()
        tree = Tree(Board(board=board), self.depth, self.playerId, self.heuristic, self.playerId)
        if Heuristic is not None:
            print("heuristic " + self.heuristic.__str__() + " calculated the best move is: "
             + str(tree.getMove()))
        print("Player " + self.__str__() + "\nWhich column would you like to play in?")
        
        column = int(input())
        print(f"Selected Column: {column}")
        return column - 1

class Tree:

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int):
        """_summary_

        Args:
            board (Board): _description_
            depth (int): _description_
            playerId (int): _description_
            heuristic (Heuristic): _description_
            evaluationPlayer (int): _description_
        """
        if depth != 0:
            children = []
            nextPlayer = 1 if evaluationPlayer == 2 else 2 
            for col in range(0, board.width):
                children.append(Tree(board.getNewBoard(col, evaluationPlayer), depth-1, playerId, heuristic, nextPlayer))
            self.value, self.move = self.getMinMaxValueAndMove(playerId, evaluationPlayer, children)
        else:
            self.leaf = True
            self.value = heuristic.evaluateBoard(playerId, board)
            self.move = -1


    def getMinMaxValueAndMove(self, playerId:int, evaluationPlayer:int, children:list('Tree')) -> tuple(int, int):
        """_summary_

        Args:
            self (_type_): _description_
            int (_type_): _description_

        Returns:
            _type_: _description_
        """
        childrenValues:list(int) = self.getChildrenValues(children)
        if playerId == evaluationPlayer:
            maxValue = max(childrenValues)
            return (maxValue, childrenValues.index(maxValue)+1)
        else:
            minValue = min(childrenValues)
            return (minValue, childrenValues.index(minValue)+1)


    def getChildrenValues(self, children:list()):
        """_summary_

        Args:
            children (list): _description_

        Returns:
            _type_: _description_
        """
        return list(map(lambda x: x.getEvaluation(), children))


    def getEvaluation(self) -> int:
        return self.value

    def getMove(self) -> int:
        return self.move





