from treeNode import node
import time
from search import getPathAndCost

# breadth-first search algorithm
def bfs(root: node, goalNode: node, map: list, start_time: time):
    if root is None:
        return
    queue = [root]
    visited = [root.coordinates]
    numExpandedNodes = 0
    maxNodes = 1

    while len(queue) > 0:
        # Check the elapsed time
        elapsedTime = time.time() - start_time
        if elapsedTime > 180:
            print("BFS search timed out after 3 minutes.")
            return -1, numExpandedNodes, maxNodes, None
          
        # keep track of maximum nodes held in queue
        if (len(queue) > maxNodes):
            maxNodes = len(queue)  
        
        cur_node = queue.pop(0) # FIFO queue
        
        # check if we have reached the goal node
        if cur_node.coordinates == goalNode.coordinates:
            # if we have, first get path and sum total cost
            path, cost = getPathAndCost(cur_node, root)
            return cost, numExpandedNodes, maxNodes, path
        
        # generate successor nodes for the current node we are in
        cur_node.generateSuccessorNodes(map)

        # for each successor node, we check if we can visit it. We can visit
        # a successor node if all following conditions are met:
        # (1) it is not None
        # (2) the node has not been visited before, and
        # (3) the node's cost is not 0 (not a barrier node)
        # we do this check for all 4 candidate successor nodes (left, right, up, down)
        if cur_node.left is not None:
            numExpandedNodes+=1
            if cur_node.left.coordinates not in visited and cur_node.left.cost != 0:
                visited.append(cur_node.left.coordinates)
                queue.append(cur_node.left)

        if cur_node.right is not None:
            numExpandedNodes += 1
            if cur_node.right.coordinates not in visited and cur_node.right.cost != 0:
                visited.append(cur_node.right.coordinates)
                queue.append(cur_node.right)
            
        if cur_node.up is not None:
            numExpandedNodes += 1
            if cur_node.up.coordinates not in visited and cur_node.up.cost != 0:
                visited.append(cur_node.up.coordinates)
                queue.append(cur_node.up)

        if cur_node.down is not None:
            numExpandedNodes += 1
            if cur_node.down.coordinates not in visited and cur_node.down.cost != 0:
                visited.append(cur_node.down.coordinates)
                queue.append(cur_node.down)
    
    # if while loop exits, means a path was not found            
    print("Path to goal not found")
    return -1, numExpandedNodes, maxNodes, None