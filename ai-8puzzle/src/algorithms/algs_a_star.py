from algs import *


class AStar(SearchAlgorithm):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def search(self, start: int, goal: int) -> List[int]:
        # Implementation of A* with the given heuristic
        print("A* Working ..")
        return [0]