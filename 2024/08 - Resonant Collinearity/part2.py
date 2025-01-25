from collections import defaultdict


def in_grid(p):
    global size
    return 0 <= p.imag < size[0] and 0 <= p.real < size[1]


def antinodes(p1, p2):
    d = p1 - p2
    return [p1, p2] + antinodes_rec(p1, d, 1, 1) + antinodes_rec(p2, d, -1, -1)


def antinodes_rec(p, d, k, s):
    if in_grid(n := p + s * k * d):
        return [n] + antinodes_rec(p, d, k + s, s)
    else:
        return []


def main(data):
    global size
    size = (len(data), len(data[0]))

    ## find list of antennas
    antennas = defaultdict(list)
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c != '.':
                antennas[c].append(j + i * 1j)

    ## compute antinodes
    return len(set(n for key in antennas for ant1 in antennas[key] for ant2 in antennas[key] if ant1 != ant2 for n in antinodes(ant1, ant2)))


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
