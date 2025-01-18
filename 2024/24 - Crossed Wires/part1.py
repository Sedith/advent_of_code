import operator
from collections import deque


def parse(data):
    iter_data = iter(data)
    wires = {}
    while l := next(iter_data):
        key, val = l.split(': ')
        wires[key] = bool(int(val))

    instructions = []
    while l := next(iter_data, ''):
        in1, op, in2, _, out = l.split()
        instructions.append((in1, in2, op, out))

    return wires, instructions


def zs_to_int(wires):
    zs = {int(key[1:]): wires[key] for key in wires if key.startswith('z')}
    return int(''.join([str(int(zs[key])) for key in sorted(zs, reverse=True)]), base=2)


def main(data):
    wires, instructions = parse(data)

    ops = {'AND': operator.mul, 'OR': operator.add, 'XOR': operator.xor}

    instructions = deque(instructions, maxlen=len(instructions))
    while instructions:
        in1, in2, op, out = instructions.popleft()
        if in1 in wires and in2 in wires:
            wires[out] = bool(ops[op](wires[in1], wires[in2]))
        else:
            instructions.append((in1, in2, op, out))

    return zs_to_int(wires)


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
