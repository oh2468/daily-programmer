## https://old.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/

def smallest(n):
    n_sqrt = n ** 0.5
    if n_sqrt / int(n_sqrt) == 1:
        return n_sqrt + n_sqrt
    b = c = 0
    for i in range(1, int(n_sqrt) + 1):
        if n % i == 0:
            b = i
            c = n / i
    return b + c

assert smallest(12) == 7
assert smallest(456) == 43
assert smallest(4567) == 4568
assert smallest(12345) == 838

# bonus challenge 1 - answer = 2544788
print(smallest(1234567891011))
