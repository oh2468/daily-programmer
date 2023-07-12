## https://old.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

from urllib import request
from collections import defaultdict


def same_necklace(a, b):
    if len(a) != len(b):
        return False

    if a == b:
        return True
    
    for i in range(len(a)):
        if a == b[i:] + b[0:i]:
            return True
    
    return False

# inspired solution
def inspired(a, b):
    return len(a) == len(b) and b in a + a

# bonus 1
def repeats(a):
    return 1 if len(a) == 0 else sum(a == a[i:] + a[0:i] for i in range(len(a)))

# bonus 2 - answer: {'stope', 'topes', 'pesto', 'estop'}
def necklace_count(n):
    try:
        with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
            words = file.read().split("\n")
    except FileNotFoundError:
        words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")
    
    necklace_map = defaultdict(list)

    for word in words:
        for i in range(len(word)):
            necklace_map[word[i:] + word[0:i]].append(word)
    
    matches = []
    for wrds in necklace_map.values():
        if len(wrds) == n:
            matches.append(wrds)
    
    return set(w for m in matches for w in m)

assert same_necklace("nicole", "icolen") == True
assert same_necklace("nicole", "lenico") == True
assert same_necklace("nicole", "coneli") == False
assert same_necklace("aabaaaaabaab", "aabaabaabaaa") == True
assert same_necklace("abc", "cba") == False
assert same_necklace("xxyyy", "xxxyy") == False
assert same_necklace("xyxxz", "xxyxz") == False
assert same_necklace("x", "x") == True
assert same_necklace("x", "xx") == False
assert same_necklace("x", "") == False
assert same_necklace("", "") == True

assert inspired("nicole", "icolen") == True
assert inspired("nicole", "lenico") == True
assert inspired("nicole", "coneli") == False
assert inspired("aabaaaaabaab", "aabaabaabaaa") == True
assert inspired("abc", "cba") == False
assert inspired("xxyyy", "xxxyy") == False
assert inspired("xyxxz", "xxyxz") == False
assert inspired("x", "x") == True
assert inspired("x", "xx") == False
assert inspired("x", "") == False
assert inspired("", "") == True

assert repeats("abc") == 1
assert repeats("abcabcabc") == 3
assert repeats("abcabcabcx") == 1
assert repeats("aaaaaa") == 6
assert repeats("a") == 1
assert repeats("") == 1

print(necklace_count(4))
