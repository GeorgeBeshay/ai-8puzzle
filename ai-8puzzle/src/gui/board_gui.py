import tkinter as tk
from src.algorithms.solution import *

background = "#15095A"
board = "#CD7F32"
button_bg = "#13C2D3"
border = "#080445"

class BoardGUI:
    def __init__(self, master, solution: Solution):
        self.master = master
        self.master.title("8-Puzzle Game")
        self.dimension = len(solution.get_first_step())
        self.tiles = {}
        self.current_step = solution.get_first_step()
        self.solution = solution

        # Create frame for the board
        board_frame = tk.Frame(master, bg=border, bd=2)
        board_frame.pack(pady=20)

        # Create board
        for i in range(self.dimension):
            for j in range(self.dimension):
                tile_value = self.current_step[i][j]
                label = tk.Label(
                    board_frame, text=str(tile_value), width=4, height=2, font=("Helvetica", 20),
                    bg=board, relief=tk.RAISED, borderwidth=2
                )
                label.grid(row=i, column=j)
                self.tiles[(i, j)] = label

        # Create frame for buttons
        button_frame = tk.Frame(master, bg=background)
        button_frame.pack(pady=20)
        # Create buttons
        previous_button = tk.Button(button_frame, text="Previous", bg=button_bg, padx=10, pady=5,
                                    borderwidth=2, command=self.get_previous_state)
        previous_button.pack(side=tk.LEFT, padx=10)  # Use side=tk.LEFT and padx for spacing

        next_button = tk.Button(button_frame, text="Next", bg=button_bg, padx=10, pady=5,
                                borderwidth=2, command=self.get_next_step)
        next_button.pack(side=tk.LEFT, padx=10)  # Use side=tk.LEFT and padx for spacing

        first_button = tk.Button(button_frame, text="First",bg=button_bg, padx=10, pady=5,
                                 borderwidth=2, command=self.get_first_state)
        first_button.pack(side=tk.LEFT, padx=10)  # Use side=tk.LEFT and padx for spacing

        last_button = tk.Button(button_frame, text="Last", bg=button_bg, padx=10, pady=5,
                                borderwidth=2, command=self.get_last_state)
        last_button.pack(side=tk.LEFT, padx=10)  # Use side=tk.LEFT and padx for spacing


    def get_next_step(self):
        next = self.solution.get_next_step()
        if(next != None):
            self.current_step = next
            self.update_gui()

    def get_first_state(self):
        first = self.solution.get_first_step()
        if(first != None):
            self.current_step = first
            self.update_gui()

    def get_last_state(self):
        last = self.solution.get_last_step()
        if(last != None):
            self.current_step = last
            self.update_gui()

    def get_previous_state(self):
        previous = self.solution.get_prev_step()
        if(previous != None):
            self.current_step = previous
            self.update_gui()

    def update_gui(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                tile_value = self.current_step[i][j]
                self.tiles[(i, j)].config(text=str(tile_value))

