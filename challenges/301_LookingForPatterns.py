## https://old.reddit.com/r/dailyprogrammer/comments/5rlpz1/20170202_challenge_301_easyintemerdiate_looking/

from urllib import request


try:
    with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
        all_words = file.read().split("\n")
except FileNotFoundError:
    all_words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

def find_words(patt):
    maps = {tuple(i for i, x in enumerate(patt) if x == y) for y in patt}
    matches = []
    p = len(patt)
    for word in all_words:
        w = len(word)
        if w < p:
            continue
        for i in range(w - p + 1):
            chars = set()
            for map in maps:
                if len(s := {word[i + m] for m in map}) == 1:
                    chars |= s
            if len(chars) == len(maps):
                matches.append(word)
                break
    print(matches)
    return "\n".join(matches)

pattern_1 = "XXYY"
output_1 = """aarrgh
aarrghh
addressee
addressees
allee
allees
allottee
allottees
appellee
appellees
arrowwood
arrowwoods
balloon
ballooned
ballooning
balloonings
balloonist
balloonists
balloons
barroom
barrooms
bassoon
bassoonist
bassoonists
bassoons
belleek
belleeks"""

pattern_2 = "XXYYZZ"
output_2 = """bookkeeper
bookkeepers
bookkeeping
bookkeepings"""

pattern_3 = "XXYYX"
output_3 = """addressees
betweenness
betweennesses
colessees
fricassees
greenness
greennesses
heelless
keelless
keenness
keennesses
lessees
wheelless"""

assert find_words(pattern_1).startswith(output_1)
assert find_words(pattern_2) == output_2
assert find_words(pattern_3) == output_3
