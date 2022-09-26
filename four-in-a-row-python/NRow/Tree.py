from __future__ import annotations
from .Board import Board
from .Heuristic import Heuristic


class Tree:

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int):
      
        self.board = board
        self.depth = depth
        if depth != 0:
            self.children = self.getChildren(board, depth, playerId, heuristic, evaluationPlayer)
            self.value, self.move = self.evaluateChildren(playerId, evaluationPlayer, self.children)
        else:
            self.leaf = True
            self.value = heuristic.evaluateBoard(playerId, board)
            self.move = -1
        

    def getChildren(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int) -> list('Tree'):

        children = []
        nextPlayer = 1 if evaluationPlayer == 2 else 2 
        for col in range(0, board.width):
            newTree = Tree(board.getNewBoard(col, evaluationPlayer), depth-1, playerId, heuristic, nextPlayer)
            children.append(newTree)
        return children

    def evaluateChildren(self, playerId:int, evaluationPlayer:int, children:list('Tree')) -> tuple(int, int):
        childrenValues:list(int) = self.getChildrenValues(children)
        if self.depth > 1:
            print(childrenValues, self.depth)
        if playerId == evaluationPlayer:
            maxValue = max(childrenValues)
            return (maxValue, childrenValues.index(maxValue)+1)
        else:
            minValue = min(childrenValues)
            return (minValue, childrenValues.index(minValue)+1)

            
    def getChildrenValues(self, children:list()):
        return list(map(lambda x: x.getEvaluation(), children))


    def getEvaluation(self):
        return self.value

    def getMove(self):
        return self.move