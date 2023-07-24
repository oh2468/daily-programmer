## https://old.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(n):
    s = ""
    while n > 0:
        s += alphabet[n % len(alphabet)]
        n //= len(alphabet)
    return s

assert convert(15674) == "O44"
assert convert(7026425611433322325) == "bDcRfbr63n8"

assert convert(187621) == "9OM"
assert convert(237860461) == "3n26g"
assert convert(2187521) == "B4b9"
assert convert(18752) == "sS4"
