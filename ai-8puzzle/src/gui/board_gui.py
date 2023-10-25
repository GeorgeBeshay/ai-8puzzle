import tkinter as tk
from src.algorithms.solution import *

background = "#1B1212"
board = "#CD7F32"
button_bg = "#FFC000"
border = "#7B3F00"
text_background = "#4169E1"

class BoardGUI:
    def __init__(self, master, solution: Solution):
        self.master = master
        self.master.title("8-Puzzle Game")
        self.dimension = len(solution.get_first_step())
        self.tiles = {}
        self.current_step = solution.get_first_step()
        self.solution = solution

        # Create frame for the text to be printed
        text_frame = tk.Frame(master=master, bg=border, bd=2)
        text = "Total Cost: " + str(solution.get_cost()) + "\n"
        text += "Total Expanded Nodes: " + str(solution.get_nodes_expanded()) + "\n"
        text += "Max Search Depth: " + str(solution.get_max_search_depth()) + "\n"
        text += "Time Elapsed: {:.5f} seconds".format(solution.get_running_time())


        label = tk.Label(
            text_frame, text=text, font=("Helvetica", 10),
            bg=text_background, relief=tk.RAISED, borderwidth=2, fg="white", pady=10, padx=10
        )
        label.grid(row=0, column=1)
        text_frame.pack(pady=20)

        # Create frame for the board
        board_frame = tk.Frame(master, bg=border, bd=2)
        board_frame.pack(pady=20)

        # Create board
        for i in range(self.dimension):
            for j in range(self.dimension):
                tile_value = self.current_step[i][j]
                text = ""
                if(tile_value != 0):
                    text = str(tile_value)
                label = tk.Label(
                    board_frame, text=text, width=4, height=2, font=("Helvetica", 20),
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
                text = ""
                if(tile_value != 0):
                    text = str(tile_value)
                self.tiles[(i, j)].config(text=text)

