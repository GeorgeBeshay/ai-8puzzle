from typing import List, Tuple

from src.algorithms.frontier import Frontier
from src.state.state import State
from src.state.state_utilities import convert_1d_to_int, convert_int_to_1d


def init_datastructures(frontier: Frontier, explored_and_frontier: set, parent_map: dict, initial_state: State):
    """
    Explain here
    :param frontier:
    :param explored_and_frontier:
    :param parent_map:
    :param initial_state:
    :return:
    """
    frontier.push(initial_state)
    explored_and_frontier.add(initial_state.value)
    parent_map[initial_state.value] = initial_state.value


def depth_first_search(initial_state: State, integer_goal_state: int = 36344967696) -> Tuple[bool, dict]:
    """
    Explain here
    :param initial_state:
    :param integer_goal_state:
    :return:
    """
    no_of_explored = 0                                  # initially nothing is explored
    frontier = Frontier("stack")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}

    init_datastructures(frontier, explored_and_frontier, parent_map, initial_state)

    while frontier.size() > 0:
        current_state: State = frontier.pop()
        explored.add(current_state.value)
        no_of_explored += 1

        if current_state.is_goal(integer_goal_state):       # note that 36344967696 is the default integer goal state.
            return True, parent_map

        neighbors = current_state.expand()              # .reverse() gives error
        for neighbor in neighbors:
            if neighbor.value not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor.value)
                parent_map[neighbor.value] = current_state.value
    return False, {}


def breadth_first_search(initial_state: State, int_goal_state: int = 36344967696) -> Tuple[bool, dict]:
    """
    Explain here
    :param initial_state:
    :param int_goal_state:
    :return:
    """
    no_of_explored = 0  # initially nothing is explored
    frontier = Frontier("queue")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}

    init_datastructures(frontier, explored_and_frontier, parent_map, initial_state)

    while frontier.size() > 0:
        current_state: State = frontier.pop()
        explored.add(current_state)
        no_of_explored += 1

        if current_state.is_goal(int_goal_state):
            return True, parent_map

        for neighbor in current_state.expand():
            if neighbor not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor.value)
                parent_map[neighbor.value] = current_state.value
    return False, {}


# TODO remove this
init_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
s = State(convert_1d_to_int(init_state), 0, 0, 5)
flag, par_map = depth_first_search(s)

if flag:
    temp_int_state = par_map.get(convert_1d_to_int([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    while par_map.get(temp_int_state) != temp_int_state:
        print(convert_int_to_1d(temp_int_state))
        temp_int_state = par_map.get(temp_int_state)
    else:
        print(convert_int_to_1d(temp_int_state))
else:
    print("Couldn't solve")
