# Advent of code 2024 - Day 05: Print Queue

https://adventofcode.com/2024/day/5

## Part 1

The rules `a|b` are stored as `dict[a] = [b]`, assigning a list of latters to each former in the pairs.
The rule dict is a `defaultdict`, which assigns a default value (according to the considered type) to new keys, to avoid try/catching KeyErrors.

For checking each update: if any `b` has a `a` in the same update but placed afterward, it invalid.
The `manual_check` function performs this check and return the middle element if need be.

After doing (and improving) part 2, I realized that its effectively faster to sort the update based on the custom comparison function, and check if the sorted output differs from the input. This is implemented in `sort_based_check`, which runs 3 to 4 times faster.

## Part 2

Similar to part 1 in spirit but instead of checking the validity, we fix the ordering in each update. I first made a custom function operating on a copy of the update, but instead its more efficient and elegant to sort the update with a custom comparison function.
For two elements `a` and `b` of the update, `a` is first if it is originally placed before, or if its after and is in a rule `a|b` forcing it to be before. Otherwise, b is first.
This is implemented as the lambda `lambda a,b: -1 if a in update[: update.index(b)] else (1 if b in rules[a] else -1)`.
Then, the sort is achieved with `cmp_to_key` from `functools`, which I just (re?)discovered.
