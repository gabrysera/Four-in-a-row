from __future__ import annotations
from .Players.PlayerController import PlayerController
from .Board import Board
import time


class Game:

    def __init__(self, game_n:int, board_width:int, board_heigth:int, players:list(PlayerController)):
        assert(board_width % 2 != 0)
        self.game_n = game_n
        self.players = players
        self.winner = -1
        self.game_board:Board = Board(board_width, board_heigth)

    #start game and keep make players move until game is finished, return the idplayer that win
    def start_game(self) -> tuple(int,int):
        print("start game!")
        current_player = 0

        while(not self.is_over()):
            if self.game_board.play(self.players[current_player].make_move(self.game_board), self.players[current_player].player_id):
                current_player = 1 if current_player == 0 else 0
            else:
                print("Illegal move!!")
                time.sleep(5)
        #self.game_board.print_board()
        if self.winner < 0:
            print("game is a draw")
        else:
            print(f"Player {self.players[self.winner-1].__str__()} won!")
        print(f"Player {self.players[0].__str__()} evaluated the board {self.players[0].get_eval_count()} times")
        print(f"Player {self.players[1].__str__()} evaluated the board {self.players[1].get_eval_count()} times")

        return (self.players[0].get_eval_count() , self.players[1].get_eval_count())
    #function that determine if the game is over
    def is_over(self) -> bool:
        self.winner = Game.winning(self.game_board.get_board_state(), self.game_n)
        return self.winner != 0

    #determines if a player has won, if so return his player_id
    def winning(board:list(list(int)), game_n:int) -> int:

        #vertical check
        for i in range(0, len(board)):
            for j in range(0, len(board[i]) - game_n + 1):
                if(board[i][j] != 0):
                    player = board[i][j]
                    for x in range(1, game_n):
                        if board[i][j+x] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #horizontal check
        for i in range(0, len(board)-game_n+1):
            for j in range(0, len(board[i])):
                if board[i][j] != 0:
                    player = board[i][j]
                    for x in range(1,game_n):
                        if board[i+x][j] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #ascending diagonal check
        for i in range(0, len(board) - game_n + 1):
            for j in range(len(board[i]) - 1, game_n - 1, -1):
                if board[i][j] != 0:
                    player = board[i][j]
                    for x in range(1,game_n):
                        if board[i+x][j-x] != player:
                            player = 0
                            break
                    if player != 0:
                        return player

        #descending diagonal check
        for i in range(0, len(board) - game_n + 1):
            for j in range(len(board[i])- game_n + 1):
                if board[i][j] != 0:
                    player = board[i][j]
                    for x in range(1,game_n):
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
            