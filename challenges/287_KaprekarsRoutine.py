## https://old.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/

def largest_digit(n):
    return int(max(str(n)))

# bonus 1
def desc_digits(n, desc=True):
    return int("".join(sorted(str(n).rjust(4, "0"), reverse=desc)))

# bonus 2
def kaprekar(n):
    if n == 6174 or (n > 1000 and len(set(str(n))) == 1):
        return 0
    else:
        return 1 + kaprekar(desc_digits(n, True) - desc_digits(n, False))

# bonus 3
def find_largest_n():
    return max((kaprekar(i), i) for i in range(1, 10000))

assert largest_digit(1234) == 4
assert largest_digit(3253) == 5
assert largest_digit(9800) == 9
assert largest_digit(3333) == 3
assert largest_digit(120) == 2

assert desc_digits(1234) == 4321
assert desc_digits(3253) == 5332
assert desc_digits(9800) == 9800
assert desc_digits(3333) == 3333
assert desc_digits(120) == 2100

assert kaprekar(6589) == 2
assert kaprekar(5455) == 5
assert kaprekar(6174) == 0

print(find_largest_n())
