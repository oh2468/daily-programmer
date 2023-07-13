## https://old.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

import time
from collections import Counter
from urllib import request


def yahtzee_upper(dice):
    return max(c[0] * c[1] for c in Counter(dice).items())

# bonus challenge - answer: 31415926535
text_file = str(request.urlopen("https://gist.githubusercontent.com/cosmologicon/beadf49c9fe50a5c2a07ab8d68093bd0/raw/fb5af1a744faf79d64e2a3bb10973e642dc6f7b0/yahtzee-upper-1.txt").read(), "UTF-8")
dice = map(int, text_file.split("\n"))

assert yahtzee_upper([2, 3, 5, 5, 6]) == 10
assert yahtzee_upper([1, 1, 1, 1, 3]) == 4
assert yahtzee_upper([1, 1, 1, 3, 3]) == 6
assert yahtzee_upper([1, 2, 3, 4, 5]) == 5
assert yahtzee_upper([6, 6, 6, 6, 6]) == 30

# bonus
assert yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747, 1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654, 30864, 4868, 30864]) == 123456

s1 = time.time()
m = yahtzee_upper(dice)
s2 = time.time()
print(f"max: {m}, time: {s2 - s1}")