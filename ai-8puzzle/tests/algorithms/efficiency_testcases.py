import unittest

from src.algorithms.algs_dfs_bfs import *
from src.algorithms.algs_a_star import *
from src.state.state import State
from src.algorithms.frontier import Frontier
from src.algorithms.solution import Solution


class SearchAlgorithmsEfficiencyTests(unittest.TestCase):
    def test_efficiency_01(self):
        initial_state = State(value=convert_1d_to_int([6, 4, 3, 2, 8, 5, 7, 1, 0]), depth=0, cost=0, zero_index=8)

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

        self.assertTrue(a_star_solution.get_running_time() <= bfs_solution.get_running_time())

    def test_efficiency_02(self):
        # DFS and BFS can't solve this problem. 381406752
        initial_state = State(value=convert_1d_to_int([6, 4, 0, 3, 2, 1, 5, 8, 7]), depth=0, cost=0, zero_index=2)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)
        a_star_solution = a_star(initial_state)

        self.assertTrue(dfs_solution.is_success())
        self.assertTrue(bfs_solution.is_success())
        self.assertTrue(a_star_solution.is_success())

        self.assertTrue(a_star_solution.get_cost() <= bfs_solution.get_cost())
        self.assertTrue(bfs_solution.get_cost() <= dfs_solution.get_cost())

        self.assertTrue(a_star_solution.get_nodes_expanded() <= bfs_solution.get_nodes_expanded())

        self.assertTrue(a_star_solution.get_running_time() <= bfs_solution.get_running_time())

    def test_efficiency_03(self):
        initial_state = State(value=convert_1d_to_int([4, 8, 7, 3, 2, 1, 0, 6, 5]), depth=0, cost=0, zero_index=6)

        dfs_solution = depth_first_search(initial_state)
        bfs_solution = breadth_first_search(initial_state)
        a_star_solution = a_star(initial_state)

        self.assertTrue(dfs_solution.is_success())
        self.assertTrue(bfs_solution.is_success())
        self.assertTrue(a_star_solution.is_success())

        self.assertTrue(a_star_solution.get_cost() <= bfs_solution.get_cost())
        self.assertTrue(bfs_solution.get_cost() <= dfs_solution.get_cost())

        self.assertTrue(a_star_solution.get_nodes_expanded() <= bfs_solution.get_nodes_expanded())

        self.assertTrue(a_star_solution.get_running_time() <= bfs_solution.get_running_time())
