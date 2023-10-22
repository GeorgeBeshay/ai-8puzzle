from typing import List
from src.state.state_utilities import *

class State:
    def __init__(self, value: int, depth: int, cost: int , zero_position: int):
        self.value = value
        self.depth = depth
        self.cost = cost
        self.zero_position = zero_position

    # TODO: What the value of cost of each successor
    def expand(self) -> List[int]:
        """
        Function expands the current state, to obtain the new possible reachable states from this one.
        :return: List of the new states.
        """
        possiblePlaces = getPossiblePlaces(self.zero_position)
        result = []
        for place in possiblePlaces:
            result.append(State(value=move_zero(self.value, self.zero_position, place),
                                depth=self.depth + 1, cost=self.depth + 1, zero_position=place))
        return result

    # TODO
    def is_goal(self) -> bool:
        """
        Function checks if the current state is equivalent to the goal state or not.
        :return: Boolean variable indicating the flag of the goal state.
        """
        if self.value == 12345678:
            return True
        else:
            return False

# array = [6, 0, 1, 4, 5, 3, 2, 4, 7]
# print(array)
# print("Getting its successors")
# a = convert_1d_to_int(array)
# s = State(a, 1, 1, 1)
# successors = s.expand()
# for i in range(len(successors)):
#     print("State: ", convert_int_to_1d(successors[i].value), ", Zero_position: ", successors[i].zero_position)