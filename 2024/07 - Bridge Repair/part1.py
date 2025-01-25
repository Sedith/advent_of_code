def check_rec(poss, nums):
    if not nums:
        return poss
    return check_rec([i for p in poss for i in [p + nums[0], p * nums[0]]], nums[1:])


def main(data):
    ops = ((r[0], n) for r, n in ([list(map(int, p.split())) for p in l.split(':')] for l in data))
    # return sum(r for r, n in ops if r in check_rec([n[0]], n[1:]))
    return [print(check_rec([n[0]], n[1:])) for r, n in ops]


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
