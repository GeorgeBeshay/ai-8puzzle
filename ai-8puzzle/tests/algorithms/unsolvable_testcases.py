import unittest

from src.algorithms.algs_dfs_bfs import *
from src.algorithms.algs_a_star import *
from src.state.state import State
from src.algorithms.frontier import Frontier
from src.algorithms.solution import Solution


class UnsolvableTestCases(unittest.TestCase):
    def test_unsolvable_01(self):
        initial_state = State(value=convert_1d_to_int([8, 1, 7, 3, 0, 5, 2, 4, 6]), depth=0, cost=0, zero_index=4)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)
        a_star_solution = a_star(initial_state)

        self.assertFalse(dfs_solution.is_success())
        self.assertFalse(bfs_solution.is_success())
        self.assertFalse(a_star_solution.is_success())

    def test_unsolvable_02(self):
        initial_state = State(value=convert_1d_to_int([8, 3, 7, 5, 1, 6, 2, 4, 0]), depth=0, cost=0, zero_index=8)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)
        a_star_solution = a_star(initial_state)

        self.assertFalse(dfs_solution.is_success())
        self.assertFalse(bfs_solution.is_success())
        self.assertFalse(a_star_solution.is_success())

    def test_unsolvable_03(self):
        initial_state = State(value=convert_1d_to_int([8, 3, 7, 6, 4, 2, 1, 0, 5]), depth=0, cost=0, zero_index=7)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)
        a_star_solution = a_star(initial_state)

        self.assertFalse(dfs_solution.is_success())
        self.assertFalse(bfs_solution.is_success())
        self.assertFalse(a_star_solution.is_success())
