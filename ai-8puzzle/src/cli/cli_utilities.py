from src.state.state_utilities import convert_1d_to_int
from src.algorithms.solution import Solution

"""
Implementing all the utilities to be used when dealing with the CLI, such as scanning input, converting it, etc..
"""
from typing import List


def scan_algorithm_type():
    """
    Function to scan the type of the search algorithm from user input.
    Returns the algorithm type as a string.
    """
    while True:
        algorithm_type = input("Enter the search algorithm type (DFS, BFS, or A*): ").strip().upper()
        if algorithm_type in {"DFS", "BFS", "A*"}:
            return algorithm_type
        else:
            print("Invalid algorithm type. Please enter DFS, BFS, or A*.")


def scan_3x3_matrix():
    """
    Function to scan a 3x3 matrix of integers from the user.
    Returns a list of lists representing the 3x3 matrix.
    """
    matrix = []
    for i in range(3):
        row = input(f"Enter 3 integers for row {i + 1} separated by spaces: \n")
        row_values = [int(x) for x in row.split()]
        if len(row_values) != 3:
            raise ValueError("You must enter exactly 3 integers per row.")
        matrix.append(row_values)
    return matrix


def convert_2d_to_1d(matrix):
    """
    Function to convert a 2D matrix (list of lists) to a 1D list.
    """
    return [value for row in matrix for value in row]


def zero_index(init_list: List[int]) -> int:
    for i in range(len(init_list)):
        if init_list[i] == 0:
            return i


def convert_1d_to_2d(arr):
    """
    Function to convert a 1D array to a 2D matrix of size 3 x 3.
    """
    if len(arr) != 9:
        raise ValueError("Input 1D array must have 9 elements to form a 3x3 matrix.")

    matrix = []
    for i in range(3):
        matrix.append(arr[i * 3: (i + 1) * 3])

    return matrix


def scan_input():
    matrix_state = scan_3x3_matrix()
    print("Scanned 3x3 matrix: ")
    display_in_2d(matrix_state)
    array_start_state = convert_2d_to_1d(matrix_state)
    int_start_state = convert_1d_to_int(array_start_state)
    int_goal_state = convert_1d_to_int(convert_2d_to_1d([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    zero_pos = zero_index(array_start_state)
    return int_start_state, zero_pos


def display_in_2d(matrix):
    print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n\n')


def scan_step_to_display(solution: Solution):
    state_to_display = int(input("Enter the desired option number:\n1- First Step (1)\n2- Previous Step (2)\n"
                                 "3- Next Step (3)\n4- Last Step (4)\n5- Exit (5)\n").split()[0])
    match state_to_display:
        case 1:
            return True, solution.get_first_step()
        case 2:
            return True, solution.get_prev_step()
        case 3:
            return True, solution.get_next_step()
        case 4:
            return True, solution.get_last_step()
        case 5:
            return False, None


def display_solution(solution: Solution):
    if solution.is_success():
        print(f"Total Cost: \t\t\t{solution.get_cost()}")
        print(f"Total Expanded Nodes: {solution.get_nodes_expanded()}")
        print(f"Max Search Depth: {solution.get_max_search_depth()}")

        still_querying, step = scan_step_to_display(solution)
        while still_querying:
            display_in_2d(step)
            still_querying, step = scan_step_to_display(solution)
    else:
        print("Couldn't solve")
    print(f"Time Elapsed: {solution.get_running_time() :.2f} seconds")
