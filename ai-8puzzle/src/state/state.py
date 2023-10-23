from typing import List
from src.state.state_utilities import *


class State:
    def __init__(self, value: int, depth: int, cost: int, zero_index: int):
        self.value = value
        self.depth = depth
        self.cost = cost
        self.zero_index = zero_index

    # TODO: What the value of cost of each successor
    def expand(self) -> List['State']:
        """
        Function expands the current state, to obtain the new possible reachable states from this one.
        :return: List of the new states.
        """
        possible_indices = get_possible_indices(self.zero_index)
        result = []
        for new_index in possible_indices:
            result.append(
                State(value=move_zero(self.value, self.zero_index, new_index),
                      depth=self.depth + 1,
                      cost=self.depth + 1,
                      zero_index=new_index)
            )
        return result

    # TODO
    def is_goal(self, custom_goal_state=36344967696) -> bool:
        """
        Function checks if the current state is equivalent to the goal state or not.
        :return: Boolean variable indicating the flag of the goal state.
        """
        if self.value == custom_goal_state:        # Goal state integer value
            return True
        else:
            return False

# TODO remove those comments
# array = [1, 2, 5, 8, 7, 6, 4, 0, 3]
# print(array)
# print("Getting its successors")
# a = convert_1d_to_int(array)
# s = State(a, 1, 1, 7)
# successors = s.expand()
# for i in range(len(successors)):
#     print("State: ", convert_int_to_1d(successors[i].value), ", Zero_position: ", successors[i].zero_index)
