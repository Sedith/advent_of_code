def parse(data):
    last_bit = 0
    instructions = []
    for l in [d for d in data if '->' in d]:
        in1, op, in2, _, out = l.split()
        instructions.append((in1, in2, op, out))
        if out[0] == 'z' and (w := int(out[1:])) > last_bit:
            last_bit = w

    return last_bit, instructions


def check_inputs(wire, gate, instructions):
    return any(wire in [in1, in2] and op == gate for in1, in2, op, out in instructions)


def main(data):
    last_bit, instructions = parse(data)

    swapped = [
        out for in1, in2, op, out in instructions if
        op == "XOR" and all(wire[0] not in 'xyz' for wire in (in1, in2, out)) or
        op == "XOR" and out[0] != 'z' and not check_inputs(out, 'OR', instructions) and not check_inputs(out, 'XOR', instructions) or
        op != 'XOR' and out[0] == 'z' and out != f'z{last_bit:02d}' or
        op == 'AND' and 'x00' not in (in1, in2) and check_inputs(out, 'XOR', instructions) or
        op == 'XOR' and 'x00' not in (in1, in2) and check_inputs(out, 'OR', instructions)
    ]

    return ''.join([f'{gate},' for gate in sorted(swapped)])[:-1]


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
