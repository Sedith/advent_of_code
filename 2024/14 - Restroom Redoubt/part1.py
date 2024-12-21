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
        grid[r.p[0]][r.p[1]] += 1
    for i in range(grid_size[0]):
        grid[i][grid_size[1] // 2] = ' '
    grid[grid_size[0] // 2][:] = [' ']
    print(''.join([''.join([str(c) if c else '.' for c in l]) + '\n' for l in grid])[:-1])


def count_quadrant(grid_size, robots):
    tl = 0
    tr = 0
    br = 0
    bl = 0
    hw = grid_size[1] // 2
    hh = grid_size[0] // 2
    for r in robots:
        if r.p[0] < hh:
            if r.p[1] < hw:
                tl += 1
            elif r.p[1] > hw:
                tr += 1
        elif r.p[0] > hh:
            if r.p[1] < hw:
                bl += 1
            elif r.p[1] > hw:
                br += 1
    return tl * tr * br * bl


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


def main(data):
    grid_size, robots = parse(data)
    for _ in range(100):
        for r in robots:
            r.move(grid_size)
    # display(grid_size, robots)
    return count_quadrant(grid_size, robots)


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
