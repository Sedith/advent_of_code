# Advent of code 2024 - Day 12: Garden Groups

## Part 1

Grid cell values are tuples `(bool, Pos)`, where the bool tells if the cell was already assigned to the region.
The grid is parsed with two nested loops:
* A row-major scan over the grid until a "non-regionned" cell is found.
* An iterative exploration of the region. The 4-neighbors for each new cell are checked for their crop type. Matching cells are added to the current list to explore.
The area (nb of cells) and perimeter (sum of `4 - nb of matching neighbors`) are incrementally computed.

Could be optimized by keeping track the direction from which the new cells are discovered, in order to recude the number of neighbor checks.

## Part 2

The main thing to note is that the number of sides of the polytopes is equal to its number of corners. Therefore, it is only about assessing cells which are corners.
There are two corner types only:
1. "outward" corners, where two neighbors 90° appart are in a different region (or outside of the grid), eg the central cell in
```
BBB
AAB
AAB
```
1. "inward" corners where two neighbors 90° appart are in the same region (qnd not ouside the grid) but the diagonal neighbor inbetween is in a different region, eg the central cell in
```
AAA
AAA
AAB
```

The implementation is similar to part one but now with a 8-neighbor `Enum`.
The added function `is_corner(p, grid)` checks if `p` is a corner according to any of the two criteria.
Note that the function returns the "multiplicity" of the corner, since a single cell can be a corner for several sides. It is notably the case for an area made of a single cell, which has a "multiplicity" of 4.
