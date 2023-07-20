## https://old.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/

from collections import defaultdict


def tally(string):
    count = defaultdict(int)
    for s in string:
        count[s.lower()] += 1 if s.islower() else -1
    return sorted(count.items(), key=lambda i: i[1], reverse=True)

print(tally("abcde"))
print(tally("dbbaCEDbdAacCEAadcB"))
print(tally("EbAAdbBEaBaaBBdAccbeebaec"))

"""
challenge input: EbAAdbBEaBaaBBdAccbeebaec
challenge output: ('c', 3), ('d', 2), ('e', 1), ('a', 1), ('b', 0)
"""
