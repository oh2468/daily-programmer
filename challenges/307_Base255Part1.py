## https://old.reddit.com/r/dailyprogrammer/comments/60ibay/20170320_challenge_307_easy_base_255_part1/

# part 1
def encode_1(lines):
    return "+,".join(line.replace("+", "++") for line in lines.split())

def decode_1(line):
    return "\n".join(line.replace("++", "+") for line in line.split("+,"))

# part 2
def encode_2(lines):
    s, c = [], 0
    add_ps = lambda c: "9" + add_ps(c - 9) if c > 9 else f"{c}"
    for line in lines.split():
        t = ""
        for ch in line:
            if ch == "+":
                c += 1
            else:
                if c > 0:
                    t += "+" + add_ps(c)
                    c = 0
                t += ch
        if c > 0:
            t += "+" + add_ps(c)
            c = 0
        s.append(t)
    return "+0".join(s)

def decode_2(line):
    s, c, count = [], 0, False
    for part in line.split("+0"):
        t = ""
        for ch in part:
            if ch == "+":
                count = True
            elif count:
                if ch.isdigit():
                    c += int(ch)
                else:
                    if c % 9 != 0:
                        count = False
                    t += ("+" * c) + ch
                    c = 0
            else:
                t += ch
        if c > 0 :
            t += "+" * c
            c = 0
        s.append(t)
    return "\n".join(s)

enc_input = """abc+def
ghij
klmno++p+"""

dec_input = "abc++def+,ghij+,klmno++++p++"

dec_input_2 = "abc+1def+0ghij+0klmno+2p+1"

assert encode_1(enc_input) == dec_input
assert decode_1(dec_input) == enc_input

assert encode_2(enc_input) == dec_input_2
assert decode_2(dec_input_2) == enc_input
