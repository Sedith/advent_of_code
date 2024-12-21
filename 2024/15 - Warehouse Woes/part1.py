from enum import Enum


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

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
        self.chars = {'@': '\033[93m@\033[0m', '#': '\033[31m#\033[0m', 'O': '\033[32mO\033[0m', '.': ' '}
        grid_lines = []
        while l := data.pop(0):
            if (j := l.find('@')) != -1:
                robot = len(grid_lines), j
            grid_lines.append(l)
        self.grid = [[c for c in l] for l in grid_lines]
        self.robot = Pos(robot[0], robot[1], (len(self.grid), len(self.grid[0])))

        char_to_dir = {'^': Dir.N, '>': Dir.E, 'v': Dir.S, '<': Dir.W}
        self.moves = [char_to_dir[c] for l in data for c in l]

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def set(self, pos, v):
        self.grid[pos[0]][pos[1]] = v

    def move_rec(self, pos, dir):
        next_pos = pos + dir
        c = self.get(next_pos)
        if c == '.':
            self.set(next_pos, cc := self.get(pos))
            self.set(pos, '.')
            if cc == '@':
                self.robot = next_pos
            return True
        elif c == '#':
            return False
        elif c == 'O':
            if self.move_rec(next_pos, dir):
                return self.move_rec(pos, dir)

    def do_all_moves(self):
        for dir in self.moves:
            self.move_rec(self.robot, dir)

    def get_all_gps(self):
        sum_gps = 0
        for i, l in enumerate(self.grid):
            for j, c in enumerate(l):
                if c == 'O':
                    sum_gps += 100 * i + j
        return sum_gps

    def __str__(self):
        return ''.join([''.join([self.chars[c] for c in l]) + '\n' for l in self.grid])[:-1]


def main(data):
    grid = Grid(data)
    grid.do_all_moves()
    # print(grid)
    return grid.get_all_gps()


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
