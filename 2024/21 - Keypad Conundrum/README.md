# Advent of code 2024 - Day 21: Keypad Conundrum

## Part 1

Each key of each pad is allocated its coordinates starting from the topleft. Then, the path to reach the target key from the current one is obtained by checking the difference of coordinates.
Avoiding the empty key defines if vertical or horizontal motions have to happen first.
However, this does not ensure that the key strokes at higher degrees (ie, "one keypad above") are optimal.
This is counter intuitive to me since the same number of key press is required. But this effect appears at higher degrees.
I've observed this from the example `379A`. The sequences can start with either
* `^^<<A` that becomes `<AAv<AA>>^A`, or
* `<<^^A` that becomes `v<<AA>^AA>A`.

Because the `<` key is further away from `A`, it requires more steps. It is therefore critical that they are pressed consecutively, as much as possible.
Thus, because going to the `<` key from `A` requires two `<`, we want these two presses to happen consecutively, so we don't want to 'stop' in between to press something else.
Hence `<<^^A` is better than `^^<<A` because its direct translation has its `<` more condensed.

In general, `<` should be prioritized, then `v` (same reasoning: because it is 2 keystokes away from `A` so it should happen first), then `>` or `^`.

## Part 2
