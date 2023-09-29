# Write a node class (stores coordinates and all necessary helper data;
# use the same node class for all three searches)

class node:
    coordinates: list # represents the coordinates of the current node
    cost: int = 0 # represents the cost of this node
    successorNodes: list # stores all successor nodes
    left = None
    right = None
    up = None
    down = None
    
    def setCoordinates(self, coordinates):
        self.coordinates = coordinates
      
    def setCost(self, cost):
        self.cost = cost
        
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def setUp(self, up):
        self.up = up
        
    def setDown(self, down):
        self.down = down
    
    def __str__(self):
        return "Cost: " + str(self.cost) + "\nCoordinates: " + str(self.coordinates)
    # we can add more attributes/methods along the way
    
    def generate_successor_nodes(self, map):
        # start at self coordinates
        x = self.coordinates[0] # start here
        y = self.coordinates[1]
        
        # left is -1 on y coordinate
        checkLeft = map[x][y-1] # if statement here
        # if can't go to left: nothing
        # if you can
        left = node()
        left.setCoordinates([x, y-1])
        left.setCost(map[x][y-1])
        self.setLeft(left)
        # up is -1 on x coordinate
        # down is +1 on x
        # right is +1 on y
        # if possible, generate child node
        
        # else don't
    
[2, 4, 2, 1, 4, 5, 2]
[0, 1, 2, 3, 5, 3, 1]
[2, 0, 4, 4, 1, 2, 4]
[2, 5, 5, 3, 2, 0, 1]
[4, 3, 3, 2, 1, 0, 1]
# pseudocode:
# successor_nodes(map, parentNode):
#   get coordinates from parent
#   check to see (using map) if you can move up, down, right, left
#   if you can, generate successor node
#   return successor nodes
