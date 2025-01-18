# Advent of code 2024 - Day 23: LAN Party

## Part 1

After building the connection dictionnary, I realized that this was nothing but a [3-clique search problem](https://en.wikipedia.org/wiki/Clique_problem).
According to [the relevant section of the wikipedia article](https://en.wikipedia.org/wiki/Clique_problem#Cliques_of_fixed_size), doing an exhaustive search for a `k`-clique is solvable in polynomial time if `k` is fixed (3 here).

I've implemented it looking for all pairs of neighbors if any neighbor of the second is also neighbor of the first.
The 3-cliques are stored in a set of ordered tuples to avoid duplicates.

## Part 2

We now want to find the largest clique in the graph. This is a NP-hard problem.
There exist a bunch of algorithms for doing it. The most spread seems to be [Bron–Kerbosch algorithm](https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm).

I implemented the pseudo-code from wikipedia:
```
algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each vertex v in P do
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P \ {v}
        X := X ⋃ {v}

```
using sets (which provides `union` and `intersection` functions).
A trick is that we need to iterate over `p` which gets modified. Thus we iterate over a copy, created using `list(p)` instead of importing the copy module. 
