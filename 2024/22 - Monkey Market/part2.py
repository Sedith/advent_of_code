from collections import defaultdict, deque


def main(data):
    nb_iteration = 2000
    bananas_per_seq = defaultdict(int)

    for number in map(int, data):
        used_seqs = set()
        changes = deque(maxlen=4)
        last_price = number % 10
        for i in range(nb_iteration):
            number = (number ^ (number * 64)) % 16777216
            number = (number ^ (number // 32)) % 16777216
            number = (number ^ (number * 2048)) % 16777216
            changes.append(
                - last_price
                + (last_price := number % 10)
            )
            if i >= 4:
                sequence = tuple(changes)
                if sequence not in used_seqs:
                    bananas_per_seq[sequence] += last_price
                    used_seqs.add(sequence)

    return max(bananas_per_seq.values())


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
