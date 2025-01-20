# Advent of code 2024 - Day 16: Reindeer Maze

https://adventofcode.com/2024/day/16

## Part 0

Mockup test with graph implementation of the maze and both Dijkstra and A* algorithms. It disregards the cost of turning 90°, and simply finds the shortest path in the maze with uniform edge length.
A refresher on those algorithms :)

## Part 1

The tricky part is the graph building: each node is a position and a direction. For each of the 4 directions, 2 neighbors can be reached by rotating, and 0 or 1 can be reached by moving forward (depending on if there is a wall).
I ended up not constructing the graph explicitly, but rather exploring the graph within the dijkstra algorithm. Because the heap queue is explored based on shortest distance, it ensures that the first time we reach the end is the shortest path.

Note: because the heap queue does comparisons for pushing new elements, and the same node can be inserted with the same distance but different directions, the Dir class needs to be comparable. Either define the `__lt__` operator, or use an `IntEnum` instead.

## Part 2

Very similar, but we don't finish on the first time we reach the end.
Each path with the shortest length is added to a set of seen positions. Path explorations are aborted as soon as they get longer than the minimum length.
