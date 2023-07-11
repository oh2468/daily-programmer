## https://old.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

coins = [500, 100, 25, 10, 5, 1]

def change(s):
    if s <= 0:
        return 0
    else:
        for c in coins:
            if (n := s - c) >= 0:
                return 1 + change(n)

assert change(0) == 0
assert change(12) == 3
assert change(468) == 11
assert change(123456) == 254
