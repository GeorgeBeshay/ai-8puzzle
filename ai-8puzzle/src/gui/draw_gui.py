import tkinter as tk
from src.gui.board_gui import BoardGUI
from src.algorithms.solution import *
from src.state.state import *
from src.state.state_utilities import *
from src.algorithms.algs_dfs_bfs import *

background = "#1B1212"


def runGUI(solution: Solution):
    root = tk.Tk()
    root.geometry('500x500')
    # root.eval('tk::PlaceWindow . center')
    root.config(bg=background)
    boardGUI = BoardGUI(root, solution)
    root.mainloop()
