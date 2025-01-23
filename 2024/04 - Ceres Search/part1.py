from collections import defaultdict


def check_neighbors_rec(grid, p, d, i, target_str):
    return i == len(target_str) or grid[p + i * d] == target_str[i] and check_neighbors_rec(grid, p, d, i + 1, target_str)


def main(data):
    grid = defaultdict(str) | {j + 1j * i: c for i, l in enumerate(data) for j, c in enumerate(l)}
    target_str = 'XMAS'
    dir_8 = [-1j, 1 - 1j, 1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j]

    return sum(check_neighbors_rec(grid, p, d, 1, target_str) for p in list(grid.keys()) if grid[p] == target_str[0] for d in dir_8)


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
