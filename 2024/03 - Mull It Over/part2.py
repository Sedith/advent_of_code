import re


def manual_solution(data):
    data = data.splitlines()
    sum_mult = 0
    do = True
    last = ''
    n1 = ''
    n2 = ''
    for line in data:
        for c in line:
            if c == 'd':
                last = 'd'
            elif do and c == 'm':
                last = 'm'
            elif last == 'd' and c == 'o':
                last = 'do'
            elif last == 'do' and c == '(':
                last = 'do('
            elif last == 'do(' and c == ')':
                last = ''
                do = True
            elif last == 'do' and c == 'n':
                last = 'don'
            elif last == 'don' and c == '\'':
                last = 'don\''
            elif last == 'don\'' and c == 't':
                last = 'don\'t'
            elif last == 'don\'t' and c == '(':
                last = 'don\'t('
            elif last == 'don\'t(' and c == ')':
                last = ''
                do = False
            elif last == 'm' and c == 'u':
                last = 'mu'
            elif last == 'mu' and c == 'l':
                last = 'mul'
            elif last == 'mul' and c == '(':
                last = 'mul('
            elif last == 'mul(' and c.isdigit() and len(n1) < 3:
                n1 += c
            elif last == 'mul(' and c == ',':
                last = 'mul(,'
            elif last == 'mul(,' and c.isdigit() and len(n2) < 3:
                n2 += c
            elif last == 'mul(,' and c == ')' and len(n1) and len(n2):
                sum_mult += int(n1) * int(n2)
                n1 = ''
                n2 = ''
                last = ''
            else:
                n1 = ''
                n2 = ''
                last = ''
    return sum_mult


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
    # return manual_solution(data)
    global do
    do = True
    return sum(parse_match(m) for m in re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)').findall(data))


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
