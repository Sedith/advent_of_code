from functools import cache


@cache
def path_len_rec(start, end, deg, max_deg):
    global dir_keypad, num_keypad
    if deg == max_deg:
        return 1

    keypad = dir_keypad if deg else num_keypad
    di = keypad[end][0] - keypad[start][0]
    dj = keypad[end][1] - keypad[start][1]
    path = '<' * (-dj) + 'v' * di + '^' * (-di) + '>' * dj
    ## invert path if it goes through the empty key, if the empty key is there, its at the 'corner'
    if (path and path[0] in ['v', '^'] and keypad[' '] == (keypad[end][0], keypad[start][1])) or (
        path and path[0] in ['<', '>'] and keypad[' '] == (keypad[start][0], keypad[end][1])
    ):
        path = path[::-1]

    return sum([path_len_rec(c1, c2, deg + 1, max_deg) for c1, c2 in zip('A' + path, path + 'A')])


def main(data):
    global dir_keypad, num_keypad
    num_layout = '789', '456', '123', ' 0A'
    dir_layout = ' ^A', '<v>'
    num_keypad = {c: (i, j) for i, l in enumerate(num_layout) for j, c in enumerate(l)}
    dir_keypad = {c: (i, j) for i, l in enumerate(dir_layout) for j, c in enumerate(l)}
    max_deg = 26

    return sum([int(code[:-1]) * sum(path_len_rec(c1, c2, 0, max_deg) for c1, c2 in zip('A' + code[:-1], code)) for code in data])


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
