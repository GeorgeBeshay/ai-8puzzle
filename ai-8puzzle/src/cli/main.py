from src.algorithms.algs_factory import *
from cli_utilities import *
from src.state.state_utilities import *
import time
import os
from src.gui.draw_gui import runGUI

if __name__ == "__main__":
    play_again = True
    while play_again:
        # Scan the input, and prepare the algorithm input.
        initial_state, zero_pos = scan_input()
        # Scan the required search algorithm to be used.
        algorithm = algorithm_factory(scan_algorithm_type())
        # Choosing the desired interface
        in_gui = (input("Display result in GUI ? (Y / N): ").strip().upper()) == 'Y'
        # Solve the problem
        sol = algorithm(State(initial_state, 0, 0, zero_pos))
        if not in_gui or not sol.is_success():
            display_solution(sol)
        else:
            runGUI(sol)

        play_again = (input("Play again ? (Y / N): ").strip().upper()) == 'Y'
