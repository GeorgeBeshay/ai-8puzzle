from algs_factory import AlgorithmFactory
from utilities import scan_3x3_matrix, convert_int_to_matrix, convert_matrix_to_int, scan_algorithm_type

if __name__ == "__main__":
    # Creating an instance of the AlgorithmFactory
    factory = AlgorithmFactory()

    # Scan a 3x3 matrix
    matrix_state = scan_3x3_matrix()
    print("Scanned 3x3 matrix: ", matrix_state)
    integer_start_state = convert_matrix_to_int(matrix_state)
    integer_goal_state = convert_matrix_to_int([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    # Scan the required search algorithm to be used
    alg_name = scan_algorithm_type()
    print("Selected Algorithm: ", alg_name)
    algorithm = factory.get_algorithm(alg_name)

    """
    Apply the algorithm, the plan is the set of sequential steps (integer states) to be applied to reach the goal.
    Plan of integers states must be converted to a plan of matrix states
    """
    integers_plan = algorithm.search(integer_start_state, integer_goal_state)
    print("Here ..", integers_plan)
    matrix_plan = [convert_int_to_matrix(integer_state) for integer_state in integers_plan]
    print(matrix_plan)
