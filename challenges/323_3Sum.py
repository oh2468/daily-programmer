## https://old.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/

from itertools import combinations

def three_sum(nums):
    return {tuple(sorted(c)) for c in combinations(nums, 3) if sum(c) == 0}

assert three_sum([9, -6, -5, 9, 8, 3, -4, 8, 1, 7, -4, 9, -9, 1, 9, -9, 9, 4, -6, -8]) == {(-9, 1, 8), (-8, 1, 7), (-5, -4, 9), (-5, 1, 4), (-4, 1, 3), (-4, -4, 8)}
assert three_sum([4, 5, -1, -2, -7, 2, -5, -3, -7, -3, 1]) == {(-7, 2, 5), (-5, 1, 4), (-3, -2, 5), (-3, -1, 4), (-3, 1, 2)}
assert three_sum([-1, -6, -3, -7, 5, -8, 2, -8, 1]) == {(-7, 2, 5), (-6, 1, 5), (-3, 1, 2)}
assert three_sum([-5, -1, -4, 2, 9, -9, -6, -1, -7]) == {(-5, -4, 9), (-1, -1, 2)}
