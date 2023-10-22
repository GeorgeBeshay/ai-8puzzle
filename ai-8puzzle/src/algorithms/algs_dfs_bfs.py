# from typing import List

from src.algorithms.frontier import Frontier


def depth_first_search(start: int, goal: int) -> dict:
    # Implementation of DFS
    no_of_explored = 0  # initially nothing is explored
    frontier = Frontier("stack")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}

    frontier.push(start)
    explored_and_frontier.add(start)
    parent_map[start] = start

    while frontier.size() > 0:
        curr = frontier.pop()
        explored.add(curr)
        no_of_explored += 1

        if curr == goal:
            # we found the goal state
            print("DFS is Working ..")
            return parent_map
        neighbors = curr.expand().reverse()
        for neighbor in neighbors:
            if neighbor not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor)
                parent_map[neighbor] = curr
    return False
    # print("DFS Working ..")
    # return [123456789]


def breadth_first_search(start: int, goal: int) -> bool:
    # Implementation of BFS

    frontier = Frontier("queue")
    explored = set()
    explored_and_frontier = set()
    no_of_explored = 0  # initially nothing is explored
    parent_map = {}

    frontier.push(start)
    explored_and_frontier.add(start)
    parent_map[start] = start

    while frontier.size() > 0:
        curr = frontier.pop()
        explored.add(curr)
        no_of_explored += 1

        if curr == goal:
            # we found the goal state
            print("BFS is Working ..")
            return parent_map
        for neighbor in curr.expand():
            if neighbor not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor)
                parent_map[neighbor] = curr
    return False
    # print("BFS Working ..")
    # return [123456789]
