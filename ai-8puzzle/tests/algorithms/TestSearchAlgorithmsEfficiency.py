import unittest

from src.algorithms.algs_dfs_bfs import *
from src.algorithms.algs_a_star import *
from src.state.state import State
from src.algorithms.frontier import Frontier
from src.algorithms.solution import Solution


class TestSearchAlgorithmsEfficiency(unittest.TestCase):
    def test_a_star_efficiency(self):
        initial_state = State(value=convert_1d_to_int([3, 5, 1, 0, 2, 7, 4, 8, 6]), depth=0, cost=0, zero_index=3)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)
        a_star_solution = a_star(initial_state)

        self.assertTrue(dfs_solution.is_success())
        self.assertTrue(bfs_solution.is_success())
        self.assertTrue(a_star_solution.is_success())

        self.assertTrue(a_star_solution.get_cost() <= bfs_solution.get_cost())
        self.assertTrue(a_star_solution.get_cost() <= dfs_solution.get_cost())

        self.assertTrue(a_star_solution.get_nodes_expanded() <= bfs_solution.get_nodes_expanded())
        self.assertTrue(a_star_solution.get_nodes_expanded() <= dfs_solution.get_nodes_expanded())

        # self.assertTrue(a_star_solution.get_running_time() <= bfs_solution.get_running_time())
        # self.assertTrue(a_star_solution.get_running_time() <= dfs_solution.get_running_time())

    def test_bfs_efficiency(self):
        initial_state = State(value=convert_1d_to_int([3, 5, 1, 0, 2, 7, 4, 8, 6]), depth=0, cost=0, zero_index=3)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)

        self.assertTrue(dfs_solution.is_success())
        self.assertTrue(bfs_solution.is_success())

        self.assertTrue(bfs_solution.get_cost() <= dfs_solution.get_cost())

        self.assertTrue(bfs_solution.get_max_search_depth() <= dfs_solution.get_max_search_depth())
