from treeNode import node
import time
import numpy as np

# For A* search you should use the Manhattan distance as your heuristic,
# but implement the algorithm in a general way so that a new heuristic
# could be used.

# Write A * search
# * write a simple comparator class, or implement a compareTo method in
# your Node class to allow you to use a PriorityQueue (builtin java class)
# to maintain a sorted list of nodes

# function:
# f(n) = g(n) + h(n)
# g(n) = cost so far
# h(n) = manhattan distance

def myFunc(n):
    return n.evalFunc
    
def astar_search(root: node, goalNode: node, map: list): 
    if not root: 
        return None #tree is empty 
    
    priorityQueue = [] #prority queue to manage the nodes to explore 
    root.generateSuccessorNodes(map)
    visited = [root.coordinates]
    
    left = root.left
    right = root.right
    up = root.up
    down = root.down
    if left and left.cost != 0:
        left.computeEvalFunc(manhattan(root, left))
        priorityQueue.append(left)
        visited.append(left.coordinates)
    if right and right.cost != 0:
        right.computeEvalFunc(manhattan(root, right))
        priorityQueue.append(right)
        visited.append(right.coordinates)
    if up and up.cost != 0:
        up.computeEvalFunc(manhattan(root, up))
        priorityQueue.append(up)
        visited.append(up.coordinates)
    if down and down.cost != 0:
        down.computeEvalFunc(manhattan(root, down))
        priorityQueue.append(down)
        visited.append(down.coordinates)
    priorityQueue.sort(key=myFunc)
    
    while priorityQueue:
        current_node = priorityQueue.pop(0)

        if current_node.coordinates == goalNode.coordinates:
            # found one possible path, must check this is the least
            # costly path
            print("Found one goal node!")
            path, _ = getPathAndCost(current_node, root)
            cost = current_node.evalFunc
            print("Path of current found goal node: ", path)
            print("Cost of current found goal node: ", cost)
            if priorityQueue[0].evalFunc > current_node.evalFunc:
                # stop looping
                print("Found goal node!")
                path, _ = getPathAndCost(current_node, root)
                cost = current_node.evalFunc
                return path, cost # whatever else we need

        # generate successor nodes for the current node we are in
        current_node.generateSuccessorNodes(map)
        
        left = current_node.left
        right = current_node.right
        up = current_node.up
        down = current_node.down
        if left and left.cost != 0 and left.coordinates not in visited:
            left.computeEvalFunc(manhattan(root, left))
            priorityQueue.append(left)
            visited.append(left.coordinates)
        if right and right.cost != 0 and right.coordinates not in visited:
            right.computeEvalFunc(manhattan(root, right))
            priorityQueue.append(right)
            visited.append(right.coordinates)
        if up and up.cost != 0 and up.coordinates not in visited:
            up.computeEvalFunc(manhattan(root, up))
            priorityQueue.append(up)
            visited.append(up.coordinates)
        if down and down.cost != 0 and down.coordinates not in visited:
            down.computeEvalFunc(manhattan(root, down))
            priorityQueue.append(down)
            visited.append(down.coordinates)
        priorityQueue.sort(key=myFunc)  

    return None, None ## goalNode node not found 
        
# Manhattan Distance of two nodes
def manhattan(node1, node2):
    # compare coordinates of node1 to node2
    v1 = np.array(node1.coordinates) # [x, y]
    v2 = np.array(node2.coordinates) # [x, y]
    
    m = sum(abs(v1-v2))
    return m

# helper method which finds the path from the goal node to the start node
# and calculates the total cost


def getPathAndCost(goalNode, startNode):
    pathRev = []
    cur_node = goalNode
    cost = 0
    # adds them in reverse order, from goal node to start node
    while cur_node.coordinates != startNode.coordinates:
        pathRev.append(cur_node.coordinates)
        cost += cur_node.cost
        cur_node = cur_node.parent
    pathRev.append(startNode.coordinates)
    cost += startNode.cost
    # reverse the path
    path = pathRev[::-1]
    return path, cost
