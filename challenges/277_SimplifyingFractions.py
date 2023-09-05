## https://old.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/

from math import gcd


# using built-ins
def reduced_fractions(a, b):
    return (a // (g := gcd(a, b)), b // g)

# using the euclidean algorithm
def euc_gcd_rec(a, b):
    return a if b == 0 else euc_gcd_rec(b, a % b)

def euc_gcd_loo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduced_fractions_2(a, b):
    return (a // (g := euc_gcd_loo(a, b)), b // g)

assert reduced_fractions(4, 8) == (1, 2)
assert reduced_fractions(1536, 78360) == (64, 3265)
assert reduced_fractions(51478, 5536) == (25739, 2768)
assert reduced_fractions(46410, 119340) == (7, 18)
assert reduced_fractions(7673, 4729) == (7673, 4729)
assert reduced_fractions(4096, 1024) == (4, 1)

assert reduced_fractions_2(4, 8) == (1, 2)
assert reduced_fractions_2(1536, 78360) == (64, 3265)
assert reduced_fractions_2(51478, 5536) == (25739, 2768)
assert reduced_fractions_2(46410, 119340) == (7, 18)
assert reduced_fractions_2(7673, 4729) == (7673, 4729)
assert reduced_fractions_2(4096, 1024) == (4, 1)
