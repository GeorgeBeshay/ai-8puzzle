from typing import List


def convert_1d_to_int(array_state: List[int]) -> int:
    """
    Converts the 1D game state and returns the integer game state.

    Args:
        array_state (List[int]): A 1D input array.

    Returns:
        int: An integer result.
    """
    result = 0
    for i in range(len(array_state) - 1, 0, -1):
        result = result | array_state[i]
        result = result << 4
    result = result | array_state[0]
    return result


def convert_int_to_1d(int_state: int) -> List[int]:
    """
    Converts the int game state and return the 1D game state.

    Args:
        int_state (int): An integer input value.

    Returns:
        List[int]: A 1D output array (list of integers).
    """
    result = []
    while int_state != 0:
        result = result + [int_state & 15]
        int_state = int_state >> 4
    return result


def move_zero(current_state: int, zeroPlace: int, anotherPlace: int) -> int:
    """
    Move zero from its place to another place, and
    Move the another number to place of Zero.

    Args:
        current_state: int represent the value of current state
        zeroPlace: the place of zero
        anotherPlace: the place of another number

    :returns
         int: represent the value of new state
    """
    extractAnotherNum = ((15 << (anotherPlace * 4)) & (current_state)) >> (anotherPlace * 4)
    current_state = current_state & (~(15 << (anotherPlace * 4)))
    current_state = current_state | (extractAnotherNum << (zeroPlace * 4))
    return current_state
