import unittest

from src.algorithms.algs_dfs_bfs import *
from src.state.state import State
from src.algorithms.frontier import Frontier
from src.algorithms.solution import Solution

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        # Initialize test states and goal state
        self.initial_state = State(value=convert_1d_to_int([3,5,1,0,2,7,4,8,6]), depth=0, cost=0, zero_index=3)

    def test_dfs_goal_state_found(self):
        solution = depth_first_search(self.initial_state)
        
        self.assertEqual(solution.get_cost(), 66717)  # Total states in the 8-puzzle
        self.assertEqual(solution.get_max_search_depth(), 66741)  # Starting state
        self.assertEqual(solution.get_nodes_expanded(), 99686)
