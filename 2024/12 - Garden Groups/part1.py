from enum import Enum


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

    def next(self):
        if self[1] == self.grid_size[1] - 1:
            if self[0] == self.grid_size[0] - 1:
                return None
            else:
                return Pos(self[0] + 1, 0, self.grid_size)
        else:
            return Pos(self[0], self[1] + 1, self.grid_size)


class Grid:
    def __init__(self, data):
        self.grid = [[(False, c) for c in l] for l in data]
        self.size = (len(data), len(data[0]))
        self.cursor = Pos(0, 0, self.size)


    def get(self, idx):
        return self.grid[idx[0]][idx[1]]


    def set_regionned(self, idx):
        self.grid[idx[0]][idx[1]] = (True, self.grid[idx[0]][idx[1]][1])

    def next(self):
        if self.cursor is None:
            return None
        else:
            next = self.get(self.cursor), self.cursor
            self.cursor = self.cursor.next()
            return next


class Region:
    def __init__(self, type):
        self.type = type
        self.area = 0
        self.peri = 0


def main(data):
    grid = Grid(data)
    regions = []
    while next := grid.next():  ## scan over the grid
        (is_regionned, crop_type), pos = next
        if not is_regionned:  ## skip if already regionned
            region = Region(crop_type)
            to_be_regionned = [pos]
            while to_be_regionned:  ## iterative exploration of the current region
                pos = to_be_regionned.pop(0)
                if not grid.get(pos)[0]:  ## skip if already regionned
                    grid.set_regionned(pos)
                    neighbors = [pos + d for d in [Dir.N, Dir.E, Dir.S, Dir.W]]
                    to_be_regionned += (valid_neighbors := [pos for pos in neighbors if pos and grid.get(pos)[1] == crop_type])
                    region.area += 1
                    region.peri += 4 - len(valid_neighbors)
            regions.append(region)

    # [print(f'region of {r.type}, area {r.area}, perimeter {r.peri}, price {r.area * r.peri}') for r in regions]
    return sum([r.area * r.peri for r in regions])


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example3.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
