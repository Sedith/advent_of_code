# Advent of code 2024 - Day 06: Guard Gallivant

https://adventofcode.com/2024/day/6

## Part 1

~Simple impletation based on the grid/idx/dir implemented for 2024/04.~
Grid positions implemented as complex numbers.
Increment the guard position until they leave the map.

## Part 2

The concept is to explore a branch by adding an obstacle in front of the guard at each step, and check if this leads to a loop.
There are several edge cases:
* check that the obstacle can be placed
    * we cannot place the obstacle on the current guard position
    * we cannot place the obstacle on the previously walked path of the guard (imply the previous)
* don't account for obstacles several times in the same location
* consider collisions with the new obstacle as well (duh)

Implementation of path as a dict whose key is the position and value is the directions the cell was crossed with.
The exploration path is a separate path dict.

Notably, during the exploration, its only necessary to check for loops when hitting an obstacle.

## Part 2 v2

Found an efficient implementation of the proper graph problem, see https://github.com/APMorto/aoc2024/blob/master/day_06_guard_gallivant/guard.py
