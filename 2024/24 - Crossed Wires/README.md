# Advent of code 2024 - Day 24: Crossed Wires

## Part 1

The wire values are stored in a dict, which is augmented each time a logic gate is used.
The gates are stored as a queue of instructions: if the first one has two valid inputs, the gate is processed, else the instruction is pushed back and the end of the queue.

There is maybe a smarter way, eg doing a gate order preprocessing, but this runs sub-ms already.

## Part 2
