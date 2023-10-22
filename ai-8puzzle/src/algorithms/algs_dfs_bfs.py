from typing import List

from src.algorithms.frontier import Frontier
from src.state.state import State
from src.state.state_utilities import convert_1d_to_int, convert_int_to_1d


def depth_first_search(start: State, goal: State) -> dict:
    # Implementation of DFS
    no_of_explored = 0  # initially nothing is explored
    frontier = Frontier("stack")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}

    frontier.push(start)
    explored_and_frontier.add(start.value)
    parent_map[start.value] = start.value

    while frontier.size() > 0:
        curr: State = frontier.pop()
        print("curr = ", convert_int_to_1d(curr.value))
        explored.add(curr.value)
        no_of_explored += 1

        if curr.value == g.value:
        # if curr.is_goal():
            # we found the goal state
            print("DFS is Working ..")
            return parent_map
        neighbors = curr.expand() # .reverse() gives error
        # print("===================")
        # for i in neighbors:
        #     print("State: ", convert_int_to_1d(i.value))
        # print("===================")
        for neighbor in neighbors:
            if neighbor.value not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor.value)
                parent_map[neighbor.value] = curr.value
    return False
    # print("DFS Working ..")
    # return [123456789]


def breadth_first_search(start: int, goal: int) -> bool:
    # Implementation of BFS
    no_of_explored = 0  # initially nothing is explored
    frontier = Frontier("queue")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}

    frontier.push(start)
    explored_and_frontier.add(start.value)
    parent_map[start.value] = start.value

    while frontier.size() > 0:
        curr = frontier.pop()
        explored.add(curr)
        no_of_explored += 1

        if curr.value == goal.value:
            # we found the goal state
            print("BFS is Working ..")
            return parent_map
        for neighbor in curr.expand():
            if neighbor not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor.value)
                parent_map[neighbor.value] = curr.value
    return False
    # print("BFS Working ..")
    # return [123456789]

array = [1,2,5,3,4,0,6,7,8]
# print(array)
a = convert_1d_to_int(array)
s = State(a, 1, 1, 5)

goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(goal)
b = convert_1d_to_int(goal)
g = State(b, 1, 1, 0)
depth_first_search(s, g)
print("finished")