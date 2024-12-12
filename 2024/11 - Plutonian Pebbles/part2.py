from collections import defaultdict


def expand_stone(stone):
    if stone == '0':
        return ['1']
    elif not len(stone) % 2:
        n = int(len(stone)/2)
        return [stone[:n], str(int(stone[n:]))]
    else:
        return [str(int(stone) * 2024)]


def expand_rec(mem, max_depth, depth, stone):
    if depth == max_depth:
        return 1
    else:
        ## this is ok (helps to speed up to a lot)
        ## but it would be better to exploit stored memory better (eg store the list of nodes N levels below the current depth)
        if stone in mem.keys() and depth in mem[stone].keys():
            return mem[stone][depth]
        else:
            val = sum([expand_rec(mem, max_depth, depth+1, s) for s in expand_stone(stone)])
            mem[stone].update({depth: val})
            return val


def main(data):
    stones = data[0].split()
    nb_iter = 75
    return sum([expand_rec(defaultdict(dict), nb_iter, 0, s) for s in stones])


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
