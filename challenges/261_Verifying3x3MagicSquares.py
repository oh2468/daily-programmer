## https://old.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

from itertools import permutations

# with bonus challenge 1
def is_magic_square(nums, n):
    val_nums = range(1, (n ** 2) + 1)
    if set(val_nums) != set(nums):
        return False
    ms = sum(val_nums) // n
    drl = dlr = 0
    for i in range(n):
        rs = cs = 0
        for j in range(n):
            rs += nums[(i * n) + j]
            cs += nums[(j * n) + i]
        if rs != cs != ms:
            return False
        dlr += nums[(i * n) + i]
        drl += nums[((i + 1) * n) - (i + 1)]
    return drl == dlr == ms

# bonus challenge 2
def missing_last_row(nums):
    mi_nums = set(nums) ^ set(range(1, 10))
    return any(is_magic_square(nums + list(p), 3) for p in permutations(mi_nums))

assert is_magic_square([8, 1, 6, 3, 5, 7, 4, 9, 2], 3) == True
assert is_magic_square([2, 7, 6, 9, 5, 1, 4, 3, 8], 3) == True
assert is_magic_square([3, 5, 7, 8, 1, 6, 4, 9, 2], 3) == False
assert is_magic_square([8, 1, 6, 7, 5, 3, 4, 9, 2], 3) == False

assert missing_last_row([8, 1, 6, 3, 5, 7]) == True
assert missing_last_row([3, 5, 7, 8, 1, 6]) == False
