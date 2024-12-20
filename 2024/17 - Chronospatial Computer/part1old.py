from dataclasses import dataclass


@dataclass
class Ram:
    regA: int
    regB: int
    regC: int
    cursor: int
    output: list

    def __str__(self):
        return f'A:{self.regA}, B:{self.regB}, C:{self.regC}, cursor:{self.cursor}'


def combo(ram, operand):
    if operand in range(4):
        return operand
    elif operand == 4:
        return ram.regA
    elif operand == 5:
        return ram.regB
    elif operand == 6:
        return ram.regC
    else:
        raise AssertionError('combo of 7')


def adv(ram, operand):
    ram.regA = ram.regA // (2 ** combo(ram, operand))
    ram.cursor += 2


def bxl(ram, operand):
    ram.regB = ram.regB ^ operand
    ram.cursor += 2


def bst(ram, operand):
    ram.regB = combo(ram, operand) % 8
    ram.cursor += 2


def jnz(ram, operand):
    if ram.regA:
        ram.cursor = operand
    else:
        ram.cursor += 2


def bxc(ram, operand):
    ram.regB = ram.regB ^ ram.regC
    ram.cursor += 2


def out(ram, operand):
    ram.output.append(combo(ram, operand) % 8)
    ram.cursor += 2


def bdv(ram, operand):
    ram.regB = ram.regA // (2 ** combo(ram, operand))
    ram.cursor += 2


def cdv(ram, operand):
    ram.regC = ram.regA // (2 ** combo(ram, operand))
    ram.cursor += 2


def parse(data):
    regA = int(data[0].split(': ')[1])
    regB = int(data[1].split(': ')[1])
    regC = int(data[2].split(': ')[1])
    instructions = [int(c) for c in data[4].split(': ')[1].split(',')]
    return regA, regB, regC, instructions


def main(data):
    a, regB, regC, instructions = parse(data)
    print(instructions)

    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
    ram = Ram(a, regB, regC, 0, [])

    while ram.cursor < len(instructions):
        opcode, operand = instructions[ram.cursor : ram.cursor + 2]
        ops[opcode](ram, operand)

    return ''.join([f'{str(output)},' for output in ram.output])[:-1]


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
