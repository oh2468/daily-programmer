## https://old.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

from urllib import request
from collections import defaultdict
from itertools import product

codes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split(" ")
code_map = {chr(i + 97): c for i, c in enumerate(codes)}

def smorse(string):
    # return "".join(code_map[s] for s in string)
    return "".join(codes[ord(s) - 97] for s in string)
    # return [code_map[s] for s in string]

# bonus challenges 
try:
    with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
        words = file.read().split("\n")
except FileNotFoundError:
    words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

code_words_map = defaultdict(list)
for word in words:
    code_words_map[smorse(word)].append(word)

# bonus 1 - answer: ['babe', 'bans', 'bates', 'bath', 'begs', 'deans', 'death', 'digs', 'dimes', 'duns', 'neeps', 'nips', 'tsadi']
def smorse_b1(n):
    return [l for c, l in code_words_map.items() if len(l) == n]

# bonus 2 - answer: 'bottommost'
def smorse_b2(patt):
    return [w for c, w in code_words_map.items() if patt in c]

# bonus 3 - answer: 'overcommercialization'
def smorse_b3(l):
    return [w for c, ws in code_words_map.items() for w in ws if c.count(".") == c.count("-") and len(w) == l]

# bonus 4 - answer: 'intransigence'
def smorse_b4(l):
    w_l = [w for w in words if len(w) == l]
    return [w for w in w_l if (c := smorse(w)) == c[::-1]]

# bonus 5 - answer: {'---.----.----', '--.---.------', '---.---.---.-', '---.---.-----'}
def smorse_b5(l):
    len_set = {c[i:i+l] for c in code_words_map.keys() for i in range(1 + len(c) - l)}
    code_set = set("".join(p) for p in product(".-", repeat=l))
    return code_set - len_set

assert smorse("sos") == "...---..."
assert smorse("daily") == "-...-...-..-.--"
assert smorse("programmer") == ".--..-.-----..-..-----..-."
assert smorse("bits") == "-.....-..."
assert smorse("three") == "-.....-..."

print(smorse_b1(13))

print(smorse_b2("-"*15))

print(smorse_b3(21))

print(smorse_b4(13))

print(smorse_b5(13))
