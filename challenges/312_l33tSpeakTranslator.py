## https://old.reddit.com/r/dailyprogrammer/comments/67dxts/20170424_challenge_312_easy_l33tspeak_translator/

leet_map = {
    "A": "4", "B": "6", "E": "3", "I": "1",
    "L": "|", "M": "(V)", "N": "(\)", "O": "0", "S":
    "5", "T": "7", "V": "\/", "W": "`//"
}

norm_map = {v: k for k, v in leet_map.items()}

def translate(string, to_leet):
    if to_leet:
        # print("".join([leet_map.get(ch.upper(), ch) for ch in string.upper()]))
        return "".join([leet_map.get(ch.upper(), ch) for ch in string.upper()])
    else:
        string = string.upper()
        trans = ""
        x = 0
        for i in range(len(string)):
            if i < x: continue
            match = False
            for j in range(3, 0, -1):
                lt = norm_map.get(string[i:i + j], None)
                if lt:
                    trans += lt
                    x = i + j
                    match = True
                    break
            if not match:
                trans += string[i]
        # print(trans)
        return trans

assert translate("3|337", False) == "eleet".upper()
assert translate("storm", True) == "570R(V)".upper()

assert translate("I am elite.", True) == "1 4(V) 3|173.".upper()
assert translate("Da pain!", True) == "D4 P41(\)!".upper()
assert translate("Eye need help!", True) == "3Y3 (\)33D H3|P!".upper()
assert translate("3Y3 (\)33D H3|P!", False) == "eye need help!".upper()
assert translate("3Y3 (\)33d j00 t0 g37 d4 d0c70r.", False) == "Eye need joo to get da doctor.".upper()
assert translate("1 n33d m4 p1llz!", False) == "I need ma pillz!".upper()
