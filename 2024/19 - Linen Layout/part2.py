from functools import cache

@cache
def check_pattern(tokens, pattern):
    if not pattern:
        return 1

    return sum(check_pattern(tokens, pattern[len(t):]) for t in tokens if pattern.startswith(t))


def main(data):
    tokens = tuple(data[0].split(', '))
    patterns = data[2:]

    return sum(check_pattern(tokens, p) for p in patterns)


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
