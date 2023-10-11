from treeNode import node
from bfs import bfs 
from astarsearch import astar_search
from ids import ids
import time
import sys

# general search method, entry point for taking in a search algorithm, the map,
# the start node, and the goal node
def search(map: list, algorithm: str, startNode: node, goalNode: node):
    if algorithm.lower() == "bfs":
        start_time = time.time()
        cost, numExpandedNodes, maxNodes, path = bfs(startNode, goalNode, map, start_time)
        endTime = time.time() - start_time
        print("Total Cost: ", cost)
        print("Number of Expanded Nodes: ", numExpandedNodes)
        print("Max Number of Nodes Held in Memory: ", maxNodes)
        print("Path to Goal: ", path)
        print("Total time elapsed: ", endTime*1000, "milliseconds")
    elif algorithm.lower() == "a-star":
        start_time = time.time()
        cost, numExpandedNodes, maxNodes, path = astar_search(startNode, goalNode, map, start_time)
        endTime = time.time() - start_time
        print("Total Cost: ", cost)
        print("Number of Expanded Nodes: ", numExpandedNodes)
        print("Max Number of Nodes Held in Memory: ", maxNodes)
        print("Path to Goal: ", path)
        print("Total time elapsed: ", endTime*1000, "miliseconds")
    elif algorithm.lower() == "ids":
        start_time = time.time()
        cost, numExpandedNodes, maxNodes, path, elapsedTime = ids(startNode, goalNode, map, start_time)
        print("Total Cost: ", cost)
        print("Number of Expanded Nodes: ", numExpandedNodes)
        print("Max Number of Nodes Held in Memory: ", maxNodes)
        print("Path to Goal: ", path)
        print("Total time elapsed: ", elapsedTime, "miliseconds")

# Read file and store map into 2D array 
def readFromFile(fileName: str) -> (list, list, node, node):
    map = []
    dimensions = []
    startNode = node()
    goalNode = node()
   
   # reading the file
    with open(fileName, 'r') as f:
        dimensions = [int(x) for x in f.readline().split()] # first line
        startNode.setCoordinates([int(x) for x in f.readline().split()]) # second line
        
        goalNodeCoordinates = [int(x) for x in f.readline().split()] # third line
        goalNode.setCoordinates(goalNodeCoordinates)
        
        # reading through all the map coordinates and savind as a 2D list
        for _, line in enumerate(f):
            strLine = line.split(' ')
            intLine = [eval(i) for i in strLine]
            map.append(intLine)

        goalNode.setCost(map[goalNodeCoordinates[0]][goalNodeCoordinates[1]])
        
    return (map, dimensions, startNode, goalNode)

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

# starting point       
def main():
    fileName = sys.argv[1]
    searchAlgorithm = sys.argv[2]
    map, dimensions, startNode, goalNode = readFromFile(fileName)  
    
    # call the search method by passing in the map
    search(map, searchAlgorithm, startNode, goalNode)
    
if __name__ == "__main__":
    main()