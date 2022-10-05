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
        print("Type 1 for playing against the computer.\nType 2 for running tests on performance difference between min max without alpha beta pruning and min max wityh alpha beta pruning")
        choice = int(input())
        if choice == 1:
            self.play_normal_game()
        else:
            self.test()
        

    def get_players(self, game_n:int) -> list(PlayerController):
        """Determine the players for the game

        Args:
            game_n (int):

        Returns:
            list(PlayerController): a list of size 2 with two PlayerControllers
        """
        heuristic1 = AdvancedHeuristic(game_n, self.board_width, self.board_height)
        heuristic2 = AdvancedHeuristic(game_n, self.board_width, self.board_height)

        human = AlphaBetaPlayer(1, game_n, self.depth, heuristic1)
        human2 = HumanPlayer(2, game_n,heuristic2)

        players = [human, human2]
        return players

    def get_min_max_players(self, game_n:int) -> list(PlayerController):
            """Determine the players for the game

            Args:
                game_n (int):

            Returns:
                list(PlayerController): a list of size 2 with two PlayerControllers
            """
            heuristic1 = AdvancedHeuristic(game_n, self.board_width, self.board_height)
            heuristic2 = AdvancedHeuristic(game_n, self.board_width, self.board_height)

            human = AlphaBetaPlayer(1, game_n, self.depth, heuristic1)
            human2 = HumanPlayer(2, game_n,heuristic2)

            players = [human, human2]
            return players

    def get_alpha_beta_players(self, game_n:int) -> list(PlayerController):
        """Determine the players for the game

        Args:
            game_n (int):

        Returns:
            list(PlayerController): a list of size 2 with two PlayerControllers
        """
        heuristic1 = AdvancedHeuristic(game_n, self.board_width, self.board_height)
        heuristic2 = AdvancedHeuristic(game_n, self.board_width, self.board_height)

        human = AlphaBetaPlayer(1, game_n, self.depth, heuristic1)
        human2 = HumanPlayer(2, game_n,heuristic2)

        players = [human, human2]
        return players


    def play_normal_game(self):
        self.game_n = 4
        self.board_width = 7
        self.board_height = 6
        self.players = self.get_players(self.game_n)
        self.game= Game(self.game_n, self.board_width, self.board_height, self.players)
        self.game.start_game()

    def test(self):
        #we change a parameter while keeping the other parameters constant for each test to see how this impact performance of the 2 algorithms 
        total_board_evaluations_min_max = []
        for width in range(5,13,2):
            self.game_n = 4
            self.depth = 6
            self.board_width = width
            self.board_height = 6
            self.players = self.get_min_max_players(self.game_n)
            self.game= Game(self.game_n, self.board_width, self.board_height, self.players)

            total_board_evaluations_min_max.append(self.game.start_game())
        print("min max players evaluated the board: ", total_board_evaluations_min_max)
