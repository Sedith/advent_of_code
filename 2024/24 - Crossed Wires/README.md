# Advent of code 2024 - Day 24: Crossed Wires

## Part 1

The wire values are stored in a dict, which is augmented each time a logic gate is used.
The gates are stored as a queue of instructions: if the first one has two valid inputs, the gate is processed, else the instruction is pushed back and the end of the queue.

There is maybe a smarter way, eg doing a gate order preprocessing, but this runs sub-ms already.

## Part 2

Tough one. I tried to make an analyzer that wouldn't rely on the specific logic of the adder and how it should be structured (simply knowing the desired output for each input), but no luck. I believe that it's feasible but extremely hard (maybe through some formal SAT optimization).

The only somehow interesting thing I managed is retrieving the list of faulty output bits by summing `0` to `2**k` and checking outputs that doesn't match.
It yields 4 faulty bits, but tracing backwards doesn't narrow the list of candidate swaps so much.

I went checking the subreddit, it appears that most people went through manual checks of inconsistencies (via visual plotting of the graph) or automated checks for inconsistencies based on some ad-hoc rules describing the logic structure of the adder (a [ripple-carry adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder)).
A handful of people (I counted 3 on the subreddit) used genetic algorithms to generate random swaps ("mutations") and correct the genome based on some penalty computed on some samples. That's really the only fun approach I came accross.

Anyway, here are the rule that the circuit should follow (taken from reddit):
* no output bit come directly from input wires except the first (which is from a XOR between the first bit of each input number)
* XOR gates that come from OR and XOR gates are output bits
* output bits come from XOR gates, except the last bit
* AND gate cannot take XOR gates as input (except if it takes as input the wire `x00`)
* XOR gate cannot take OR gates as input (except if it takes as input the wire `x00`)

Implemented as is.
