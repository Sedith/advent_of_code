# Advent of code 2024 - Day 22: Monkey Market

https://adventofcode.com/2024/day/22

## Part 1

Direct implementation of the secret number generation recipe.

## Part 2

As the 2000 secret numbers are iterated over, a dict is populated whose keys and vals are respectively the last four changes sequences and the sum of bananas the sequence would get from each monkey. A memory of "used" sequences is also built for each monkey such that only the first instance of each sequence is accounted for.
As optimizations:
* using a `dequeu` with specified `maxlen = 4` makes it nicer and faster than aggregating a list and using only the last four elements,
* using a `set` for `used_seqs` instead of a list speeds up the checks more than 10x.

I don't see much more room for speed up without changing the method. Using numpy would probably help (doing vectorized operations instead of using the big for loop)?
