from typing import List
from src.algorithms.solution import Solution
from src.state.state import State
from src.state.state_utilities import convert_1d_to_int, convert_int_to_1d
from queue import PriorityQueue


def h_of_n(state: State, heuristic_type: str) -> int:
    return 0        # TODO change this


def f_of_n(parent_state: State, child_state: State, heuristic_type: str) -> int:
    g = parent_state.get_cost() + 1
    h = h_of_n(child_state, heuristic_type)
    return g + h


def a_star(initial_state: State, int_goal_state: int = 36344967696,
           heuristic="Manhattan") -> Solution:
    frontier = PriorityQueue()
    frontier_set = set()
    explored_set = set()
    parent_map = {}
    max_search_depth = 0
    explored_states_count = 0

    frontier.put((0, initial_state))
    frontier_set.add(initial_state.get_value())
    parent_map[initial_state.get_value()] = initial_state.get_value()

    while not frontier.empty():
        current_state: State = frontier.get()[1]
        if current_state.get_value() in explored_set:
            continue

        explored_set.add(current_state.get_value())
        explored_states_count += 1
        max_search_depth = max(max_search_depth, current_state.get_depth())

        if current_state.is_goal(int_goal_state):
            return Solution(True, parent_map, explored_states_count,
                            max_search_depth, current_state.get_cost(), int_goal_state)

        for neighbor in current_state.expand():
            if ((neighbor not in frontier_set and neighbor not in explored_set)
                    or (neighbor in frontier_set)):
                frontier.put((f_of_n(current_state, neighbor, heuristic), neighbor))
                frontier_set.add(neighbor)
                parent_map[neighbor.get_value()] = current_state.get_value()

    return Solution(False)


# TODO remove this
init_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
s = State(convert_1d_to_int(init_state), 0, 0, 5)
solutions = [a_star(s)]

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