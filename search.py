from treeNode import node
from bfs import bfs 
from astarsearch import astar_search
from ids import ids
import time
import sys
import numpy as np

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
        cost, numExpandedNodes, maxNodes, path = astar_search(startNode, goalNode, map, start_time, manhattan)
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

# Manhattan Distance of two nodes
def manhattan(node1, node2):
    # compare coordinates of node1 to node2
    v1 = np.array(node1.coordinates)  # [x, y]
    v2 = np.array(node2.coordinates)  # [x, y]

    m = sum(abs(v1-v2))
    return m

# starting point       
def main():
    fileName = sys.argv[1]
    searchAlgorithm = sys.argv[2]
    map, dimensions, startNode, goalNode = readFromFile(fileName)  
    
    # call the search method by passing in the map
    search(map, searchAlgorithm, startNode, goalNode)
    
if __name__ == "__main__":
    main()