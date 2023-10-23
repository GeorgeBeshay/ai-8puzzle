from typing import List, Tuple

from src.algorithms.frontier import Frontier
from src.state.state import State
from src.state.state_utilities import convert_1d_to_int, convert_int_to_1d
from src.algorithms.solution import Solution


def init_datastructures(frontier: Frontier, explored_and_frontier: set, parent_map: dict, initial_state: State):
    """
    Initiates the data structures used by the bfs and dfs

    Args:
        frontier: Frontier that represents the stack or the queue which stores the states to be expanded
        explored_and_frontier: set contains elements either in the explored or the frontier
        parent_map: dictionary that has the node and its parent
        initial_state: The start state that is given

    :returns: None
    """
    frontier.push(initial_state)
    explored_and_frontier.add(initial_state.value)
    parent_map[initial_state.value] = initial_state.value


def depth_first_search(initial_state: State, int_goal_state: int = 36344967696) -> Solution:
    """
    Performs a depth first search to find a goal state in a search space starting from an initial_state

    Args:
        initial_state: State that represents initial state from which the search begins.
        integer_goal_state: int representation of the goal state (default is 36344967696).

    :returns:
        Tuple[bool, dict]: A tuple containing a boolean value indicating whether a goal state was found or not,
        and a dictionary that maps states to their parent states in the search tree (or an empty dictionary if initial state is not solvable).
    """
    no_of_explored = 0                                  # initially nothing is explored
    frontier = Frontier("stack")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}
    max_search_depth = 0

    init_datastructures(frontier, explored_and_frontier, parent_map, initial_state)

    while frontier.size() > 0:
        current_state: State = frontier.pop()
        explored.add(current_state.value)
        no_of_explored += 1
        max_search_depth = max(max_search_depth, current_state.get_depth())

        if current_state.is_goal(int_goal_state):       # note that 36344967696 is the default integer goal state.
            return Solution(True, parent_map, no_of_explored, max_search_depth,
                            current_state.get_cost(), int_goal_state)

        neighbors = current_state.expand()
        neighbors.reverse()
        for neighbor in neighbors:
            if neighbor.value not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor.value)
                parent_map[neighbor.value] = current_state.value
    return Solution(False)


def breadth_first_search(initial_state: State, int_goal_state: int = 36344967696) -> Solution:
    """
    Performs a breadth first search to find a goal state in a search space starting from an initial_state

    Args:
        initial_state: State that represents initial state from which the search begins.
        integer_goal_state: int representation of the goal state (default is 36344967696).

    :returns:
        Tuple[bool, dict]: A tuple containing a boolean value indicating whether a goal state was found or not,
        and a dictionary that maps states to their parent states in the search tree (or an empty dictionary if initial state is not solvable).
    """
    no_of_explored = 0  # initially nothing is explored
    frontier = Frontier("queue")
    explored = set()
    explored_and_frontier = set()
    parent_map = {}
    max_search_depth = 0

    init_datastructures(frontier, explored_and_frontier, parent_map, initial_state)

    while frontier.size() > 0:
        current_state: State = frontier.pop()
        explored.add(current_state.value)
        no_of_explored += 1
        max_search_depth = max(max_search_depth, current_state.get_depth())

        if current_state.is_goal(int_goal_state):
            return Solution(True, parent_map, no_of_explored, max_search_depth,
                            current_state.get_cost(), int_goal_state)

        neighbors = current_state.expand()
        for neighbor in neighbors:
            if neighbor.value not in explored_and_frontier:
                frontier.push(neighbor)
                explored_and_frontier.add(neighbor.value)
                parent_map[neighbor.value] = current_state.value
    return Solution(False)


# TODO remove this
init_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
s = State(convert_1d_to_int(init_state), 0, 0, 5)
solutions = [depth_first_search(s), breadth_first_search(s)]

for solution in solutions:
    if solution.is_success():
        plan_step = solution.get_next_step()
        while plan_step is not None:
            print(f'{plan_step[0]}\n{plan_step[1]}\n{plan_step[2]}\n\n')
            plan_step = solution.get_next_step()
        print(f"Total Cost: {solution.get_cost()}")
        print(f"Total Expanded Nodes: {solution.get_nodes_expanded()}")
        print(f"Max Search Depth: {solution.get_max_search_depth()}")
        print(f"First Step: {solution.get_first_step()}")
        print(f"Last Step: {solution.get_last_step()}")
    else:
        print("Couldn't solve")
    print(" --------------------------------------- END --------------------------------------- ")
