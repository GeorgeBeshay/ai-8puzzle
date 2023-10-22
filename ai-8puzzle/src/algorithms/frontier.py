
class Frontier:
    def __init__(self, data_structure="queue"):
        """ data_structure: String that is either queue or stack """
        self.ds = data_structure
        self.frontier = []


    def push(self, state):
        self.frontier.append(state)

    def pop(self):
        if self.ds.lower() == "stack":
            ans = self.frontier.pop() # pop the last element in the list
        elif self.ds.lower() == "queue":
            ans = self.frontier.pop(0) # pop the first element in the list
        return ans

    def size(self):
        return len(self.frontier)

