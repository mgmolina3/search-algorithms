# This can be the file for breath-first search algorithm
# keep track of total cost
# timer
from treeNode import node

def bfs(root: node, goalNode: node, map: list):
    if root is None:
        return
    queue = [root]
    visited = [root.coordinates]
    numExpandedNodes = 0

    while len(queue) > 0:
        cur_node = queue.pop(0)
        
        if cur_node.coordinates == goalNode.coordinates:
            # first sum up totalCost
            path, totalCost = getPathAndCost(cur_node, root)
            depth = len(path) - 1
            return visited, path, totalCost, depth, numExpandedNodes
        
        cur_node.generateSuccessorNodes(map)

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
        
def getPathAndCost(endNode, startNode):
    pathRev = []
    cur_node = endNode
    cost = 0
    while cur_node.coordinates != startNode.coordinates:
        pathRev.append(cur_node.coordinates)
        cost += cur_node.cost
        cur_node = cur_node.parent
    pathRev.append(startNode.coordinates)
    cost += startNode.cost
    # reverse the path
    path = pathRev[::-1]
    return path, cost