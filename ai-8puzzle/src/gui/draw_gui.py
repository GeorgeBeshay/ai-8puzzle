import tkinter as tk
from src.gui.board_gui import BoardGUI
from src.algorithms.solution import *
from src.state.state import *
from src.state.state_utilities import *
from src.algorithms.algs_dfs_bfs import *

background = "#15095A"

def runGUI(solution: Solution):
    root = tk.Tk()
    root.geometry('350x350')
    root.eval('tk::PlaceWindow . center')
    root.config(bg=background)
    boardGUI = BoardGUI(root, solution)
    root.mainloop()


init_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
s = State(convert_1d_to_int(init_state), 0, 0, 5)
solutions = [depth_first_search(s)]

for solution in solutions:
    if solution.is_success():
        runGUI(solution)
        plan_step = solution.get_next_step()
        while plan_step is not None:
            print(f'{plan_step[0]}\n{plan_step[1]}\n{plan_step[2]}\n\n')
            plan_step = solution.get_next_step()
        print(f"Total Cost: {solution.get_cost()}")
        print(f"Total Expanded Nodes: {solution.get_nodes_expanded()}")
        print(f"Max Search Depth: {solution.get_max_search_depth()}")
        print(f"First Step: {solution.get_first_step()}")
        print(f"Last Step: {solution.get_last_step()}")
    else:
        print("Couldn't solve")
    print(" --------------------------------------- END --------------------------------------- ")