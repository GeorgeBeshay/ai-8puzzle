from typing import List
from src.state.state_utilities import convert_int_to_1d


# Function to generate a plan from a parent_map and goal state
def generate_plan(parent_map: dict, int_goal_state: int) -> List[List[List[int]]]:
    plan: List[List[List[int]]] = []  # Initialize an empty list to store the plan
    temp_state: int = int_goal_state  # Start with the goal state
    while True and parent_map:  # While parent_map is not None
        # Convert the current state to a 2D list and append it to the plan
        plan.append([convert_int_to_1d(temp_state)[i:i + 3] for i in range(0, 9, 3)])
        if parent_map.get(temp_state) == temp_state:
            # If we reach the root state (where the initial state is
            # the parent of itself), exit the loop
            break
        else:
            temp_state = parent_map.get(temp_state)  # Move to the parent state
    plan.reverse()  # Reverse the plan to get it in the correct order
    return plan  # Return the generated plan


class Solution:
    """
    Represents a solution to a problem, including search-related information and a solution plan.
    This class is designed to encapsulate the details of a solution, providing access to the success flag,
    the maximum search depth, the cost of the solution, and a plan for reaching the solution.

    Attributes:
        success (bool): Indicates whether the solution was successful.
        max_search_depth (int): The maximum depth reached by the searching algorithm (not the solution depth).
        cost (int): The cost associated with the solution.
        plan (List[List[List[int]]]): A plan, represented as a 3D list of steps, for achieving the solution.
        iterator (int): An iterator for navigating through the plan.

    Methods:
        get_next_step(): Retrieves the next step in the plan. Returns None if the end of the plan is reached.
        reset_iterator(): Resets the iterator to the beginning of the plan.
        get_max_search_depth(): Returns the maximum search depth.
        is_success(): Checks if the solution was successful.
        get_cost(): Returns the cost of the solution.
    """
    def __init__(self, success: bool, parent_map: dict = None,
                 max_search_depth: int = 0, cost: int = 0, int_goal_state: int = 0):
        self.success = success  # Flag indicating whether the solution was successful
        # Maximum depth reached by the searching algorithm (not the solution depth)
        self.max_search_depth = max_search_depth
        self.cost = cost  # The cost of the solution
        self.plan: List[List[List[int]]] = generate_plan(parent_map, int_goal_state)  # Generate and store the plan
        self.iterator = 0  # Initialize an iterator to navigate through the plan

    # Method to get the next step in the plan
    def get_next_step(self):
        if self.iterator == len(self.plan):
            return None  # If we've reached the end of the plan, return None
        next_step = self.plan[self.iterator]  # Get the next step from the plan
        self.iterator += 1  # Increment the iterator for the next call
        return next_step

    # Method to reset the iterator to the beginning of the plan
    def reset_iterator(self): self.iterator = 0
    # Method to get the maximum depth reached by the searching algorithm (not the solution depth)
    def get_max_search_depth(self): return self.max_search_depth
    # Method to check if the solution was successful
    def is_success(self): return self.success
    # Method to get the cost of the solution
    def get_cost(self): return self.cost
