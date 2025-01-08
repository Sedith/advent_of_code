def meta_code(code, keypad):
    meta_code = ''
    pointer = 'A'
    for c in code:
        di = keypad[c][0] - keypad[pointer][0]
        dj = keypad[c][1] - keypad[pointer][1]
        path = '<' * (-dj) + 'v' * di + '^' * (-di) + '>' * dj
        ## invert path if it goes through the empty key
        ## if its there, its at a 'corner' of the path so only 2 checks needed
        if keypad[' '] in [(keypad[c][0], keypad[pointer][1]), (keypad[pointer][0], keypad[c][1])]:
            path = path[::-1]
        meta_code += path + 'A'
        pointer = c
    return meta_code


def main(data):
    num_layout = '789', '456', '123', ' 0A'
    dir_layout = ' ^A', '<v>'
    num_keypad = {c: (i, j) for i, l in enumerate(num_layout) for j, c in enumerate(l)}
    dir_keypad = {c: (i, j) for i, l in enumerate(dir_layout) for j, c in enumerate(l)}

    max_deg = 3

    sum_complexities = 0
    for l in data:
        code = l
        for deg in range(max_deg):
            code = meta_code(code, dir_keypad if deg else num_keypad)
        sum_complexities += int(l[:-1]) * len(code)
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
