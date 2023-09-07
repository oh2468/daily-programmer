## https://old.reddit.com/r/dailyprogrammer/comments/4nvrnx/20160613_challenge_271_easy_critical_hit/

def probability(d, h):
    prod, c = 1, h
    while d < c:
        prod *= 1 / d
        c -= d
    prod *= ((d + 1) - c) / d
    return prod

assert probability(4, 1) == 1
assert probability(4, 4) == 0.25
assert probability(4, 5) == 0.25
assert probability(4, 6) == 0.1875
assert probability(1, 10) == 1
assert probability(100, 200) == 0.0001
assert probability(8, 20) == 0.009765625
