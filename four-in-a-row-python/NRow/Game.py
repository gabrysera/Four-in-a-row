from __future__ import annotations
from .Players.PlayerController import PlayerController
from .Board import Board



class Game:

    def __init__(self, gameN:int, boardWidth:int, boardHeight:int, players:list(PlayerController)):
        assert(boardWidth % 2 != 0)
        self.gameN = gameN
        self.players = players
        self.winner = -1
        self.gameBoard:Board = Board(boardWidth, boardHeight)

    #start game and keep make players move until game is finished, return the idplayer that win
    def startGame(self) -> int:
        print("start game!")
        currentPlayer = 0

        while(not self.isOver()):
            if self.gameBoard.play(self.players[currentPlayer].makeMove(self.gameBoard), self.players[currentPlayer].playerId):
                currentPlayer = 1 if currentPlayer == 0 else 0
            else:
                print("Illegal move!!")

        self.gameBoard.printBoard()
        if self.winner < 0:
            print("game is a draw")
        else:
            print(f"Player {self.players[self.winner-1].__str__()} won!")
        print(f"Player {self.players[0].__str__()} evaluated the board {self.players[0].getEvalCount()} times")
        print(f"Player {self.players[1].__str__()} evaluated the board {self.players[1].getEvalCount()} times")

    #function that determine if the game is over
    def isOver(self) -> bool:
        self.winner = Game.winning(self.gameBoard.getBoardState(), self.gameN)
        return self.winner != 0

    #determines if a player has won, if so return his playerId
    def winning(board:list(list(int)), gameN:int) -> int:

        #vertical check
        for i in range(0, len(board)):
            for j in range(0, len(board[i]) - gameN + 1):
                if(board[i][j] != 0):
                    player = board[i][j]
                    for x in range(1, gameN):
                        if board[i][j+x] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #horizontal check
        for i in range(0, len(board)-gameN+1):
            for j in range(0, len(board[i])):
                if board[i][j] != 0:
                    player = board[i][j]
                    for x in range(1,gameN):
                        if board[i+x][j] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #ascending diagonal check
        for i in range(0, len(board) - gameN + 1):
            for j in range(len(board[i]) - 1, gameN - 1, -1):
                if board[i][j] != 0:
                    player = board[i][j]
                    for x in range(1,gameN):
                        if board[i+x][j-x] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #descending diagonal check
        for i in range(0, len(board) - gameN + 1):
            for j in range(len(board[i])- gameN + 1):
                if board[i][j] != 0:
                    player = board[i][j]
                    for x in range(1,gameN):
                        if board[i+x][j+x] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #check for a draw
        for i in range(0,len(board)):
            if board[i][0] == 0:
                return 0 #board not full yet
        return -1 #is a draw
            