from collections import defaultdict


def main(data):
    target_center = 'A'
    target_sides = ['M', 'S']
    grid = defaultdict(str) | {j + 1j * i: c for i, l in enumerate(data) for j, c in enumerate(l)}
    dir_nesw = [1 - 1j, -1 + 1j]
    dir_nwse = [1 + 1j, -1 - 1j]

    return sum(
        grid[p] == target_center
        and all(c in map(lambda x: grid[p + x], diag) for c in target_sides for diag in [dir_nesw, dir_nwse])
        for p in list(grid.keys())
    )


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
