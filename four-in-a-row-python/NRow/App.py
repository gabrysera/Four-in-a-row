from __future__ import annotations

from .Players.HumanPlayer import HumanPlayer
from .Heuristic.SimpleHeuristic import SimpleHeuristic
from .Players.PlayerController import PlayerController
from .Players.AlphaBetaPlayer import AlphaBetaPlayer
from .Players.MinMaxPlayer import MinMaxPlayer
from .Players.AlphaBetaPlayer import AlphaBetaPlayer
from .Heuristic.AdvancedHeuristic import AdvancedHeuristic, Heuristic
from .Game import Game
from .Test import Test
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
            list(PlayerController): a list of size 2 with One Normal player and one Alpha Beta player
        """
        heuristic1 = SimpleHeuristic(game_n,)
        heuristic2 = AdvancedHeuristic(game_n, self.board_width, self.board_height)

        alpha_beta_1 = AlphaBetaPlayer(1, game_n, 7, heuristic1)
        alpha_beta_2 = AlphaBetaPlayer(2, game_n,6,heuristic2)

        players = [alpha_beta_1, alpha_beta_2]
        return players

    


    def play_normal_game(self):
        self.game_n = 4
        self.board_width = 7
        self.board_height = 6
        self.players = self.get_players(self.game_n)
        self.game= Game(self.game_n, self.board_width, self.board_height, self.players)
        self.game.start_game()

    def test(self):
        """
        In the following function we test:
            1) difference in computational cost between min max and alpha beta pruning, this is done by:
                - testing how many times they evaluate the board for different board width by running many games with different depths for both with and without alpha beta pruning players
                - testing how many times they evaluate the board for different depth by running many games with different depths and widths
            2) How good is the new heuristic compared to the simple one, this is done by:
                - let 2 alpha beta players play against each other, one with depth x using the simple heuristic, the other one with 
                depth (x-1) using the advanced heuristic. if the advanced heuristic win we go on testing for depth (x-2) and so on. 
                The difference in depth is therefore used as an indicator for better an heuristic is compared to the other
        """
        test = Test()
        test.test_alpha_beta_vs_min_max_with_different_width()
        test.test_new_heuristic()
