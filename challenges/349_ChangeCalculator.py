## https://old.reddit.com/r/dailyprogrammer/comments/7ttiq5/20180129_challenge_349_easy_change_calculator/

from itertools import combinations


def sum_combs(s, c, n):
    for comb in combinations(c, n):
        if sum(comb) == s:
            return comb
    return None

def change(coin_input, con, n):
    inp = [int(c) for c in coin_input.split()]
    chng, coins = inp[0], inp[1::]

    if sum(coins) < chng:
        return None
    
    if con == "<":
        x, y = 1, n - 1
    else:
        x, y = n + 1, len(coins)

    while x <= y:
        if (comb := sum_combs(chng, coins, x)):
            return comb
        x += 1
    
    return None

# bonus challenge
def change_bonus(coin_input):
    inp = [int(c) for c in coin_input.split()]
    chng, coins = inp[0], inp[1::]

    if sum(coins) < chng:
        return None

    s = x = 0
    for c in coins:
        if s >= chng:
            break
        if c <= chng:
            s += c
            x += 1

    while x <= len(coins):
        if (comb := sum_combs(chng, coins, x)):
            return len(comb)
        x += 1

print(change("10 5 5 2 2 1", "<", 4))
print(change("150 100 50 50 50 50", "<", 6))
print(change("130 100 20 18 12 5 5", "<", 7))
print(change("200 50 50 20 20 10", ">", 4))

print(change_bonus("150" + (" 1" * 1000)))
