from collections import defaultdict
from functools import cmp_to_key


def manual_check(rules, update):
    is_fixed = not any(prev not in update[:i] and prev in update[i:] for i, page in enumerate(update) for prev in rules[page])
    return is_fixed * int(update[len(update) // 2])


def sort_based_check(rules, update):
    fixed = sorted(update, key=cmp_to_key(lambda a, b: -1 if a in update[: update.index(b)] else (1 if b in rules[a] else -1)))
    return (fixed == update) * int(update[len(update) // 2])


def main(data):
    ## build ordering dict
    rules = defaultdict(list)
    i = -1
    while (data[i := i + 1]) != '':
        before, after = data[i].split('|')
        rules[after].append(before)

    ## check update
    # return sum(manual_check(rules, update) for update in map(lambda l: l.split(','), data[i + 1 :]))  # ~8ms
    return sum(sort_based_check(rules, update) for update in map(lambda l: l.split(','), data[i + 1 :]))  # ~2ms


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
