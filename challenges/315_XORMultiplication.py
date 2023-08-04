## https://old.reddit.com/r/dailyprogrammer/comments/6ba9id/20170515_challenge_315_easy_xor_multiplication/

def xor_mul(a, b):
    a, b = f"{a:b}", f"{b:b}"
    aand = lambda l: "1" if all(i == "1" for i in l) else "0"
    xxor = lambda l: "1" if l.count("1") % 2 != 0 else "0"
    m = []
    for i, n in enumerate(b, 1):
        m.append(("0" * (i - 1)) + "".join(map(aand, [(m, n) for m in a])) + ("0" * (len(b) - i)))
    s = "".join(map(xxor, zip(*m)))
    return f"{int(a, 2)}@{int(b, 2)}={int(s, 2)}"

assert xor_mul(1, 2) == "1@2=2"
assert xor_mul(9, 0) == "9@0=0"
assert xor_mul(6, 1) == "6@1=6"
assert xor_mul(3, 3) == "3@3=5"
assert xor_mul(2, 5) == "2@5=10"
assert xor_mul(7, 9) == "7@9=63"
assert xor_mul(13, 11) == "13@11=127"
assert xor_mul(5, 17) == "5@17=85"
assert xor_mul(14, 13) == "14@13=70"
assert xor_mul(19, 1) == "19@1=19"
assert xor_mul(63, 63) == "63@63=1365"
