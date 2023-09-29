from treeNode import node
# This can be the main file that will run. Here is where we can
# do the file reading, and according to user input, search using
# the specified search algorithm.

# Professor's Instructions:
# You must implement your program in either Java or Python and turn 
# in both the source code and an executable file that can be run on 
# the command line with the name of the map file and the solution 
# algorithm (BFS, IDS, AS) specified on the command line.  
# For example, I should be able to run your program using something 
# similar to (for Java):
# java –jar myProgram.jar map1.txt IDS

def search(map: list, algorithm: str):
    # TODO
    # This method can take care of calling whatever search algorithm was
    # specified. Then we will need to take care of returning the following:
    # Your program should run each search algorithm with a 3 minute time 
    # cutoff (i.e., you should stop the search with no result after a maximum 
    # of 3 minutes of runtime). For each of the three algorithms, print out 
    # the following information to the console:
    # 
    # 1)	The cost of the path found
    # 2)	The number of nodes expanded
    # 3)	The maximum number of nodes held in memory
    # 4)	The runtime of the algorithm in milliseconds
    # 5)	The path as a sequence of coordinates(row, col), (row col), …, (row, col)
    #
    # If the algorithm terminates without finding a result, print -1 for the
    # path cost and NULL for the path sequence. You should still print the 
    # number of nodes and the runtime.

    pass
   

## Read file and store map into 2D array 
def readFromFile(fileName) -> tuple:
    array2D = []
    dimensions = []
    startNode = node()
    goalNode = node()
   
   # first line: dimensions
    with open(fileName, 'r') as f:
        firstLine = f.readline()
        dimensions = firstLine.split()
        secondLine = f.readline()
        startNode.setCoordinates(secondLine)
        thirdLine = f.readline()
        goalNode.setCoordinates(thirdLine)
        for i, line in enumerate(f):
            strLine = line.split(' ')
            intLine = [eval(i) for i in strLine]
            array2D.append(intLine)

    return (array2D, dimensions, startNode, goalNode)


# the main method, starting point       
def main():
    # for now we can take user input from the command line
    # later on we can modify for when we create the executable
    fileName = input("Input name of file:")
    # algorithm = input("Input name of search algorithm:")
    readFromFile(fileName)
    # and then we can call the search method by passing in the 2D array
    # search(map, algorithm)
    
    # Write a method to generate successor nodes(this should be the same 
    # for all three searches!)
    # Write BFS - follow the pseudocode as closely as possible.
    # Add a “closed” list to check for repeated states
    # Test this first!
    
if __name__ == "__main__":
    main()