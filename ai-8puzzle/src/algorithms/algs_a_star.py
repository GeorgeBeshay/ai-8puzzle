import math
from typing import List, Dict, Tuple, Callable
from src.algorithms.solution import Solution
from src.state.state import State
from src.state.state_utilities import convert_1d_to_int, convert_int_to_1d
from queue import PriorityQueue


def get_heuristic(heuristic_type: str) -> Callable[[int, int], int]:
    """
    Get Heuristic Function for A* Search Algorithm

    This function retrieves a heuristic function based on the provided
    heuristic type for use in the A* search algorithm.

    Parameters:
    :param heuristic_type:
    - heuristic_type (str): The type of heuristic used to estimate the cost to reach the goal state.

    Returns:
    :return: Callable[[int, int], int]
    - Callable[[int, int], int]: A callable function that computes the heuristic value for a
    given element and its index.

    Algorithm Overview:
    - The function uses a `match` statement to select the appropriate heuristic function based on the heuristic type.
    - If the heuristic type is "Manhattan," a lambda function is returned to compute the Manhattan distance.
    - If the heuristic type is "Euclidean," a lambda function is returned to compute the Euclidean distance.
    - For unknown heuristic types, a default lambda function is returned, which returns 0 for all element pairs.

    Each lambda function takes two parameters: `value` (element) and its `idx` (index).
    """
    match heuristic_type.lower():
        case "manhattan":
            return lambda value, idx: (abs((value % 3) - (idx % 3)) + abs((value // 3) - (idx // 3))) \
                if value != idx else 0
        case "euclidean":
            return lambda value, idx: math.sqrt(((value % 3) - (idx % 3)) ** 2 + ((value // 3) - (idx // 3)) ** 2) \
                if value != idx else 0
        case _:
            return lambda value, idx: 0


def h_of_n(state: State, heuristic: Callable[[int, int], int]) -> int:
    """
    Calculate the Heuristic Value for A* Search Algorithm

    This function calculates the heuristic value for a given state in the A* search algorithm, using a user-defined
    heuristic function.

    Parameters:
    :param state:
    :param heuristic:
    - state (State): The state for which the heuristic value is calculated.
    - heuristic (Callable[[int, int], int]): A callable function that computes the
    heuristic value for element and index.

    Returns:
    :return: int
    - int: The calculated heuristic value representing the estimated cost
    to reach the goal state from the current state.

    Algorithm Overview:
    - Convert the state's integer representation into a 1D array ('arr_state').
    - Initialize the heuristic value accumulator 'h' to 0.
    - Iterate through the elements of 'arr_state' and calculate the heuristic value:
      - If the element is 0 (empty tile) or in its correct position (matches the index), skip it.
      - Otherwise, call the user-defined heuristic function to calculate the heuristic value for the element.
      - Add the calculated heuristic value to 'h'.
    - Return the total heuristic value 'h'.
    """
    arr_state = convert_int_to_1d(state.get_value())
    h = 0
    for i in range(9):
        if arr_state[i] == 0 or arr_state[i] == i:
            continue
        h += heuristic(arr_state[i], i)
    return h


def f_of_n(parent_state: State, child_state: State, heuristic_type: str) -> int:
    """
    Calculate the 'f' Value for the A* Search Algorithm

    This function computes the 'f' value for the A* search algorithm, which is the sum of the
    backward cost function ('g') and the heuristic forward cost value ('h').

    Parameters:
    :param parent_state:
    :param child_state:
    :param heuristic_type:

    - parent_state (State): The parent state in the search.
    - child_state (State): The child state for which the 'f' value is calculated.
    - heuristic_type (str): The type of heuristic to be used in the calculation.

    Returns:
    :return: int
    - int: The 'f' value representing the cost from the initial state to the child state.

    Algorithm Overview:
    1.  Calculate the 'g' value as the parent state's backward cost plus 1 (cost of the edge / move).
    2.  Obtain the heuristic value ('h') by calling the 'h_of_n' function with the child state and heuristic type.
    2.1 The heuristic function is retrieved from the function `get_heuristic()` so that it can be applied directly.
    3.  Compute the 'f' value as the sum of 'g' and 'h'.
    4.  Return the 'f' value, which represents the estimated total cost from the initial state to the child state.

    This function is a crucial part of the A* search algorithm, helping in prioritizing state exploration
    based on both the cost to reach the state ('g') which is the backward cost
    and the estimated cost to reach the goal from the state ('h') which is the forward cost (heuristic).
    """
    g = parent_state.get_cost() + 1
    h = h_of_n(child_state, get_heuristic(heuristic_type))
    return g + h


def a_star(initial_state: State, int_goal_state: int = 36344967696, heuristic="Manhattan") -> Solution:
    """
        A* Search Algorithm Implementation

        This function implements the A* search algorithm to find the optimal path from an initial state to a goal state.

        Parameters:
        :param initial_state:
        :param int_goal_state:
        :param heuristic:

        Returns:
        :return: int

        Algorithm Overview:
        1. Initialize data structures including the priority queue (frontier), sets to track explored and frontier states,
           and a parent_map to keep track of parent-child relationships.
        2. Start with the initial state and add it to the frontier.
        3. Begin the A* search loop (the while loop).
        4. For each iteration of the loop, select a state from the frontier with the lowest "f" value (cost + heuristic).
        5. If the selected state is the goal state, construct a solution and return it.
        6. Expand the selected state to generate its neighbors.
        7. For each neighbor, calculate the "f" value, and add it to the frontier if it's not in the explored set
           or if the new path has a lower cost.
        8. Continue the loop until a solution is found or the frontier is empty.
        9. In case of finishing the A* search loop, construct a solution indicating the algorithm failure.

        This function uses priority-based search, explores promising paths (paths with the lowest cost) first,
        and maintains parent information to reconstruct the optimal path once the goal state is reached.
        The choice of heuristic influences the search efficiency, however in our assignment we've been asked to
        utilize only the Manhattans distance and the Euclidean distance as our possible heuristics.
        """

    # Creation and Initialization of algorithm data_structures
    frontier = PriorityQueue()      # lowest priority first
    # we will need to check for the presence of a state in the frontier, so to avoid the O(n) procedure when
    # utilizing the PriorityQueue datastructure, we will maintain a set for this purpose only.
    frontier_set = set()
    explored_set = set()        # the states that have been explored.
    # datastructure maps between a state, and its (parent x, path total cost from parent x) tuple.
    parent_map: Dict[int, Tuple[int, int]] = {}
    # to keep track of the deepest point reached in the search tree using this searching algorithm
    max_search_depth = 0
    explored_states_count = 0   # counting all the explored states.

    frontier.put((0, initial_state))        # insert the initial state with a 0 cost in the frontier.
    frontier_set.add(initial_state.get_value())
    parent_map[initial_state.get_value()] = (initial_state.get_value(), 0)

    while not frontier.empty():
        current_state: State = frontier.get()[1]
        if current_state.get_value() in explored_set:
            continue
            # this may occur when a state may have multiple possible paths, however the least cost path
            # will be the first to pop from the frontier, and so to avoid re-exploring the same state when being
            # popped from the frontier with the non least cost path, we check the explored_set for this condition.

        explored_set.add(current_state.get_value())
        explored_states_count += 1
        max_search_depth = max(max_search_depth, current_state.get_depth())     # keep track of the max reached depth.

        if current_state.is_goal(int_goal_state):
            # To match with the default implementation of the solution class,
            # that takes a parent map as a dict[int, int], so we convert it to a new dict, dropping the cost term.
            new_parent_map: Dict[int, int] = {key: value[0] for key, value in parent_map.items()}
            return Solution(True, new_parent_map, explored_states_count,
                            max_search_depth, current_state.get_cost(), int_goal_state)

        for neighbor in current_state.expand():
            # first case, that the neighbor was the first time being "seen"
            if neighbor.get_value() not in frontier_set and neighbor.get_value() not in explored_set:
                temp_f_of_n = f_of_n(current_state, neighbor, heuristic)
                frontier.put((temp_f_of_n, neighbor))
                frontier_set.add(neighbor.get_value())
                parent_map[neighbor.get_value()] = (current_state.get_value(), temp_f_of_n)
            # second case, the neighbor has been seen before, however this time from another path that may be better.
            elif neighbor.get_value() in frontier_set:
                temp_f_of_n = f_of_n(current_state, neighbor, heuristic)
                if temp_f_of_n < parent_map[neighbor.get_value()][1]:
                    frontier.put((temp_f_of_n, neighbor))
                    frontier_set.add(neighbor.get_value())
                    parent_map[neighbor.get_value()] = (current_state.get_value(), temp_f_of_n)
    return Solution(False)


# TODO remove this
init_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
s = State(convert_1d_to_int(init_state), 0, 0, 5)
# init_state = [1, 0, 2, 3, 4, 5, 6, 7, 8]
# s = State(convert_1d_to_int(init_state), 0, 0, 1)
solution = a_star(s)

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