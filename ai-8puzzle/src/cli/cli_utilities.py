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
    """
    The 'scan_input' function is responsible for scanning the input puzzle and preparing it for the algorithm. The steps performed are as follows:
    1. It scans a 3x3 matrix, which represents the puzzle state.
    2. It prints the scanned 3x3 matrix to display it to the user.
    3. It converts the 2D matrix into a 1D array to prepare it for processing.
    4. It further converts the 1D array into an integer representation.
    5. It calculates the position of the zero element within the puzzle.
    6. The function returns two values:
       - 'int_start_state': The integer representation of the puzzle state.
       - 'zero_pos': The position of the zero element.

    The function is a crucial part of initializing the puzzle-solving process and providing the necessary data for the algorithm.
    :param:
    :return: initial_state (integer), zero_pos (integer).
    """
    matrix_state = scan_3x3_matrix()
    print("Scanned 3x3 matrix: ")
    display_in_2d(matrix_state)
    array_start_state = convert_2d_to_1d(matrix_state)
    int_start_state = convert_1d_to_int(array_start_state)
    zero_pos = zero_index(array_start_state)
    return int_start_state, zero_pos


def display_in_2d(matrix):
    print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n\n')


def scan_step_to_display(solution: Solution):
    """
    This function, 'scan_step_to_display', is responsible for interacting with the user to select the next step to display in the solution.
    It takes a 'Solution' object as input and displays a menu with options to choose from.
    It returns a tuple containing two values:
    1. A boolean indicating whether the user wants to continue querying for steps.
    2. The step to be displayed based on the user's choice.
    The function matches the user's input with the corresponding cases and returns the appropriate values.
    :param solution:
    :return: Tuple(bool, step)
    """
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
    """
    This function, 'display_solution', is used to display the solution to a puzzle-solving problem. It takes a 'Solution' object as input and performs the following tasks:
    1. Prints the elapsed running time in seconds.
    2. Checks if the solution was successful or not, and prints relevant information.
    3. If successful, it displays the total cost, total expanded nodes, and max search depth.
    4. Iteratively displays the solution steps (in 2D format) based on user input. (traversing through the plan).
    5. If the solution was not successful, it prints a message indicating that the problem couldn't be solved.
    The function provides a summary of the solution and its various attributes.
    :param solution:
    :return: void
    """

    print(f"Time Elapsed: {solution.get_running_time() :.5f} seconds")
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
