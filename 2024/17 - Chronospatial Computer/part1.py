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


def run_program(a, b, c, instructions):
    i = 0
    output = []
    while i < len(instructions):
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
                if a:
                    i = operand
                    continue
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                output.append(combo(a, b, c, operand) % 8)
            case 6:  # bdv
                b = a // (2 ** combo(a, b, c, operand))
            case 7:  # cdv
                c = a // (2 ** combo(a, b, c, operand))
        i += 2
    return output


def parse(data):
    regA = int(data[0].split(': ')[1])
    regB = int(data[1].split(': ')[1])
    regC = int(data[2].split(': ')[1])
    instructions = [int(c) for c in data[4].split(': ')[1].split(',')]
    return regA, regB, regC, instructions


def main(data):
    output = run_program(*parse(data))
    return ''.join([f'{str(o)},' for o in output])[:-1]


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
