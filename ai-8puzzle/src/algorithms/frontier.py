from src.state.state import State


class Frontier:
    def __init__(self, data_structure="queue"):
        """
        Initializes a frontier object to be used for storing storing nodes and expanding them.

        Args:
        data_structure: str that that specifies the data structure to use, either 'queue' or 'stack'
        """
        if data_structure.lower() not in ["stack", "queue"]:
            raise Exception("Wrong Data Type For Frontier")
        self.ds = data_structure
        self.frontier = []

    def push(self, state: State):
        """
            Pushes a state onto the frontier.

            Args:
                state: The state to be added to the frontier.
        """
        self.frontier.append(state)

    def pop(self):
        """
            Removes and returns a state from the frontier based on the specified data structure ('stack' or 'queue').

            Returns:
                The state removed from the frontier.
        """

        if self.ds.lower() == "stack":
            ans = self.frontier.pop() # pop the last element in the list
        elif self.ds.lower() == "queue":
            ans = self.frontier.pop(0) # pop the first element in the list
        return ans

    def size(self):
        """
            Function that returns the number of elements in the frontier.

            Returns:
                The number of elements in the frontier.
        """
        return len(self.frontier)

