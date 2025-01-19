# Advent of code 2024 - Day 25: Code Chronicle

## Part 1

The algorithm is trivial: count free space for locks and occupied space for keys (column-wise) and check that all columns fit.
For the implementation, I to be fancy. I made a generator spitting chunks of lines seperated by empty lines in the data files. It gets transposed by this magic one-liner from day 1.
The `parse` function creates a list of tuples `(first char, list of free/occupied spaces)`, which gets split in two sublists `locks` and `keys` according to the value of the first char (`'#'` or `'.'`).
