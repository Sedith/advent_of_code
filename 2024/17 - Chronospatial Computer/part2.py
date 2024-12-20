def combo(a, b, c, operand):
    if operand in range(4):
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        raise AssertionError('combo of 7')


def get_output(a, instructions):
    i = 0
    b = 0
    c = 0
    output = []
    while instructions[i] != 5:
        opcode = instructions[i]
        operand = instructions[i + 1]
        match opcode:
            case 0:  # adv
                a = a // (2 ** combo(a, b, c, operand))
            case 1:  # bxl
                b = b ^ operand
            case 2:  # bst
                b = combo(a, b, c, operand) % 8
            case 3:  # jnz
                i = operand
                continue
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                return combo(a, b, c, operand) % 8
            case 6:  # bdv
                b = a // (2 ** combo(a, b, c, operand))
            case 7:  # cdv
                c = a // (2 ** combo(a, b, c, operand))
        i += 2
    return combo(a, b, c, instructions[i + 1]) % 8


def get_prev_a(a):
    return [a * 8 + i for i in range(8)]


def check_a_rec(instructions, idx, chains_of_a):
    ## terminal condition: all instructions have been processed
    if idx < 0:
        return chains_of_a

    new_chains = []
    for chain_a in chains_of_a:
        for possible_a in get_prev_a(chain_a[-1]):  # check possible previous a
            if get_output(possible_a, instructions) == instructions[idx]:  # validate against output
                new_chains.append(chain_a + [possible_a])
    return check_a_rec(instructions, idx - 1, new_chains)


def parse(data):
    instructions = [int(c) for c in data[4].split(': ')[1].split(',')]
    return instructions


def main(data):
    instructions = parse(data)
    print(instructions)

    return min([a[-1] for a in check_a_rec(instructions, len(instructions) - 1, [[0]])])


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example7.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
