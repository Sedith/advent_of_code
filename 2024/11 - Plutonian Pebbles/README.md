# Advent of code 2024 - Day 11: Plutonian Pebbles

## Part 1

Straigthforward implementation. Tested both with recursion and for-loop.

## Part 2

Essentially building upon the recursion with memoization.
It's implemented naively, that is, the memoization dict looks like:
`{ stone number : { depth at which it is encountered : nb of leaves at depth == nb_iter} }`
This is obvious suboptimal. Ideallly, one would store the list of leaves for each given depth below the current leaf, eg
`{ stone number : { depth below current : list of leaves } }`.
The main difference is that if a given stone is encountered at depth `N` and was previously encountered at depth `M > N`, it is not needed to explore the whole tree again but simply expand from the deepest known list of leaves.
Not implemented for now because recursions fuck up my brain.
