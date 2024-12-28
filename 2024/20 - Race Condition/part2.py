def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]


def find_path(data):
    (pos,) = ((i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == 'S')

    path = [None, pos]  # add None in order to allow looking at path[-2]
    while data[pos[0]][pos[1]] != 'E':
        (pos,) = (np for np in [add(pos, d) for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]] if np != path[-2] and data[np[0]][np[1]] in ['.', 'E'])
        path.append(pos)
    return path[1:]


def dist_l1(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def cheats(path, max_dist):
    nb_cheats = 0
    min_gain = 102  # 100 gains and distance is at least 2
    for i, p1 in enumerate(path[:-min_gain]):
        for j, p2 in enumerate(path[i + min_gain :]):
            d = dist_l1(p1, p2)
            if d <= max_dist and j + 2 >= d:
                nb_cheats += 1
    return nb_cheats


def main(data):
    path = find_path(data)
    return cheats(path, 20)


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
