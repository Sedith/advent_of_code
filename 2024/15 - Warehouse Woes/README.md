# Advent of code 2024 - Day 15: Warehouse Woes

## Part 1

The grid is implemented as a list of list of chars, and the robot position is kept track of. The main function is the `move_rec(pos, dir)` method, moving the object at position `pos` in direction `dir`. If object is movable, it does it. If it would move into a box, it recursively tries to move the box in the next cell before coming back to the current cell.

## Part 2

The direct extension of the implementation from part 1 breaks when pushing a box up or down. I didn't manage to get the recursive implementation to work in this setup.
I ended up implenting an ugly `move` function that:
1. check if the robot and all box in the way can move or are blocked
1. if movable, stored the value to insert for each moved cell (look in the direction opposite to movement, and check if it is also moved or not to determine new char)
1. move (ie, replace all chars) the boxes
1. move the robot

Very non-optimized, but works.
