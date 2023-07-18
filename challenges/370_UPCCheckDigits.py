## https://old.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/

def upc(code):
    return (10 - sum(int(c) if i % 2 else int(c) * 3 for i, c in enumerate(code))) % 10

#bonus challenge
def upc_b(code):
    return upc(f"{code:011d}")

assert upc("03600029145") == 2
assert upc("04210000526") == 4
assert upc("03600029145") == 2
assert upc("12345678910") == 4
assert upc("00001234567") == 0

assert upc_b(4210000526) == 4
assert upc_b(3600029145) == 2
assert upc_b(12345678910) == 4
assert upc_b(1234567) == 0
