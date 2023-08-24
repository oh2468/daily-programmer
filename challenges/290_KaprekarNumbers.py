## https://old.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/

from math import log10


def is_kaprekar(n):
    if n == 1: return True
    if float(log10(n)).is_integer(): return False
    x = str(n ** 2)
    return any(int(x[:i]) + int(x[i:]) == n for i in range(1, len(x)))


def find_kaprekar(r):
    b, e = map(int, r.split())
    return [i for i in range(b, e + 1) if is_kaprekar(i)]

assert find_kaprekar("1 50") == [1, 9, 45]
assert find_kaprekar("2 100") == [9, 45, 55, 99]
assert find_kaprekar("101 9000") == [297, 703, 999, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777]
