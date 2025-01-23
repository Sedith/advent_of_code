def meta_code(code, keypad):
    meta_code = ''
    for start, end in zip('A' + code[:-1], code):
        di = keypad[end][0] - keypad[start][0]
        dj = keypad[end][1] - keypad[start][1]
        path = '<' * (-dj) + 'v' * di + '^' * (-di) + '>' * dj
        ## invert path if it goes through the empty key, if the empty key is there, its at the 'corner'
        if path and path[0] in ['v', '^'] and keypad[' '] == (keypad[end][0], keypad[start][1]) \
        or path and path[0] in ['<', '>'] and keypad[' '] == (keypad[start][0], keypad[end][1]):
            path = path[::-1]
        meta_code += path + 'A'
    return meta_code


def main(data):
    num_layout = '789', '456', '123', ' 0A'
    dir_layout = ' ^A', '<v>'
    num_keypad = {c: (i, j) for i, l in enumerate(num_layout) for j, c in enumerate(l)}
    dir_keypad = {c: (i, j) for i, l in enumerate(dir_layout) for j, c in enumerate(l)}

    max_deg = 3

    sum_complexities = 0
    for code in data:
        numeric_part = int(code[:-1])
        for deg in range(max_deg):
            code = meta_code(code, dir_keypad if deg else num_keypad)
        sum_complexities += numeric_part * len(code)
    return sum_complexities


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
