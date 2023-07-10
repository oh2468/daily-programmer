## https://old.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def numcompare(a, b):
    sum_string = lambda s: sum(num_map[c] for c in s)
    return sum_string(a) < sum_string(b)

assert numcompare("I", "I") == False
assert numcompare("I", "II") == True
assert numcompare("II", "I") == False
assert numcompare("V", "IIII") == False
assert numcompare("MDCLXV", "MDCLXVI") == True
assert numcompare("MM", "MDCCCCLXXXXVIIII") == False
