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


def move_zero(current_state: int, current_zero_position: int, new_zero_position: int) -> int:
    """
    Swaps the zero from the current_zero_position to the new_zero_position

    Args:
        current_state: int represent the value of current state.
        current_zero_position: current index of the zero.
        new_zero_position: index of the element to be swapped with the zero (new index of the zero).

    :returns:
         int: represent the value of new state
    """
    extract_another_num = ((15 << (new_zero_position * 4)) & current_state) >> (new_zero_position * 4)
    current_state = current_state & (~(15 << (new_zero_position * 4)))
    current_state = current_state | (extract_another_num << (current_zero_position * 4))
    return current_state


def get_possible_indices(current_zero_position: int) -> List[int]:
    result = []
    match current_zero_position:
        case 0:
            result = [3, 1]
        case 1:
            result = [0, 4, 2]
        case 2:
            result = [1, 5]
        case 3:
            result = [0, 6, 4]
        case 4:
            result = [1, 3, 7, 5]
        case 5:
            result = [2, 4, 8]
        case 6:
            result = [3, 7]
        case 7:
            result = [4, 6, 8]
        case 8:
            result = [5, 7]
    return result
