from __future__ import annotations
import sys
from . import Heuristic
from ..Board import Board
from ..Game import Game
from .Heuristic import Heuristic

class AdvancedHeuristic(Heuristic):

    def __init__(self, game_N):