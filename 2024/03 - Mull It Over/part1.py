import re


def main(data):
    return sum(map(lambda x: int(x[0]) * int(x[1]), map(lambda x: x[4:-1].split(','), re.compile(r'mul\(\d{1,3},\d{1,3}\)').findall(data))))


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
