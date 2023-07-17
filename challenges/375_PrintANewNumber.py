## https://old.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/

import random


def add_one(n):
    return int("".join(str(int(s) + 1) for s in str(n)))

# bonus challenge (no string cast)
def add_one_b(n):
    nums = []
    while n > 0:
        nums.append((n % 10) + 1)
        n = n // 10
    c = s = 0
    for num in nums:
        s += num * 10**c
        c += 1 if num < 10 else 2
    return s

# shorter version of bonus
def add_one_b_s(n):
    c = s = 0
    while n > 0:
        x = (n % 10) + 1
        s += x * 10**c
        c += 1 if x < 10 else 2
        n = n // 10
    return s

# print(add_one(9))
# print(add_one(998))
# print(add_one(12345))
# print(add_one(7654))
# print(add_one(919191))

# print(add_one_b(9))
# print(add_one_b(998))
# print(add_one_b(12345))
# print(add_one_b(7654))
# print(add_one_b(919191))

for i in range(10000):
    r = random.randint(0, 1e10)
    assert add_one(r) == add_one_b(r) == add_one_b_s(r)
