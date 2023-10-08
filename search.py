from treeNode import node
from bfs import bfs 
from ids import ids
import time
import sys

# general search method, entry point for taking in a search algorithm, the map,
# the start node, and the goal node
def search(map: list, algorithm: str, startNode: node, goalNode: node):
    if algorithm.lower() == "bfs":
        start_time = time.time()
        visited, path, totalCost, depth, numExpandedNodes = bfs(startNode, goalNode, map, start_time)
        endTime = time.time() - start_time
        print("Visited Nodes: ", visited)
        print("Path to Goal: ", path)
        print("Total Cost: ", totalCost)
        print("Depth: ", depth)
        print("Number of Expanded Nodes: ", numExpandedNodes)
        print("Total time elapsed: ", endTime*1000, "miliseconds")
    elif algorithm.lower() == "ids":
        start_time = time.time()
        visited, path, totalCost, depth, numExpandedNodes, elapsedTime = ids(startNode, goalNode, map, start_time)
        print("Visited Nodes: ", visited)
        print("Path to Goal: ", path)
        print("Total Cost: ", totalCost)
        print("Depth: ", depth)
        print("Number of Expanded Nodes: ", numExpandedNodes)
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

# starting point       
def main():
    fileName = sys.argv[1]
    searchAlgorithm = sys.argv[2]
    map, dimensions, startNode, goalNode = readFromFile(fileName)   
    
    # call the search method by passing in the map
    search(map, searchAlgorithm, startNode, goalNode)
    
if __name__ == "__main__":
    main()