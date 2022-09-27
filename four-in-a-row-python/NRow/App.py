from __future__ import annotations
from .Heuristic.SimpleHeuristic import SimpleHeuristic
from .Players.PlayerController import PlayerController
from .Players.HumanPlayer import HumanPlayer
from .Players.MinMaxPlayer import minMaxPlayer
from .Game import Game

class App:

    def __init__(self):
        self.gameN = 4
        self.boardWidth = 7
        self.boardHeight = 6
        self.players = self.__getPlayers(self.gameN)
        self.game= Game(self.gameN, self.boardWidth, self.boardHeight, self.players)
        self.game.startGame()
        

    def __getPlayers(self, gameN:int) -> list(PlayerController):
        heuristic1 = SimpleHeuristic(gameN)
        heuristic2 = SimpleHeuristic(gameN)

        human = HumanPlayer(1, gameN, heuristic1)
        human2 = minMaxPlayer(2, gameN, 3, heuristic2)

        players = [human, human2]
        return players

    