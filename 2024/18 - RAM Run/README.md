# Advent of code 2024 - Day 18: RAM Run

https://adventofcode.com/2024/day/18

## Part 1

Simple A* implementation for solving the maze.
First, simulate the `1024` first byte fall and then find the shortest path. The heuristic is the Euclidean distance.
As for Day 16, there is no pre-building of the graph. Rather, it is locally constructed 'as we go' through the heap queue.

## Part 2

I first though about dichotomie.
But instead, it's much more efficient to:
1. construct the shortest path up to a point we know is not blocked (1024 bytes),
1. for each new falling byte, check if it is on the path,
1. if yes, replan from the path cell just before the newly blocked one and update the path,
1. stop when A* returns no solution.
