from __future__ import annotations
from .Heuristic.SimpleHeuristic import SimpleHeuristic
from .Players.PlayerController import PlayerController
from .Players.HumanPlayer import HumanPlayer
from .Players.MinMaxPlayer import MinMaxPlayer
from .Players.AlphaBetaPlayer import AlphaBetaPlayer
from .Heuristic.AdvancedHeuristic import AdvancedHeuristic, Heuristic
from .Game import Game

class App:

    def __init__(self):
        self.game_n = 4
        self.board_width = 7
        self.board_height = 6
        self.players = self.__get_players(self.game_n)
        self.game= Game(self.game_n, self.board_width, self.board_height, self.players)
        self.game.start_game()
        

    def __get_players(self, game_n:int) -> list(PlayerController):
        """Determine the players for the game

        Args:
            game_n (int):

        Returns:
            list(PlayerController): a list of size 2 with two PlayerControllers
        """
        heuristic1 = AdvancedHeuristic(game_n)
        heuristic2 = SimpleHeuristic(game_n)

        human = AlphaBetaPlayer(1, game_n, 6, heuristic1)
        human2 = HumanPlayer(2, game_n, heuristic2)

        players = [human, human2]
        return players

    
