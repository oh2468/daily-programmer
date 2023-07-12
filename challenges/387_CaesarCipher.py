## https://old.reddit.com/r/dailyprogrammer/comments/myx3wn/20210426_challenge_387_easy_caesar_cipher/

chars = "abcdefghijklmnopqrstuvwxyz"

def caesar(string, shift):
    return "".join([chars[((ord(c) - ord(chars[0]) + shift) % len(chars))] for c in string])

# bonus 1
u_chars = chars.upper()
def caesar_b1(string, shift):
    make_shift = lambda a, c, s: a[((ord(c) - ord(a[0]) + s) % len(a))]
    return "".join([make_shift(chars if c.islower() else u_chars, c, shift) if c.isalpha() else c for c in string])
    # a little more readable version of the list comprehension
    # cipher = ""
    # for c in string:
    #     if c.isalpha():
    #         cipher += make_shift(chars if c.islower() else u_chars, c, shift)
    #     else:
    #         cipher += c
    # return cipher

# bonus 2
# answer 1: She turned me into a newt.
# answer 2: Come no further, for death awaits you all with nasty, big, pointy teeth.
# answer 3: In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right?
scores = [3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7]

def caesar_b2(string):
    all_shifts = [caesar_b1(string, i) for i in range(len(chars))]
    count_score = lambda s: sum(scores[ord(c) - ord(chars[0])] for c in s.lower() if c.isalpha())
    max_score = max((count_score(s), i) for i, s in enumerate(all_shifts))
    return all_shifts[max_score[1]]


assert caesar("a", 1) == "b"
assert caesar("abcz", 1) == "bcda"
assert caesar("irk", 13) == "vex"
assert caesar("fusion", 6) == "layout"
assert caesar("dailyprogrammer", 6) == "jgorevxumxgsskx"
assert caesar("jgorevxumxgsskx", 20) == "dailyprogrammer"

assert caesar_b1("a", 1) == "b"
assert caesar_b1("abcz", 1) == "bcda"
assert caesar_b1("irk", 13) == "vex"
assert caesar_b1("fusion", 6) == "layout"
assert caesar_b1("dailyprogrammer", 6) == "jgorevxumxgsskx"
assert caesar_b1("jgorevxumxgsskx", 20) == "dailyprogrammer"
assert caesar_b1("Daily Programmer!", 6) == "Jgore Vxumxgsskx!"

print(caesar_b2("Zol abyulk tl puav h ulda."))
print(caesar_b2("Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky."))
print(caesar_b2("Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?"))
