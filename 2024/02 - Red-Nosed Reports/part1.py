import math


def check_levels(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        sign = math.copysign(1, diff)
        if i == 0:
            crease = sign
        if diff == 0 or abs(diff) > 3 or sign != crease:
            return False
    return True


def main(data):
    reports = [list(map(int, l.split())) for l in data]
    return sum(check_levels(r) for r in reports)


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
