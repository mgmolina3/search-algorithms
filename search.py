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
    
# the main method, starting point       
def main():
    # for now we can take user input from the command line
    # later on we can modify for when we create the executable
    fileName = input("Input name of file:")
    algrithm = input("Input name of search algorithm:")
    # TODO: read file (can be here or in a method)
    
    # and then we can call the search method by passing in the 2D array
    # search(map, algorithm)
    
if __name__ == "__main__":
    main()