from src.algorithms.algs_factory import *
from cli_utilities import *
from src.state.state_utilities import *
import time
import os
from src.gui.draw_gui import runGUI

if __name__ == "__main__":
    '''
    This code is the main entry point for a puzzle-solving program. It follows the flow:
    1. Initialize a play_again flag to True to start the game loop.
    2. Inside the loop, it does the following:
       a. Scans the input puzzle and determines the position of the zero element.
       b. Scans and selects the search algorithm to be used.
       c. Prompts the user to choose between a graphical or text-based interface.
       d. Solves the puzzle using the chosen algorithm.
       e. Depending on the user's interface choice, either displays the solution in text or runs a GUI.
       f. Asks the user if they want to play again and continues if they choose 'Y'.
    3. The game loop continues until the user decides not to play again.
    '''
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
        # Displaying in the proper interface.
        if not in_gui or not sol.is_success():
            display_solution(sol)
        else:
            runGUI(sol)
        play_again = (input("Play again ? (Y / N): ").strip().upper()) == 'Y'
