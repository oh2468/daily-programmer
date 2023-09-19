## https://old.reddit.com/r/dailyprogrammer/comments/45w6ad/20160216_challenge_254_easy_atbash_cipher/

# with bonus challenge
def encode(text):
    return "".join(chr((219 if c.islower() else 155) - ord(c)) if c.isalpha() else c for c in text)

assert encode("foobar") == "ullyzi"
assert encode("wizard") == "draziw"
assert encode("/r/dailyprogrammer") == "/i/wzrobkiltiznnvi"
assert encode("gsrh rh zm vcznkov lu gsv zgyzhs xrksvi") == "this is an example of the atbash cipher"
assert encode("FooBar") == "UllYzi"
assert encode("WiZaRd") == "DrAzIw"
