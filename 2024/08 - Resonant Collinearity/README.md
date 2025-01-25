# Advent of code 2024 - Day 08: Resonant Collinearity

https://adventofcode.com/2024/day/8

## Part 1

The antennas are stored in a dict {antenna frequency: list of tuple of coordinates}.
From there, the antinode locations are given by: for two points A and B, the nodes are A + (A - B) and B + (B - A).

## Part 2

Weird wording, the "regardless of distance" confused me wrt the examples below. Part 1 could also be ambiguous but it explicitely says "one on either side".
I think that the input is made such that no antinode can be on non-integer multiples of the distance between antennas (ie, those fall in-between grid cells).

Still, change from part one by adding all `* k` antinodes.
The `antinodes` function calls a recursive subroutine that checks on both sides of the antenna pair (`s = 1` for `p1` and `s = -1` for `p2`).
Doing side by side instead of both side at the same time avoids redundant computations.
