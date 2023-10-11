# search-algorithms

created by Montserrat Molina & Andrea Ulloa

## Getting Started

To clone this repo, run `git clone https://github.com/mgmolina3/search-algorithms.git`

## Running our Project

In the project directory, you can run:

### For Windows: `python3 search.py <name of text file>.txt <searchAlgorithm>`

### For Mac: `./search <name of text file>.txt <searchAlgorithm>`

### Search Algorithms Accepted: `bfs` `ids` and `a-star`, in this exact format

## Features

Search a given map text file with a specified search algorithm. Currently, this project supports breadth-first search, iterative-deepening search, and a-star search algorithms.

### Breadth-First Search

The algorithm uses the given start node, goal node, and map to traverse the map text file and find a path from the start node to the goal node by using breath-first search traversal of the tree. It generates four successor child nodes for every current node it is traversing. These four successor child nodes represent the left, right, up, and down directions from the map. For each successor node, BFS will check if it can visit the node. The node can be visited if all the following conditions are met:
(1) it is not None
(2) the node has not been visited before, and
(3) the node's cost is not 0 (not a barrier node) we do this check for all 4 candidate successor nodes (left, right, up, down)

This search algorithm keeps track of the total expanded nodes, all nodes stored in memory, the time elapsed during the search, the path from the start node to the goal node, and the total cost of that path.

If there is no path from the start node to the goal node, the algorithm prints a message letting the user know and returns None for the path, -1 for the total cost, but still returns all expanded nodes and all nodes stored in memory.

### Iterative-Deepening Search

The algorithm uses the given start node, goal node, and map to traverse the map text file and find a path from the start node to the goal node by using depth-limited search traversal of the tree. It generates four successor child nodes for every current node it is traversing. These four successor child nodes represent the left, right, up, and down directions from the map. For each successor node, IDS will check if it can visit the node. The node can be visited if all the following conditions are met:
(1) it is not None
(2) the node has not been visited before, and
(3) the node's cost is not 0 (not a barrier node) we do this check for all 4 candidate successor nodes (left, right, up, down)

This search algorithm keeps track of the total expanded nodes, all nodes stored in memory, the time elapsed during the search, the path from the start node to the goal node, and the total cost of that path.

Given that iterative deepening search continues to search while no path is found, each time deepening the depth limit, if there is no path from the start node to the goal node that is possible (as is the case with two test cases provided here, explained in a later section), IDS will run until the timer times out (3 minutes), because it cannot detect that there is no possible path since each time it attempts to find the path by deepening the search.

### A-Star Search

The algorithm uses the given start node, goal node, map, and heuristic function to traverse the map text file and find a path from the start node to the goal node by computing the evaluation function each time. It generates four successor child nodes for every current node it is traversing. These four successor child nodes represent the left, right, up, and down directions from the map. For each successor node, A-Star Search will check if it can visit the node. The node can be visited if all the following conditions are met:
(1) it is not None
(2) the node has not been visited before, and
(3) the node's cost is not 0 (not a barrier node) we do this check for all 4 candidate successor nodes (left, right, up, down)

In addition, if we can traverse to a certain node, we will calculate the evaluation function as so:
`f(n) = g(n) + h(n), where:
    g(n) = total cost of the path so far, given by the cost value of the node
    h(n) = heuristic function, which defaults to the manhattan distance unless otherwise specified
`

This search algorithm keeps track of the total expanded nodes, all nodes stored in memory, the time elapsed during the search, the path from the start node to the goal node, and the total cost of that path.

If there is no path from the start node to the goal node, the algorithm prints a message letting the user know and returns None for the path, -1 for the total cost, but still returns all expanded nodes and all nodes stored in memory.

## Test Cases

There are a total of 6 test case files included, 1 (map.txt) was given and 5 were created.

### noPath1.txt

This map tests the case where the start node is surrounded by 0s, meaning that all successor nodes generated cannot be visited. Therefore, no path to the goal node can be found.

### noPath2.txt

This map tests the case where the goal node is surrounded by 0s, meaning that there is no way to reach the goal node. Therefore, no path to the goal node can be found.

### smallMap.txt

This is a small map (5x5) to test the search algorithm on a small map.

### bigMap.txt

This is a larger map (20x20) to test the search algorithm on a large map.

### superBigMap.txt

This is a larger map (50x50) to test the search algorithm on a larger map.

# Contributors and Contact Info

Thanks to the following people who have contributed to this project:

- [@andreapaola2018](https://github.com/andreapaola2018)
- [@mgmolina3](https://github.com/mgmolina3)
