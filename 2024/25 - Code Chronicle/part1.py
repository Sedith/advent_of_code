def split_chunks(data):
    chunk = []
    for line in data:
        if line:
            chunk.append(line)
        elif chunk:
            yield chunk
            chunk = []
    yield chunk


def transpose(l):
    return list(map(list, zip(*l)))


def parse(data):
    schematics = [(s[0][0], [col.count(s[0][-1]) for col in s]) for s in map(transpose, split_chunks(data))]
    return [s[1] for s in schematics if s[0] == '#'], [s[1] for s in schematics if s[0] == '.']


def main(data):
    locks, keys = parse(data)
    return sum([all([k <= l for k, l, in zip(key, lock)]) for key in keys for lock in locks])


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
