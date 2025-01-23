import re


def parse_match(match):
    global do
    n1 = n2 = 0
    if match.startswith('do('):
        do = True
    elif match.startswith('don'):
        do = False
    elif do:
        n1, n2 = match[4:-1].split(',')
    return int(n1) * int(n2) * do


def main(data):
    global do
    do = True
    return sum(parse_match(m) for m in re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)').findall(data))


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
