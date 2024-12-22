# Advent of code 2024 - Day 16: Reindeer Maze

## Part 1

Graph implementation of the maze and Dijkstra algorithm.
The tricky part is the graph building: each node is a position and a direction. For each of the 4 directions, 2 neighbors can be reached by rotating, and 0 or 1 can be reached by moving forward (depending on if there is a wall).
Since the end position can be reach from either two directions, the node which leads to the shortest path is selected.
I tried implementing an A* instead, but the heuristic function is a bit fucked up and is not a simple L1 distance, but must include the minimum amount of rotations to reach the goal node. In the end I didn't manage to get it to work much faster than Dijkstra.

I wonder if it'd be easy to build the graph as you explore the path.

## Part 2
