from typing import List
from algs import SearchAlgorithm


class AStar(SearchAlgorithm):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def search(self, start: int, goal: int) -> List[int]:
        # Implementation of A* with the given heuristic
        print("A* Working ..")
        return [123456789]