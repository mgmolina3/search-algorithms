from treeNode import node
import time
from pathAndCost import getPathAndCost

# iterative deepening search algorithm
def ids(root: node, goalNode: node, map: list, start_time: time):
    if root is None:
        return
    
    limit = 1 # start at limit = 1
    path = None
    elapsedTime = time.time() - start_time
    # while we have not found a path to the goal node and the elapsed time is less than 3 minutes
    while path is None and elapsedTime < 180:
        cost, numExpandedNodes, maxNodes, path = _idsLimitedSearch(root, goalNode, map, limit)
        elapsedTime = time.time() - start_time
        if path is not None: # if we found a path, return values
            return cost, numExpandedNodes, maxNodes, path, elapsedTime*1000
        limit+=1 # else increase the search depth limit
        
    if elapsedTime >= 180: # search timed out without finding a path
        print("IDS search timed out after 3 minutes.")
        return -1, numExpandedNodes, maxNodes, None, elapsedTime*1000

    return -1, numExpandedNodes, maxNodes, None, elapsedTime*1000
    

def _idsLimitedSearch(root: node, goalNode: node, map: list, limit: int):
    queue = [root]
    visited = [root.coordinates]
    numExpandedNodes = 0
    maxNodes = 1
    curDepth = 0
    
    while len(queue) > 0 and curDepth <= limit:
        # keep track of maximum nodes held in queue
        if (len(queue) > maxNodes):
            maxNodes = len(queue)
            
        cur_node = queue.pop() # LIFO queue

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
            numExpandedNodes += 1
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
                
        curDepth += 1
            
    # if while loop exits, means a path was not found
    return -1, numExpandedNodes, maxNodes, None