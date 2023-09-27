# Write a node class (stores coordinates and all necessary helper data;
# use the same node class for all three searches)

class node:
    coordinates: tuple # represents the coordinates of the current node
    cost: int # represents the cost of this node
    successorNodes: list # stores all successor nodes
    
    def __init__(self, coordinates, cost):
        self.coordinates = coordinates
        self.cost = cost
    
    # we can add more attributes/methods along the way