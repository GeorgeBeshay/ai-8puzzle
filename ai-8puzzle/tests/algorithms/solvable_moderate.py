import unittest

from src.algorithms.algs_dfs_bfs import *
from src.state.state import State
from src.algorithms.frontier import Frontier
from src.algorithms.solution import Solution


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        # Initialize test state
        self.initial_state = State(value=convert_1d_to_int([3, 5, 1, 0, 2, 7, 4, 8, 6]), depth=0, cost=0, zero_index=3)

    def test_dfs_finds_solution_if_exists(self):
        solution = depth_first_search(self.initial_state)
        self.assertEqual(solution.get_first_step(), [[3, 5, 1], [0, 2, 7], [4, 8, 6]])
        self.assertEqual(solution.get_last_step(), [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(solution.is_success(), True)

    def test_dfs_results(self):
        solution = depth_first_search(self.initial_state)
        self.assertEqual(solution.get_cost(), 66717)  # Total states in the 8-puzzle
        self.assertEqual(solution.get_max_search_depth(), 66741)  # maximum search depth
        self.assertEqual(solution.get_nodes_expanded(), 99686)  # number of nodes expanded

    def test_bfs_finds_solution_if_exists(self):
        solution = breadth_first_search(self.initial_state)
        self.assertEqual(solution.get_first_step(), [[3, 5, 1], [0, 2, 7], [4, 8, 6]])
        self.assertEqual(solution.get_last_step(), [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        # print(solution.get_max_search_depth(), solution.cost, solution.get_nodes_expanded())
        self.assertEqual(solution.is_success(), True)

    def test_bfs_results(self):
        solution = breadth_first_search(self.initial_state)
        self.assertEqual(solution.get_cost(), 17)  # Total states in the 8-puzzle
        self.assertEqual(solution.get_max_search_depth(), 17)  # maximum search depth
        self.assertEqual(solution.get_nodes_expanded(), 18813)  # number of nodes expanded


