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
