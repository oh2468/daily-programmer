## https://old.reddit.com/r/dailyprogrammer/comments/43ouxy/20160201_challenge_252_easy_sailors_and_monkeys/

def coconuts(n):
    start = 0
    found = False
    while not found:
        start += n
        s = start
        found = True
        for i in range(n):
            s = s * (n / (n - 1)) + 1
            if not float.is_integer(s):
                found = False
                break
    return s

assert coconuts(5) == 3121
