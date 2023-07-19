## https://old.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/

from urllib import request
from collections import defaultdict


def funnel(s1, s2):
    for i in range(len(s1)):
        if (s1[0:i:] + s1[i + 1::]) == s2:
            return True
    return False
    # code golf version
    return any(s1[0:i:] + s1[i + 1::] == s2 for i in range(len(s1)))

# bonus challenges
try:
    with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
        words = file.read().split("\n")
except FileNotFoundError:
    words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

word_set = set(words)

def bonus_1(word):
    matches = set()
    funneled_words = lambda word: [word[0:i:] + word[i + 1::] for i in range(len(word))]
    for w in funneled_words(word):
        if w in word_set:
            matches.add(w)
    return matches

def bonus_2():
    has_len_five = []
    for word in words:
        if len(word) < 5:
            continue
        funnels = bonus_1(word)
        if len(funnels) == 5:
            print(f"{word}: {funnels}")
            has_len_five.append(funnels)
    return has_len_five

assert funnel("leave", "eave") == True
assert funnel("reset", "rest") == True
assert funnel("dragoon", "dragon") == True
assert funnel("eave", "leave") == False
assert funnel("sleet", "lets") == False
assert funnel("skiff", "ski") == False

assert bonus_1("dragoon") == set(["dragon"])
assert bonus_1("boats") == set(["oats", "bats", "bots", "boas", "boat"])
assert bonus_1("affidavit") == set([])

assert len(bonus_2()) == 28
