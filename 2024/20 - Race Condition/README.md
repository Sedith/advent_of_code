# Advent of code 2024 - Day 20: Race Condition

## Part 1

I first implemented some successive astar starting from spots 'on the other sides of a wall', until I understood that it was not a maze but a single track.
Instead, the main path can be computed as a basic list of successive positions by looking at neighbooring non-`#` cells.
Then, iterate over the path with two nested loops and compute the one-to-one L1 distance. If the distance is 2 and the gain of time is enough, increment the counter.
Minor optimization: since the gain must be at least 100, and the cheat distance is at least 2, it is useless to consider the next 101 path positions, because any cheat that lands in this range doesn't save enough picosecs.

## Part 2

Same but with parametric cheat length.
