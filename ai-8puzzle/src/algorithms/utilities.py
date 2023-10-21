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


# Note that the '_' prefix in the function name means it is private, and should not be called out of this file.
def _convert_2d_to_1d(matrix):
    """
    Function to convert a 2D matrix (list of lists) to a 1D list.
    """
    return [value for row in matrix for value in row]


def _convert_1d_to_2d(arr):
    """
    Function to convert a 1D array to a 2D matrix of size 3 x 3.
    """
    if len(arr) != 9:
        raise ValueError("Input 1D array must have 9 elements to form a 3x3 matrix.")

    matrix = []
    for i in range(3):
        matrix.append(arr[i * 3: (i + 1) * 3])

    return matrix


def _convert_1d_to_string(matrix):
    """
    Function to convert a 1D matrix (list) to a string of integers concatenated.
    """
    return ''.join(map(str, matrix))


def _convert_string_to_1d(input_string):
    """
    Function to convert a string of digits to an integer 1D array.
    """
    return [int(digit) for digit in input_string]


def _convert_string_to_int(input_string):
    """
    Function to convert a string of integers to an integer.
    """
    return int(input_string)


def _convert_int_to_string(num):
    """
    Function to convert an integer to a string of digits (1 digit per element in a list).
    """
    return [digit for digit in str(num)]


def convert_matrix_to_int(matrix: List[List[int]]) -> int:
    """
    Function to convert a 2D Matrix of integers to the corresponding integer state value
    :param matrix:
    :return: the integer version of the state
    """
    return _convert_string_to_int(_convert_1d_to_string(_convert_2d_to_1d(matrix)))


def convert_int_to_matrix(int_state: int) -> List[List[int]]:
    """
    Function to convert the integer state of the game to the corresponding 2D matrix state.
    :param int_state:
    :return:
    """
    return _convert_1d_to_2d(_convert_string_to_1d(_convert_int_to_string(int_state)))
