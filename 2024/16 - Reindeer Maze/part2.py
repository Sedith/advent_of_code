from collections import defaultdict
from enum import IntEnum
from heapq import heappop, heappush


class Dir(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3

    def cw(self):
        return Dir((self.value + 1) % 4)

    def ccw(self):
        return Dir((self.value - 1) % 4)

    def move(self):
        return ((-1, 0), (0, 1), (1, 0), (0, -1))[self.value]

    def __str__(self):
        return ('^', '>', 'v', '<')[self.value]


class Pos(tuple):
    def __new__(cls, i, j):
        return super(Pos, cls).__new__(cls, (i, j))

    def __add__(self, d):
        di, dj = d.move()
        return Pos(self[0] + di, self[1] + dj)


def display(data, seen):
    def color(char):
        if char in ['S', 'E']:
            return f'\033[32m{char}\033[0m'
        elif char in ['x']:
            return f'\033[31m{char}\033[0m'
        elif char == '.':
            return ' '
        else:
            return char

    grid = [[c for c in l] for l in data]
    for p in seen:
        grid[p[0]][p[1]] = 'x'
    print(''.join([''.join([color(c) for c in l]) + '\n' for l in grid]))


def dijkstra(grid, start, end):
    distances = defaultdict(lambda: float('inf'))
    queue = [(0, start, Dir.E, [start])]
    seen = []
    best = float('inf')
    while queue:
        dist, pos, dir, path = heappop(queue)
        if dist > distances[pos, dir] or dist > best:
            continue
        else:
            distances[pos, dir] = dist

        if pos == end:
            seen += path
            best = dist

        for ndir, add_dist in [(dir, 1), (dir.cw(), 1001), (dir.ccw(), 1001)]:
            np = pos + ndir
            if grid[np[0]][np[1]] != '#':
                heappush(queue, (dist + add_dist, np, ndir, path + [np]))

    seen = set(seen)
    return len(seen), seen


def main(data):
    grid = [[c for c in l] for l in data]
    (start,) = (Pos(i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == 'S')
    (end,) = (Pos(i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == 'E')

    score, path = dijkstra(grid, start, end)
    display(grid, path)
    return score


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
