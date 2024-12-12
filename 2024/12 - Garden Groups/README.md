# Advent of code 2024 - Day 12: Garden Groups

## Part 1

Grid cell values are tuples `(bool, Pos)`, where the bool tells if the cell was already assigned to the region.
The grid is parsed with two nested loops:
* A row-major scan over the grid until a "non-regionned" cell is found.
* An iterative exploration of the region. The 4-neighbors for each new cell are checked for their crop type. Matching cells are added to the current list to explore.
The area (nb of cells) and perimeter (sum of `4 - nb of matching neighbors`) are incrementally computed.

## Part 2
