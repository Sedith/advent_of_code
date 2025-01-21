import math


def check_levels_rec(report, dampener_used):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        sign = math.copysign(1, diff)
        if i == 0:
            crease = sign
        if diff == 0 or abs(diff) > 3 or sign != crease:
            if dampener_used:
                return False
            return (
                check_levels_rec(report[:i] + report[i+1:], True)
                or diff and check_levels_rec(report[:i+1] + report[i+2:], True)
                or i == 1 and check_levels_rec(report[1:], True)
            )
    return True


def main(data):
    reports = [list(map(int, l.split())) for l in data]
    return sum([check_levels_rec(r, False) for r in reports])


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
