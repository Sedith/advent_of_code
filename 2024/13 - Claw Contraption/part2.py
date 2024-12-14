from collections import namedtuple


XY = namedtuple('XY', ['X', 'Y'])
System = namedtuple('System', ['A', 'B', 'Prize'])


def parseline(line):
    return [int(s.split('+')[1]) for s in line.split(': ')[1].replace('=', '+').split(', ')]


def parse(data):
    machines = []
    i = 0
    while i < len(data):
        A = XY(*parseline(data[i+0]))
        B = XY(*parseline(data[i+1]))
        P = XY(*[n + 10000000000000 for n in parseline(data[i+2])])
        machines.append(System(A, B, P))
        i += 4
    return machines


def solve_system(system):
    # solve by substitution
    n1 = (system.Prize.Y - system.B.Y * system.Prize.X / system.B.X) / (system.A.Y - system.A.X * system.B.Y / system.B.X)
    n2 = (system.Prize.X - system.A.X * n1) / system.B.X
    return n1, n2


def main(data):
    machines = parse(data)
    nb_tokens = 0
    for machine in machines:
        n1, n2 = solve_system(machine)
        if abs(n1 - round(n1)) < 1e-3 and abs(n2 - round(n2)) < 1e-3:
            nb_tokens += 3 * round(n1) + round(n2)
    return nb_tokens


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
