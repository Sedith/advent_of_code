def check_rec(target, nums):
    if len(nums) == 1:
        return target == nums[0]

    can_c = (t_str := str(target)).endswith(op_str := str(nums[-1]))
    can_m = target % nums[-1] == 0
    can_s = target >= nums[-1]

    return (
        can_c and check_rec(int('0' + t_str[: -len(op_str)]), nums[:-1])
        or can_m and check_rec(target // nums[-1], nums[:-1])
        or can_s and check_rec(target - nums[-1], nums[:-1])
    )


def main(data):
    ops = ((r[0], n) for r, n in ([list(map(int, p.split())) for p in l.split(':')] for l in data))
    return sum(r for r, n in ops if check_rec(r, n))


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
