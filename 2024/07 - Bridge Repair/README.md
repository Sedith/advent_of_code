# Advent of code 2024 - Day 07: Bridge Repair

https://adventofcode.com/2024/day/7

## Part 1

Recursion on the list of possible outputs.
Termination: when the list of numbers to process is empty, return the full list
Recursion: for each possible value in the list, create 2 branches for sum and mult.

## Part 2

Mostly similar, with 3 operations.
Computing the concatenation is faster using `len(str(b))` than using `int(log(b, 10) + 1)` (about 13%)
The recursion branches are terminated if the curretn value is already bigger than the target result. Surprisingly, doing the same for part 1 slightly slows down the computation. I assume it's mostly the concatenation that triggers this condition.
Didn't manage to reduce below ~2.5s.
