from enum import Enum


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def inv(self):
        return Dir((self.value + 2) % 4)

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


xss = [[1, 1]]


class Grid:
    def __init__(self, data):
        self.chars = {
            '@': '\033[93m@\033[0m',
            '#': '\033[31m#\033[0m',
            '[': '\033[32m[\033[0m',
            ']': '\033[32m]\033[0m',
            '.': ' ',
        }
        expand_char = {'@': '@.', '#': '##', 'O': '[]', '.': '..'}
        grid_lines = []
        while l := data.pop(0):
            if (j := l.find('@')) != -1:
                robot = len(grid_lines), 2 * j
            grid_lines.append(l)
        self.grid = [[c for cc in l for c in expand_char[cc]] for l in grid_lines]
        self.robot = Pos(robot[0], robot[1])

        char_to_dir = {'^': Dir.N, '>': Dir.E, 'v': Dir.S, '<': Dir.W}
        self.moves = [char_to_dir[c] for l in data for c in l]

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def set(self, pos, v):
        self.grid[pos[0]][pos[1]] = v

    def move(self, pos, dir):
        to_check = set([pos + dir])
        checked = set([pos])
        move = True
        while to_check:
            p = to_check.pop()
            if p in checked:
                continue
            checked.add(p)
            c = self.get(p)
            if c == '#':
                move = False
                break
            elif c in ['[', ']']:
                np = p + dir
                to_check.add(np)
                to_check.add(np + (Dir.E if c == '[' else Dir.W))
                checked.add(p + (Dir.E if c == '[' else Dir.W))

        if move:
            dir_inv = dir.inv()
            updates = {}
            for p in checked:
                np = p + dir_inv
                updates[p] = self.get(np) if np in checked else '.'
            for p in updates.keys():
                self.set(p, updates[p])
            self.set(pos, '.')
            self.robot += dir
            self.set(self.robot, '@')

    def do_all_moves(self):
        for dir in self.moves:
            self.move(self.robot, dir)

    def get_all_gps(self):
        sum_gps = 0
        for i, l in enumerate(self.grid):
            for j, c in enumerate(l):
                if c == '[':
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
