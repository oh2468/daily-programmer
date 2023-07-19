## https://old.reddit.com/r/dailyprogrammer/comments/9cvo0f/20180904_challenge_367_easy_subfactorials_another/

def sub_fac(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (sub_fac(n - 1) + sub_fac(n - 2))

# bonus (code gold)
sfb = lambda n: (n-1)*(sfb(n-1)+sfb(n-2)) if n >= 2 else (0 if n==1 else 1)

assert sub_fac(5) == 44
assert sub_fac(6) == 265
assert sub_fac(9) == 133496
assert sub_fac(14) == 32071101049

assert sfb(5) == 44
assert sfb(6) == 265
assert sfb(9) == 133496
assert sfb(14) == 32071101049
