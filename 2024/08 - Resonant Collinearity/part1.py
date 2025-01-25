from collections import defaultdict


def antinodes(p1, p2):
    di = p1[0] - p2[0]
    dj = p1[1] - p2[1]
    return (p1[0] + di, p1[1] + dj), (p2[0] - di, p2[1] - dj)


def main(data):
    size = (len(data), len(data[0]))
    in_grid = lambda p: 0 <= p[0] < size[0] and 0 <= p[1] < size[1]

    ## find list of antennas
    antennas = defaultdict(list)
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c != '.':
                antennas[c].append((i, j))

    ## compute antinodes
    return len(set(n for key in antennas for ant1 in antennas[key] for ant2 in antennas[key] if ant1 != ant2 for n in antinodes(ant1, ant2) if in_grid(n)))


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
