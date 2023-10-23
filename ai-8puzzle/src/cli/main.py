from src.algorithms.algs_factory import *
from cli_utilities import *
from src.state.state_utilities import *

if __name__ == "__main__":
    # Creating an instance of the AlgorithmFactory

    # Scan a 3x3 matrix
    matrix_state = scan_3x3_matrix()
    print("Scanned 3x3 matrix: ", matrix_state)
    array_start_state = convert_2d_to_1d(matrix_state)
    int_start_state = convert_1d_to_int(array_start_state)
    array_goal_state = convert_2d_to_1d([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    int_goal_state = convert_1d_to_int(array_goal_state)

    # Scan the required search algorithm to be used
    alg_name = scan_algorithm_type()
    print("Selected Algorithm: ", alg_name)
    algorithm = algorithm_factory(alg_name)

    """
    Apply the algorithm, the plan is the set of sequential steps (integer states) to be applied to reach the goal.
    Plan of integers states must be converted to a plan of matrix states
    """
    integers_plan = algorithm(int_start_state, int_goal_state)
    print("Here ..", integers_plan)
    matrix_plan = [convert_int_to_1d(integer_state) for integer_state in integers_plan]
    print(matrix_plan)
