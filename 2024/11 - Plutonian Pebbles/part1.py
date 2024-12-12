def expand_stone(stone):
    if stone == '0':
        return ['1']
    elif not len(stone) % 2:
        n = int(len(stone)/2)
        return [stone[:n], str(int(stone[n:]))]
    else:
        return [str(int(stone) * 2024)]


def expand_rec(max_depth, depth, stone):
    if depth == max_depth:
        return 1
    else:
        return sum([expand_rec(max_depth, depth+1, s) for s in expand_stone(stone)])


def main(data):
    stones = data[0].split()
    nb_iter = 25

    # ## recursive version (~250 ms)
    # return sum([expand_rec(nb_iter, 0, s) for s in stones])

    ## for loop version (~130 ms)
    for _ in range(nb_iter):
        expanded = []
        for s in stones:
            expanded += expand_stone(s)
        stones = expanded
    return len(stones)


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
