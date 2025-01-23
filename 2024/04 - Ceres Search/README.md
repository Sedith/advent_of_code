# Advent of code 2024 - Day 04: Ceres Search

https://adventofcode.com/2024/day/4

## Part 1

I first implemented an "augmented" tuple class describing positions, and overloading the `+` to conveniently work with the `Dir` enum (North, North-East...).
The class method handles edge-cases for not being outside the grid.
The grid itself is a list of strings, and the chars are accessed by `grid[i][j]` for each tuple `(i, j)`. Other convenience/debugging functions for displaying can be added to the grid class.
I thus discovered that classes inheriting tuples must declare the `__new__` class function, e.g. as
```
def __new__(cls, i, j):
       return super(Pos, cls).__new__(cls, (i, j))
```
in addition to the `__init__` which declares additional class members etc. Both function are called with the sample args when the class constructor is called.

Later, I modified the code on to use complex numbers for grid-based puzzles (first time doing so). It's freakin' efficient (and it'll be even more when rotations will be involved I guess).
It's also more legible than I thought it'd be.

The grid is now described as a `{pos: char}` dict where pos is the complex description of the position in the grid.
Its actually a `defaultdict`, such that getting a complex outside the grid returns `''`. Simplifies most checks.
I also just discovered the [merge operator](https://peps.python.org/pep-0584/) `|` for dicts.

The algorithm is mostly a naive for pattern matching in the grid.
For each character, if it hooks (matches the first character of the target str), the `check_neighbors_rec` function is called to recursively check in each of the 8 directions if all characters match the target str.

It could probably be marginally optimized by checking the match each time any letter of 'XMAS' is encountered, and using a memory of some sort to avoid rechecking previously seen cells.
This would likely help scaling up to larger grids.

## Part 2

Again, using complex numbers.
The check is very similar, but this time hooks on the middle characters instead of the first one, and check that both diagonals contains the side characters (in whatever order).
