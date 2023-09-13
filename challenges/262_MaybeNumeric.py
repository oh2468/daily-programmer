## https://old.reddit.com/r/dailyprogrammer/comments/4eaeff/20160411_challenge_262_easy_maybenumeric/

def maybe_numeric(s):
    try:
        return int(s) if float(s).is_integer() else float(s)
    except ValueError:
        return s

assert maybe_numeric("123") == 123
assert maybe_numeric("44.234") == 44.234
assert maybe_numeric("0x123N") == "0x123N"
