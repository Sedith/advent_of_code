# Advent of code 2024 - Day 19: Linen Layout

## Part 1

Recursive check of the patterns fron left to right.
For each token that matches the start of the pattern, recursively check new patterns that fit the remainder of the pattern.
I first implemtented it as a for loop dequeueing a candidate list of remainders, but the recursive version is order of one order of magnitude faster.

## Part 2