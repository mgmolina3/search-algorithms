from treeNode import node
from search import getPathAndCost
import time
import numpy as np

# Manhattan Distance of two nodes
def manhattan(node1, node2):
    # compare coordinates of node1 to node2
    v1 = np.array(node1.coordinates)  # [x, y]
    v2 = np.array(node2.coordinates)  # [x, y]

    m = sum(abs(v1-v2))
    return m

# A star search function, with default heuristic of manhattan distance
def astar_search(root: node, goalNode: node, map: list, heuristic=manhattan): 
    if not root: 
        return None # tree is empty 
    
    priorityQueue = [] # prority queue to manage the nodes to explore 
    root.generateSuccessorNodes(map)
    
    visited = [root.coordinates] # keep track of visited nodes
    pathFound = False # used to keep track of if we have found a potential path already
    goalNodeFound = None # used to keep track if we have found a potential goal node
    numExpandedNodes = 0
    maxNodes = 1
    
    numExpandedNodes, priorityQueue, visited = exploreNodes(root, numExpandedNodes, priorityQueue, visited, heuristic)
    priorityQueue.sort(key=myFunc)
    
    while priorityQueue:
        # keep track of maximum nodes held in queue
        if (len(priorityQueue) > maxNodes):
            maxNodes = len(priorityQueue)
            
        current_node = priorityQueue.pop(0) # pop node with least cost

        if current_node.coordinates == goalNode.coordinates:
            # found one possible path, must check this is the least
            # costly path
            goalNodeFound = current_node
            pathFound = True
            path, _ = getPathAndCost(goalNodeFound, root)
            cost = goalNodeFound.evalFunc
            
            # found the least costly node already, return this one
            if priorityQueue[0].evalFunc < current_node.evalFunc:
                path, _ = getPathAndCost(current_node, root)
                cost = current_node.evalFunc
                return cost, numExpandedNodes, maxNodes, path

        # generate successor nodes for the current node we are in
        current_node.generateSuccessorNodes(map)
        
        numExpandedNodes, priorityQueue, visited = exploreNodes(current_node, numExpandedNodes, priorityQueue, visited, heuristic)
        priorityQueue.sort(key=myFunc)  

    if (pathFound):
        path, _ = getPathAndCost(goalNodeFound, root)
        cost = goalNodeFound.evalFunc
        return cost, numExpandedNodes, maxNodes, path
    
    return -1, numExpandedNodes, maxNodes, None # goalNode node not found 

# helper function to explore the successor nodes and add to priority queue
def exploreNodes(node, numExpandedNodes, priorityQueue, visited, heuristic):
    # for each successor node, we check if we can visit it. We can visit
    # a successor node if all following conditions are met:
    # (1) it is not None
    # (2) the node has not been visited before, and
    # (3) the node's cost is not 0 (not a barrier node)
    # we do this check for all 4 candidate successor nodes (left, right, up, down)
    if node.left is not None:
        numExpandedNodes += 1
        if node.left and node.left.cost != 0:
            node.left.computeEvalFunc(heuristic(node, node.left))
            priorityQueue.append(node.left)
            visited.append(node.left.coordinates)
    
    if node.right is not None:
        numExpandedNodes += 1
        if node.right and node.right.cost != 0:
            node.right.computeEvalFunc(heuristic(node, node.right))
            priorityQueue.append(node.right)
            visited.append(node.right.coordinates)
    
    if node.up is not None:
        numExpandedNodes += 1
        if node.up and node.up.cost != 0:
            node.up.computeEvalFunc(heuristic(node, node.up))
            priorityQueue.append(node.up)
            visited.append(node.up.coordinates)
    
    if node.down is not None:
        numExpandedNodes += 1
        if node.down and node.down.cost != 0:
            node.down.computeEvalFunc(heuristic(node, node.down))
            priorityQueue.append(node.down)
            visited.append(node.down.coordinates)
    
    return numExpandedNodes, priorityQueue, visited

def myFunc(n):
    return n.evalFunc