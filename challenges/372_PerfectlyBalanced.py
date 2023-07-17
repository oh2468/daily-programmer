## https://old.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

def balanced(string):
    return string.count("x") == string.count("y")

# bonus challenge
def balanced_bonus(string):
    return all(string.count(s) == string.count(string[0]) for s in string)

assert balanced("xxxyyy") == True
assert balanced("yyyxxx") == True
assert balanced("xxxyyyy") == False
assert balanced("yyxyxxyxxyyyyxxxyxyx") == True
assert balanced("xyxxxxyyyxyxxyxxyy") == False
assert balanced("") == True
assert balanced("x") == False

assert balanced_bonus("xxxyyyzzz") == True
assert balanced_bonus("abccbaabccba") == True
assert balanced_bonus("xxxyyyzzzz") == False
assert balanced_bonus("abcdefghijklmnopqrstuvwxyz") == True
assert balanced_bonus("pqq") == False
assert balanced_bonus("fdedfdeffeddefeeeefddf") == False
assert balanced_bonus("www") == True
assert balanced_bonus("x") == True
assert balanced_bonus("") == True
