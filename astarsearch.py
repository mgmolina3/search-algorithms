import heapq
from treeNode import node
import time
from treeNode import NodeWithPriority
    
def astar_search(root: node, goalNode: node, map: list): 
    if not root: 
        return None #tree is empty 
    
    open_set = [] #prority queue to manage the nodes to explore 
    heapq.heappush(open_set, NodeWithPriority(root,0))


    while open_set: 

        current_node = heapq.heappop(open_set).node

        if current_node.coordinates == goalNode.coordinates: 
            return current_node ##goal node is found 
        

        # generate successor nodes for the current node we are in
        current_node.generateSuccessorNodes(map)

        left_child = current_node.left
        right_child = current_node.right 
        upper_child = current_node.up
        lower_child = current_node.down

        #calculate heursitic for each child node 

        if left_child is not None: 
            left_priority = heuristic(left_child, goalNode)
            print(left_priority)
            heapq.heappush(open_set, NodeWithPriority(left_child, left_priority))
        
        if right_child is not None: 
            right_priority = heuristic(right_child, goalNode)
            heapq.heappush(open_set, NodeWithPriority(right_child, right_priority))
        
        if upper_child is not None: 
            upper_priority = heuristic(upper_child, goalNode)
            heapq.heappush(open_set, NodeWithPriority(upper_child, upper_priority))

        if lower_child is not None: 
            lower_priority = heuristic(lower_child, goalNode)
            heapq.heappush(open_set, NodeWithPriority(lower_child, lower_priority))
    
    return None ## goalNode node not found 

def heuristic(node, goalNode): 
    return abs(node.cost - goalNode.cost)

        


    


