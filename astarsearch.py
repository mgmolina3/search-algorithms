from treeNode import node
from pathAndCost import getPathAndCost
import time
import numpy as np

# A star search function, with default heuristic of manhattan distance
def astar_search(root: node, goalNode: node, map: list, start_time, heuristic): 
    if not root: 
        return None # tree is empty 
    
    priorityQueue = [] # prority queue to manage the nodes to explore 
    root.generateSuccessorNodes(map)
    
    visited = [root.coordinates] # keep track of visited nodes
    pathFound = False # used to keep track of if we have found a potential path already
    goalNodeFound = None # used to keep track if we have found a potential goal node
    numExpandedNodes = 0
    maxNodes = 1
    
    currentNode = root
    numExpandedNodes, priorityQueue, visited = exploreNodes(root, numExpandedNodes, priorityQueue, visited, heuristic)
    priorityQueue.sort(key=myFunc)
    
    while priorityQueue:
        # Check the elapsed time
        elapsedTime = time.time() - start_time
        if elapsedTime > 180:
            print("A-Star search timed out after 3 minutes.")
            return -1, numExpandedNodes, maxNodes, None
        
        # keep track of maximum nodes held in queue
        if (len(priorityQueue) > maxNodes):
            maxNodes = len(priorityQueue)
            
        currentNode = priorityQueue.pop(0) # pop node with least cost

        if currentNode.coordinates == goalNode.coordinates:
            # found one possible path, must check this is the least
            # costly path
            goalNodeFound = currentNode
            pathFound = True
            
            # found the least costly node already, return this one
            if priorityQueue[0].evalFunc < currentNode.evalFunc:
                path, cost = getPathAndCost(currentNode, root)
                return cost, numExpandedNodes, maxNodes, path

        # generate successor nodes for the current node we are in
        currentNode.generateSuccessorNodes(map)
        
        numExpandedNodes, priorityQueue, visited = exploreNodes(currentNode, numExpandedNodes, priorityQueue, visited, heuristic)
        priorityQueue.sort(key=myFunc)  

    if (pathFound):
        path, cost = getPathAndCost(goalNodeFound, root)
        return cost, numExpandedNodes, maxNodes, path
    
    return -1, numExpandedNodes, maxNodes, None # goalNode node not found 

# helper function to explore the successor nodes and add to priority queue
def exploreNodes(currentNode, numExpandedNodes, priorityQueue, visited, heuristic):
    # for each successor node, we check if we can visit it. We can visit
    # a successor node if all following conditions are met:
    # (1) it is not None
    # (2) the node has not been visited before, and
    # (3) the node's cost is not 0 (not a barrier node)
    # we do this check for all 4 candidate successor nodes (left, right, up, down)
    left = currentNode.left
    right = currentNode.right
    up = currentNode.up
    down = currentNode.down
    if left:
        numExpandedNodes += 1
        if left.cost != 0 and left.coordinates not in visited:
            left.computeEvalFunc(manhattan(currentNode, left))
            priorityQueue.append(left)
            visited.append(left.coordinates)
    if right:
        numExpandedNodes += 1
        if right.cost != 0 and right.coordinates not in visited:
            right.computeEvalFunc(manhattan(currentNode, right))
            priorityQueue.append(right)
            visited.append(right.coordinates)
    if up:
        numExpandedNodes += 1
        if up.cost != 0 and up.coordinates not in visited:
            up.computeEvalFunc(manhattan(currentNode, up))
            priorityQueue.append(up)
            visited.append(up.coordinates)
    if down:
        numExpandedNodes += 1
        if down.cost != 0 and down.coordinates not in visited:
            down.computeEvalFunc(manhattan(currentNode, down))
            priorityQueue.append(down)
            visited.append(down.coordinates)
            
    return numExpandedNodes, priorityQueue, visited

def myFunc(n):
    return n.evalFunc

# Manhattan Distance of two nodes
def manhattan(node1, node2):
    # compare coordinates of node1 to node2
    v1 = np.array(node1.coordinates)  # [x, y]
    v2 = np.array(node2.coordinates)  # [x, y]

    m = sum(abs(v1-v2))
    return m
