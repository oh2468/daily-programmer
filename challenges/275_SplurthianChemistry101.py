## https://old.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

from itertools import combinations


def follows_rule(element, symbol):
    e, s = element.lower(), symbol.lower()
    return s[0] in e and s[1] in e[e.index(s[0]) + 1:]

# bonus challenge 1
def first_alpha(element):
    return "".join(sorted(c for c in combinations(element.lower(), 2))[0]).capitalize()

# bonus challenge 2
def distinct_symbols(element, l=2):
    return len(set(c for c in combinations(element.lower(), l)))

# bonus challenge 3
def distinct_blurth(element):
    e = element.lower()
    return sum(distinct_symbols(e, i) for i in range(1, len(e) + 1))

assert follows_rule("Spenglerium", "Ee") == True
assert follows_rule("Zeddemorium", "Zr") == True
assert follows_rule("Venkmine", "Kn") == True
assert follows_rule("Stantzon", "Zt") == False
assert follows_rule("Melintzum", "Nn") == False
assert follows_rule("Tullium", "Ty") == False
assert first_alpha("Gozerium") == "Ei"
assert first_alpha("Slimyrine") == "Ie"
assert distinct_symbols("Zuulon") == 11
assert distinct_blurth("Zuulon") == 47
