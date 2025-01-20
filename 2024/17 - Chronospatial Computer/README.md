# Advent of code 2024 - Day 17: Chronospatial Computer

https://adventofcode.com/2024/day/17

## Part 1

The `run_program` function processes the instructions and modifies the register until it terminates. It spits out the list of output values.

## Part 2

Fun one!
After manually checking the program, it turns out that it has the following properties:
* the last instruction jumps back to the first one (except if `a == 0` in which case it terminates)
* there is one output per cycle of instructions
* values for registers B and C are overwritten at each cycle, such that the output of each cycle is strictly a function of register A
* A is divided by 8 at each cycle

Thus, given that the last value of a is known, one can:
* compute the 8 possible values for `a` at the start of the cycle
* compute the 8 printed output
* for each output matching the target (self replication of the code, starting from the end), redo the same for the previous input until the first digit of the program or a dead-end.

Implemented as a recursive function taking as input all the lists of chains of valid `a` and the index of the program digit to output.
