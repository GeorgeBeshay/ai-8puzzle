from algs_a_star import AStar
from algs_dfs_bfs import DepthFirstSearch, BreadthFirstSearch
from algs import SearchAlgorithm


class AlgorithmFactory:
    @staticmethod
    def get_algorithm(algorithm_type: str, heuristic="Manhattan") -> SearchAlgorithm:
        if algorithm_type.upper() == "DFS":
            return DepthFirstSearch()
        elif algorithm_type.upper() == "BFS":
            return BreadthFirstSearch()
        elif algorithm_type.upper() == "A*":
            return AStar(heuristic)
        else:
            raise ValueError("Invalid algorithm type.")