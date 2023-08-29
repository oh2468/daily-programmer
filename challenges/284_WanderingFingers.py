## https://old.reddit.com/r/dailyprogrammer/comments/53ijnb/20160919_challenge_284_easy_wandering_fingers/

from urllib import request


try:
    with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
        all_words = file.read().split("\n")
except FileNotFoundError:
    all_words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

# with bonus
def find_word(swype, l):
    possible = []
    for word in all_words:
        if len(word) < l or word[0] != swype[0] or word[-1] != swype[-1]:
            continue
        match, i = True, 0
        for c in word:
            try:
                i = swype.index(c, i)
            except ValueError:
                match = False
                break
        if match:
            possible.append(word)
    return set(possible)

assert find_word("qwertyuytresdftyuioknn", 5) == set("queen question".split())
assert find_word("gijakjthoijerjidsdfnokg", 5) == set("gaeing garring gathering gating geeing gieing going goring".split())
