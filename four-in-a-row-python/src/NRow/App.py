from NRow.Heuristic import SimpleHeuristic
from NRow.Players import PlayerController
from NRow.Players import HumanPlayer
import Game

class App:

    def __init__(self):
        self.gameN = 4
        self.boardWidth = 7
        self.boardHeight = 6
        self.players = self.__getPlayers(self.gameN)
        self.game= Game(self.gameN, self.boardWidth, self.boardHeight, self.players)
        self.game.startGame()
        

    def __getPlayers(gameN:int) -> list(PlayerController):
        heuristic1 = SimpleHeuristic(gameN)
        heuristic2 = SimpleHeuristic(gameN)

        human = HumanPlayer(1, gameN, heuristic1)
        human2 = HumanPlayer(2, gameN, heuristic2)

        players = [human, human2]
        return players

    