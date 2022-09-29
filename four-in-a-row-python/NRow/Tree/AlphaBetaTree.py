from __future__ import annotations
import sys
from ..Tree.Tree import Tree
from ..Board import Board
from ..Heuristic.Heuristic import Heuristic

class AlphaBetaTree(Tree):

    def __init__(self, board:Board, depth:int, playerId:int, heuristic:Heuristic, evaluationPlayer:int, gameN:int, alpha:int, beta:int):
        self.alpha = alpha
        self.beta = beta
        super().__init__(board, depth, playerId, heuristic, evaluationPlayer, gameN)
        

    def getValueAndMove(self) -> tuple(int, int):
        children = self.getChildren()
        childrenValues:list(int) =self.getChildrenValues(children)
        if self.playerId == self.evaluationPlayer:
            maxValue = max(map(lambda x: -sys.maxsize-1 if x is None else x, childrenValues))
            return (maxValue, childrenValues.index(maxValue)+1)
        else:
            minValue = min(map(lambda x: sys.maxsize if x is None else x, childrenValues))
            return (minValue, childrenValues.index(minValue)+1)

    def getChildren(self) -> list('Tree'):
        #HERE IMPLEMENT ALPHA BETA PRUNING
        children = []
        nextPlayer = 1 if self.evaluationPlayer == 2 else 2 
        #if this player is max player
        if self.playerId == self.evaluationPlayer:
            bestValue = -sys.maxsize-1
            for col in range(0, self.board.width):
                if self.board.isValid(col):
                    newTree = AlphaBetaTree(self.board.getNewBoard(col, self.evaluationPlayer), self.depth-1, self.playerId, self.heuristic, nextPlayer, self.gameN, self.alpha, self.beta)
                    value = newTree.value
                    bestValue = max( bestValue, value) 
                    self.alpha = max( self.alpha, bestValue)
                    newTree.value = bestValue
                    children.append(newTree)
                    if self.beta <= self.alpha:
                        for i in range(0,self.board.width - col - 1):
                            children.append(None)
                        break
                else:
                    children.append(None)
            return children
        else:
            bestValue = sys.maxsize
            for col in range(0, self.board.width): #[0..6]
                if self.board.isValid(col):
                    newTree = AlphaBetaTree(self.board.getNewBoard(col, self.evaluationPlayer), self.depth-1, self.playerId, self.heuristic, nextPlayer, self.gameN, self.alpha, self.beta)
                    value = newTree.value
                    bestValue = min( bestValue, value) 
                    self.beta = min( self.beta, bestValue)
                    newTree.value = bestValue
                    children.append(newTree)
                    if self.beta <= self.alpha:
                        for i in range(0,self.board.width - col - 1): #[0..6]
                            children.append(None)
                        break
                else:
                    children.append(None)
            return children
    