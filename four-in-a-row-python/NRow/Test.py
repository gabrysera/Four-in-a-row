from __future__ import annotations
from .Game import Game
from .Players.AlphaBetaPlayer import AlphaBetaPlayer
from .Players.MinMaxPlayer import MinMaxPlayer
from .Heuristic.AdvancedHeuristic import AdvancedHeuristic
from .Players.PlayerController import PlayerController
import matplotlib.pyplot as plt
import numpy as np


def get_test_players(game_n:int, depth:int, board_width:int, board_height:int) -> list(PlayerController):
    """Determine the players for the game used in the tes
    Args:
        game_n (int):
    Returns:
        list(PlayerController): a list of size 2 with two AlphaBetaPlayers
    """
    heuristic1 = AdvancedHeuristic(game_n, board_width, board_height)
    heuristic2 = AdvancedHeuristic(game_n, board_width, board_height)
    alpha_beta_1 = AlphaBetaPlayer(1, game_n, depth, heuristic1)
    alpha_beta_2 = MinMaxPlayer(2, game_n, depth, heuristic2)
    players = [alpha_beta_1, alpha_beta_2]
    return players

def compute_area_difference(x:list[int], y:list[int])->int:
    """
    from 2 arrays of integers, return the difference between the
    areas of the curves that these 2 arrays would generate if plotted
    """
    return np.trapz(y, dx=2) - np.trapz(x, dx=2)

class Test:

    def __init__(self):
        self.name = "test"

    def test_alpha_beta_vs_min_max_with_different_width(self):
        """
        this tests the difference in number of evaluations computed by alpha beta player compared to min max player. It does so by 
        testing the game at different depths and different widths, since these 2 parameters are the ones that count the most in the overall
        complexity. It then print pictures representing the results and put them in the folder four-in-a-row-python/NRow/Results/
        """
        area_differences = []
        for depth in range(2,8,1):
            total_board_evaluations_same_depth = []
            
            for width in range(5,13,2):
                game_n = 4
                board_width = width
                board_height = 6
                players = get_test_players(game_n,depth,board_width, board_height)
                game= Game(game_n, board_width, board_height, players)
                total_board_evaluations_same_depth.append(game.start_game())
            
            area_differences.append(self.test_plot(total_board_evaluations_same_depth, depth))
        plt.plot(range(2,8,1), area_differences)
        plt.xlabel("depth")
        plt.ylabel("evaluations")
        plt.title('number of evaluations given the depth')
        plt.savefig(f'four-in-a-row-python/NRow/Results/evaluations_given_depth')

    def test_plot(self, players_number_of_evaluations:list[tuple[int,int]], depth:int):
        
        players_lists = list(map(list, zip(*players_number_of_evaluations)))
        aplha_beta_player = np.asarray(players_lists[0])
        min_max_player = np.asarray(players_lists[1])
        area_difference = int(compute_area_difference(aplha_beta_player, min_max_player))

        plt.plot(range(5,13,2),aplha_beta_player, label='alpha beta player')
        plt.plot(range(5,13,2), min_max_player, label='normal min max player')
        plt.yscale('log')
        plt.ylabel("number of evaluations")
        plt.xlabel("width")
        plt.title(f'depth: {depth}')
        plt.fill_between(range(5,13,2),aplha_beta_player, min_max_player, color = "red",alpha = 0.3, label = f'area difference: {area_difference}')
        plt.legend()
        plt.savefig(f'four-in-a-row-python/NRow/Results/depth: {depth}')
        plt.close()
        return area_difference


    def test_new_heuristic():
        pass

    