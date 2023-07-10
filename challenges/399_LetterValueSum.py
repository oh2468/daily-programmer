## https://old.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

import urllib.request
from collections import Counter, defaultdict


def lettersum(string):
    return sum(ord(s) - 96 for s in string)

assert lettersum("") == 0
assert lettersum("a") == 1
assert lettersum("z") == 26
assert lettersum("cab") == 6
assert lettersum("excellent") == 100
assert lettersum("microspectrophotometries") == 317


## bonus challanges ##
try:
    with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
        all_words = file.read().split("\n")
except FileNotFoundError:
    all_words = str(urllib.request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

def words_specifc_sum(s):
    return [word for word in all_words if lettersum(word) == s]

def words_odd_sum(odd=True):
    return len([w for w in all_words if lettersum(w) % 2 != odd])

def words_sum_count():
    return Counter([lettersum(w) for w in all_words])

sum_words_map = defaultdict(list)
for word in all_words:
    sum_words_map[lettersum(word)].append(word)

def words_same_sum_diff(d):
    pairs = []
    for s, wordlist in sum_words_map.items():
        for i, w1 in enumerate(wordlist):
            for j in range(i + 1, len(wordlist)):
                w2 = wordlist[j]
                if abs(len(w1) - len(w2)) == d:
                    pairs.append((s, w1, w2))
    return pairs

## inspired bonus 4 - much faster
def inspired_4(d):
    sum_len_word_map = defaultdict(list)
    for word in all_words:
        sum_len_word_map[(lettersum(word), len(word))].append(word)
    pairs = []
    for (s, l), words in sum_len_word_map.items():
        for lo_match in sum_len_word_map.get((s, l - d), []):
            pairs += [(s, w, lo_match) for w in words]
        for hi_match in sum_len_word_map.get((s, l + d), []):
            pairs += [(s, w, hi_match) for w in words]
        sum_len_word_map[(s, l)] = []
    return pairs

def words_same_sum_unique(m):
    pairs = []
    for s, wordlist in sum_words_map.items():
        if s <= m:
            continue
        for i, w1 in enumerate(wordlist):
            for j in range(i + 1, len(wordlist)):
                w2 = wordlist[j]
                if not (set(w1) & set(w2)):
                    pairs.append((s, w1, w2))
    return pairs

def words_ordered_len_sum():
    len_sum_words = [(len(w), lettersum(w), w) for w in all_words]
    len_sum_words.sort(key=lambda x: (-x[0], x[1]))

    all_lists = []
    curr_len = len_sum_words[0][0] + 1
    for i, (l1, s1, w1) in enumerate(len_sum_words):
        if l1 >= curr_len:
            continue
        lst = [w1]
        curr_sum = s1
        curr_len = l1
        for j in range(i + 1, len(len_sum_words)):
            l2, s2, w2 = len_sum_words[j]
            if l2 >= curr_len:
                continue
            if s2 > curr_sum:
                lst.append(w2)
                curr_sum = s2
                curr_len = l2
        curr_len = l1
        all_lists.append(lst)
    return all_lists


# bonus 1 - answer: reinstitutionalizations
print(words_specifc_sum(319))

# bonus 2 - answer: 86339
print(words_odd_sum(False))

# bonus 3 - answer: sum = 93, words = 1965
print(words_sum_count().most_common(1))

# bonus 4 - answer: [(151, 'biodegradabilities', 'zyzzyva'), (219, 'electroencephalographic', 'voluptuously')]
# print(words_same_sum_diff(11))
print(inspired_4(11))

# bonus 5 - answer: [(194, 'defenselessnesses', 'microphotographic'), (194, 'defenselessnesses', 'photomicrographic')]
print(words_same_sum_unique(188))

#bonus 6 - answer: ['ineffaceabilities', 'adenocarcinomata', 'bacteriophagies', 'adorablenesses', 'accommodators', 'abolitionary', 'abortionist', 'amylopsins', 'arrowworm', 'lustrous', 'zyzzyva']
print(sorted(words_ordered_len_sum(), key=lambda x: len(x))[-1])
