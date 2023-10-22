from typing import List


class State:
    def __init__(self, value: int, depth: int, cost: int, zero_position: int):
        self.value = value
        self.depth = depth
        self.cost = cost
        self.zero_position = zero_position

    # TODO
    def expand(self) -> List[int]:
        """
        Function expands the current state, to obtain the new possible reachable states from this one.
        :return: List of the new states.
        """
        return [self.value]

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
