from enum import Enum


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def next(self):
        return Dir((self.value + 1) % 4)

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


class Grid:
    def __init__(self, data):
        self.grid = [[c for c in l] for l in data]
        self.size = (len(data), len(data[0]))
        self.nb_X = 0
        self.marker_X = '\033[31mX\033[0m'

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def mark(self, pos):
        if self.get(pos) != self.marker_X:
            self.nb_X += 1
            self.grid[pos[0]][pos[1]] = self.marker_X

    def __str__(self):
        return ''.join(''.join(line) + '\n' for line in self.grid)[:-1]


def main(data):
    grid = Grid(data)

    ## find start
    for i, l in enumerate(data):
        try:
            j = l.index('^')
            break
        except ValueError:
            pass

    dir = Dir(0)
    guard = Pos(i, j, grid.size)

    ## increment guard path
    while guard is not None:
        grid.mark(guard)
        while (next_pos := guard + dir) is not None and grid.get(next_pos) == '#':
            dir = dir.next()
        guard = next_pos

    return grid.nb_X


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
