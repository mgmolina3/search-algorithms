# search-algorithms

created by Montserrat Molina & Andrea Ulloa

## Getting Started

To clone this repo, run `git clone https://github.com/mgmolina3/search-algorithms.git`

## Running our Project

In the project directory, you can run:

### For Windows: `python3 search.py <name of text file>.txt bfs`

### For Mac: `./search <name of text file>.txt bfs`

## Features

Search a given map text file with a specified search algorithm. Currently, this project supports breadth-first search algorithm only.

### Breadth-First Search

The algorithm uses the given start node, goal node, and map to traverse the map text file and find a path from the start node to the goal node. It generates four successor child nodes for every current node it is traversing. These four successor child nodes represent the left, right, up, and down directions from the map. For each successor node, bfs will check if it can visit the node. The node can be visited if all the following conditions are met:
(1) it is not None
(2) the node has not been visited before, and
(3) the node's cost is not 0 (not a barrier node) we do this check for all 4 candidate successor nodes (left, right, up, down)

This search algorithm keeps track of the total depth, total expanded nodes, all nodes stored in memory, the time elapsed during the search, the path from the start node to the goal node, and the total cost of that path.

If there is no path from the start node to the goal node, the algorithm prints a message letting the user know and returns None for the path, -1 for the total cost, but still returns all visited nodes up to that point, all expanded nodes, and all nodes stored in memory.

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
