import unittest

from src.algorithms.algs_dfs_bfs import *
from src.state.state import State
from src.algorithms.frontier import Frontier
from src.algorithms.solution import Solution


class TestSearchAlgorithms2(unittest.TestCase):
    def setUp(self):
        # Initialize test state
        self.initial_state = State(value=convert_1d_to_int([1, 2, 5, 3, 4, 0, 6, 7, 8]), depth=0, cost=0, zero_index=5)

    def test_dfs_finds_solution_if_exists(self):
        solution = depth_first_search(self.initial_state)
        self.assertEqual(solution.get_first_step(), [[1, 2, 5], [3, 4, 0], [6, 7, 8]])
        self.assertEqual(solution.get_last_step(), [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        # print(solution.get_cost(),solution.get_max_search_depth(), solution.get_nodes_expanded())
        self.assertEqual(solution.is_success(), True)

    def test_dfs_results(self):
        solution = depth_first_search(self.initial_state)
        self.assertEqual(solution.get_cost(), 3)  # Total states in the 8-puzzle
        self.assertEqual(solution.get_max_search_depth(), 3)  # maximum search depth
        self.assertEqual(solution.get_nodes_expanded(), 4)  # number of nodes expanded

    def test_bfs_finds_solution_if_exists(self):
        solution = breadth_first_search(self.initial_state)
        self.assertEqual(solution.get_first_step(), [[1, 2, 5], [3, 4, 0], [6, 7, 8]])
        self.assertEqual(solution.get_last_step(), [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        print(solution.get_cost(),solution.get_max_search_depth(), solution.get_nodes_expanded())
        self.assertEqual(solution.is_success(), True)

    def test_bfs_results(self):
        solution = breadth_first_search(self.initial_state)
        self.assertEqual(solution.get_cost(), 3)  # Total states in the 8-puzzle
        self.assertEqual(solution.get_max_search_depth(), 3)  # maximum search depth
        self.assertEqual(solution.get_nodes_expanded(), 10)  # number of nodes expanded
