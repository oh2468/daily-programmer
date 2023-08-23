## https://old.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

from collections import Counter
from urllib import request


def scrabble(tiles, word):
    return Counter(word) <= Counter(tiles)

# bonus challenge 1
def scrabble_b1(tiles, word):
    tls = Counter(tiles)
    tls.subtract(word)
    return tls.get("?", 0) + sum(v for v in tls.values() if v < 0) >= 0

# bonus challenges 
try:
    with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
        all_words = file.read().split("\n")
except FileNotFoundError:
    all_words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

# bonus challenge 2
def longest(tiles):
    lngst = ""
    for word in all_words:
        if len(word) > len(lngst) and scrabble_b1(tiles, word):
            lngst = word
    return lngst

# bonus challenge 3
points = {
    "a": 1, "b": 3, "c": 3, "d": 2,
    "e": 1, "f": 4, "g": 2, "h": 4,
    "i": 1, "j": 8, "k": 5, "l": 1,
    "m": 3, "n": 1, "o": 1, "p": 3,
    "q": 10, "r": 1, "s": 1, "t": 1,
    "u": 1, "v": 4, "w": 4, "x": 8,
    "y": 4, "z": 10
}

def highest(tiles):
    hs, hw = 0, ""
    for word in all_words:
        if scrabble_b1(tiles, word):
            ws, tc, wc = set(word), Counter(tiles), Counter(word)
            sc = sum(points[c] * min(tc[c], wc[c]) for c in ws)
            if sc > hs:
                hs, hw = sc, word
    return hw

print("running challenge")
assert scrabble("ladilmy", "daily") == True
assert scrabble("eerriin", "eerie") == False
assert scrabble("orrpgma", "program") == True
assert scrabble("orppgma", "program") == False

print("running bonus 1")
assert scrabble_b1("pizza??", "pizzazz") == True
assert scrabble_b1("piizza?", "pizzazz") == False
assert scrabble_b1("a??????", "program") == True
assert scrabble_b1("b??????", "program") == False

print("running bonus 2")
assert longest("dcthoyueorza") == "coauthored"
assert longest("uruqrnytrois") == "turquois"
assert longest("rryqeiaegicgeo??") == "greengrocery"
assert longest("udosjanyuiuebr??") == "subordinately"
assert longest("vaakojeaietg????????") == "ovolactovegetarian"

print("running bonus 3")
assert highest("dcthoyueorza") == "zydeco"
assert highest("uruqrnytrois") == "squinty"
assert highest("rryqeiaegicgeo??") == "reacquiring"
assert highest("udosjanyuiuebr??") == "jaybirds"
assert highest("vaakojeaietg????????") == "straightjacketed"
