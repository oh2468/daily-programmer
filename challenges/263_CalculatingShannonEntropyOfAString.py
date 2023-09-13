## https://old.reddit.com/r/dailyprogrammer/comments/4fc896/20160418_challenge_263_easy_calculating_shannon/

from collections import Counter
from math import log2


def shannon_entropy(s):
    return round(-1 * sum((x := (c / len(s))) * log2(x) for c in Counter(s).values()), 5)

assert shannon_entropy("1223334444") == 1.84644
assert shannon_entropy("Hello, world!") == 3.18083
assert shannon_entropy("122333444455555666666777777788888888") == round(2.794208683, 5)
assert shannon_entropy("563881467447538846567288767728553786") == round(2.794208683, 5)
assert shannon_entropy("https://www.reddit.com/r/dailyprogrammer") == round(4.056198332, 5)
assert shannon_entropy("int main(int argc, char *argv[])") == round(3.866729296, 5)
