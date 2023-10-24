from src.algorithms.algs_dfs_bfs import *
from src.algorithms.algs_a_star import *
from typing import List, Callable


def algorithm_factory(algorithm_type: str) -> Callable[[State, int], Solution]:
    algorithm_type = algorithm_type.upper()
    if algorithm_type == "DFS":
        return depth_first_search
    elif algorithm_type == "BFS":
        return breadth_first_search
    elif algorithm_type == "A*":
        heuristic = "Manhattan" if input("Enter heuristic function (M / E): ").strip().upper() == "M" else "Euclidean"
        return lambda int_state: a_star(int_state, heuristic=heuristic)
    else:
        raise ValueError("Invalid algorithm type")
