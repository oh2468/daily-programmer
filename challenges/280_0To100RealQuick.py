## https://old.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

values = [10, 10, 10, 10, 50, 5, 1, 1, 1, 1]

def is_valid(hand, pr=None):
    if len(hand) <= 1:
        return True
    elif pr == "1" and hand[0] == "0":
        return False
    else:
        return is_valid(hand, hand.pop(0))

def count(fingers):
    lh, rh = list(fingers[:5]), list(reversed(fingers[5:]))
    if not is_valid(lh) or not is_valid(rh):
        return None
    else:
        return sum(int(f) * v for f, v in zip(fingers, values))

assert count("0111011100") == 37
assert count("1010010000") == None
assert count("0011101110") == 73
assert count("0000110000") == 55
assert count("1111110001") == None
