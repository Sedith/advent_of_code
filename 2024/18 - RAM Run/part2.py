from enum import Enum
from collections import defaultdict
from heapq import heappop, heappush


class Dir(Enum):
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
    def __new__(cls, i, j, grid_size):
        return super(Pos, cls).__new__(cls, (i, j))

    def __init__(self, i, j, grid_size):
        self.grid_size = grid_size

    def __add__(self, d):
        di, dj = d.move()
        i = self[0] + di
        j = self[1] + dj
        if i in [-1, self.grid_size[0]] or j in [-1, self.grid_size[1]]:
            return None
        return Pos(i, j, self.grid_size)


def display(data, grid_size, path):
    grid = [['.' for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for l in data:
        j, i = map(int, l.split(','))
        grid[i][j] = '#'
    for p in path:
        grid[p[0]][p[1]] = '\033[31mx\033[0m'
    print(''.join([''.join([c for c in l]) + '\n' for l in grid])[:-1])


def astar(grid, start, end):
    def h(p):
        return (p[0] - end[0]) ** 2 + (p[1] - end[1]) ** 2

    distances = defaultdict(lambda: float('inf'))
    queue = [(0, 0, start, [start])]
    while queue:
        hval, dist, pos, path = heappop(queue)
        if dist > distances[pos]:
            continue
        else:
            distances[pos] = dist

        if pos == end:
            break

        for npos in [pos + d for d in [Dir.N, Dir.E, Dir.S, Dir.W]]:
            if npos and npos != pos and not grid[npos[0]][npos[1]]:
                heappush(queue, (dist + 1 + h(npos), dist + 1, npos, path + [npos]))

    return path if distances[end] != float('inf') else []


def main(data, start_bytes, grid_size):
    grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for l in data[:start_bytes]:
        j, i = map(int, l.split(','))
        grid[i][j] = 1

    start = Pos(0, 0, grid_size)
    end = Pos(grid_size[0] - 1, grid_size[1] - 1, grid_size)
    path = astar(grid, start, end)

    for k, l in enumerate(data[start_bytes:]):
        j, i = map(int, l.split(','))
        grid[i][j] = 1
        p = Pos(i, j, grid_size)
        try:
            idx = path.index(p)
            start = path[idx - 1]  # assumes no byte fall on (0,0)
            new_path = astar(grid, start, end)
            if new_path:
                path = path[: idx - 1] + new_path
            else:
                break
        except ValueError:
            pass

    return f'{j},{i}'


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    grid_size = 70 if file == 'input.txt' else 6
    start_bytes = 1024 if file == 'input.txt' else 12
    result = main(data, start_bytes, (grid_size + 1, grid_size + 1))
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
