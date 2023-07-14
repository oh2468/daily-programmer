## https://old.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

from itertools import permutations
from functools import reduce
from math import prod


def fit1(x1, y1, x2, y2):
    return (x1 // x2) * (y1 // y2)

#bonus challenges
def fit2(x1, y1, x2, y2):
    return max(fit1(x1, y1, x2, y2), fit1(x1, y1, y2, x2))

def fit3(x1, y1, z1, x2, y2, z2):
    f3 = lambda x1, x2, y1, y2, z1, z2: (x1 // x2) * (y1 // y2) * (z1 // z2)
    combs = [
        (x2, y2, z2),
        (x2, z2, y2),
        (y2, x2, z2),
        (y2, z2, x2),
        (z2, x2, y2),
        (z2, y2, x2)
    ]
    return max(f3(x1, c[0], y1, c[1], z1, c[2]) for c in combs)

def fitn(lst1, lst2):
    # easier to read solution of the list comprehension
    # fits = []
    # for permutation in permutations(lst2):
    #     prod = 1
    #     for v1 ,v2 in zip(lst1, permutation):
    #         prod *= v1 // v2
    #     fits.append(prod)
    # return max(fits)

    # return max(reduce(lambda x, y: x * y, map(lambda v: v[0] // v[1], zip(lst1, p)), 1) for p in permutations(lst2))

    # with math prod instead of reduce
    return max(prod(map(lambda v: v[0] // v[1], zip(lst1, p))) for p in permutations(lst2))

assert fit1(25, 18, 6, 5) == 12
assert fit1(10, 10, 1, 1) == 100
assert fit1(12, 34, 5, 6) == 10
assert fit1(12345, 678910, 1112, 1314) == 5676
assert fit1(5, 100, 6, 1) == 0

assert fit2(25, 18, 6, 5) == 15
assert fit2(12, 34, 5, 6) == 12
assert fit2(12345, 678910, 1112, 1314) == 5676
assert fit2(5, 5, 3, 2) == 2
assert fit2(5, 100, 6, 1) == 80
assert fit2(5, 5, 6, 1) == 0

assert fit3(10, 10, 10, 1, 1, 1) == 1000
assert fit3(12, 34, 56, 7, 8, 9) == 32
assert fit3(123, 456, 789, 10, 11, 12) == 32604
assert fit3(1234567, 89101112, 13141516, 171819, 202122, 232425) == 174648

assert fitn([3, 4], [1, 2]) == 6
assert fitn([123, 456, 789], [10, 11, 12]) == 32604
assert fitn([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]) == 1883443968
