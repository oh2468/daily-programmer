## https://old.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/

from urllib import request

def check(word):
    return word.count("ei") == word.count("cei") and "cie" not in word

# bonus challenges
# bonus 1 - answer: 2169
def check_b1():
    try:
        with open("resources/enable1.txt", "r", encoding="UTF-8") as file:
            words = file.read().split("\n")
    except FileNotFoundError:
        words = str(request.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").read(), "UTF-8").split("\n")

    return len([word for word in words if not check(word)])


assert check("a") == True
assert check("zombie") == True
assert check("transceiver") == True
assert check("veil") == False
assert check("icier") == False

total = check_b1()
print(total)
assert sum(int(s) for s in str(total)) == 18
