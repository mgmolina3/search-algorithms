class node:
    coordinates: list[int] # represents the coordinates of the current node
    cost: int = 0 # represents the cost of this node
    parent = None # parent node of this node
    # the following are the successor nodes, if any, that will be generated
    left = None
    right = None
    up = None
    down = None
    evalFunc = 0
    
    def __init__(self, coordinates: list[int] = None, cost: int = 0, parent = None) -> None:
        self.coordinates = coordinates
        self.cost = cost
        self.parent = parent
        
    def __str__(self):
        return "Cost: " + str(self.cost) + "\nCoordinates: " + str(self.coordinates) + "\nParent: " + str(self.parent)
    
    def setCoordinates(self, coordinates: list):
        self.coordinates = coordinates
      
    def setCost(self, cost: int):
        self.cost = cost
        
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def setUp(self, up):
        self.up = up
        
    def setDown(self, down):
        self.down = down
        
    def computeEvalFunc(self, heuristic):
        self.evalFunc = self.cost + heuristic
    
    def compareTo(self, node): # returns true if self is priority
        return self.evalFunc < node.evalFunc
    
    def generateSuccessorNodes(self, map: list):
        # start at self coordinates
        x = self.coordinates[0]
        y = self.coordinates[1]
        
        # check left (-1 on y coordinate)
        if y != 0:
            # generate left successor node
            self.left = node([x, y-1], map[x][y-1], self)
        # check right (+1 on y coordinate)
        if y != len(map[x])-1:
            # generate right successor node
            self.right = node([x, y+1], map[x][y+1], self)
        # check up (-1 on x coordinate)
        if x != 0:
            # generate up successor node
            self.up = node([x-1, y], map[x-1][y], self)
        # check down (+1 on x coordinate)
        if x != len(map)-1:
            # generate down successor node
            self.down = node([x+1, y], map[x+1][y], self)