from src.algorithms.algs_dfs_bfs import *
from src.algorithms.algs_a_star import *
from typing import List, Callable


def algorithm_factory(algorithm_type: str, heuristic="Manhattan") -> Callable[[int, int], List[int]]:
    algorithm_type = algorithm_type.upper()
    if algorithm_type == "DFS":
        return depth_first_search
    elif algorithm_type == "BFS":
        return breadth_first_search
    elif algorithm_type == "A*":
        return a_star
    else:
        raise ValueError("Invalid algorithm type")
