import numpy as np
import matplotlib.pyplot as plt


class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def move(self, grid_size):
        self.p[0] = (self.p[0] + self.v[0]) % grid_size[0]
        self.p[1] = (self.p[1] + self.v[1]) % grid_size[1]


def display(grid_size, robots):
    grid = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    for r in robots:
        grid[r.p[0]][r.p[1]] = 1
    grid = np.array(grid)
    plt.imshow(grid)
    plt.show(block=False)
    plt.waitforbuttonpress()


def parse(data):
    robots = []
    if data[0].startswith('grid size'):
        l = data.pop(0)
        grid_size = list(map(int, l.split(': ')[1].split(',')))
    else:
        grid_size = (103, 101)
    for l in data:
        lp, lv = l.split()
        p = list(map(int, lp.split('=')[1].split(',')))
        v = list(map(int, lv.split('=')[1].split(',')))
        robots.append(Robot(p[::-1], v[::-1]))
    return grid_size, robots


def get_std(robots):
    return np.array([r.p for r in robots]).std()


def main(data):
    grid_size, robots = parse(data)
    stds = [get_std(robots)]
    th = 0.75  # threshold is 25% of std decrease
    i = 0
    while 1:
        i += 1
        for r in robots:
            r.move(grid_size)
        std = get_std(robots)
        if std < th * np.mean(stds):
            break
        else:
            stds.append(std)
    return i


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
