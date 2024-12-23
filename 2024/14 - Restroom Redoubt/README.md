# Advent of code 2024 - Day 14: Restroom Redoubt

## Part 1

Implemted the list of robots with their pos and vel. The `move` function simulates one second of motion (using a modulo for the teleportation). Simply run the simulation for 100 steps and iterate over robots to count robots in each quadrant.

## Part 2

Looking at a the first few samples, it appeared that the robots were most often uniformly spread accross the grid. I thus had the first idea of looking for the mean of the `(i,j)` coordinates of the robots and check for clear deviation from `(0.5, 0.5)`. It clearly reduced the amount of samples I had to look for and I found the Easter Egg manually.
However, even then, there were a significant amount of outliers (many configurations with vertical bars accross the tree location). I realized that I was actually looking for a variance decrease rather than a mean shift (even the more so because the tree could a priori be centered on the grid).
Turns out that indeed the Easter Egg grid has a significantly smaller variance than the baseline.
