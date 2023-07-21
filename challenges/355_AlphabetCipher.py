## https://old.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/

alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha = {c: i for i, c in enumerate(alphabet)}

def encrypt(key, word):
    enc = ""
    for i, c in enumerate(word):
        ks = alpha[key[i % len(key)]]
        cs = alpha[c]
        nc = alphabet[(ks + cs) % len(alphabet)]
        enc += nc
    return enc

# bonus challenge
def decrypt(key, word):
    dec = ""
    for i, c in enumerate(word):
        ks = alpha[key[i % len(key)]]
        cs = alpha[c]
        nc = alphabet[(cs - ks) % len(alphabet)]
        dec += nc
    return dec

assert encrypt("bond", "theredfoxtrotsquietlyatmidnight") == "uvrufrsryherugdxjsgozogpjralhvg"
assert encrypt("train", "murderontheorientexpress") == "flrlrkfnbuxfrqrgkefckvsa"
assert encrypt("garden", "themolessnuckintothegardenlastnight") == "zhvpsyksjqypqiewsgnexdvqkncdwgtixkx"

# bonus challenge
assert decrypt("cloak", "klatrgafedvtssdwywcyty") == "iamtheprettiestunicorn"
assert decrypt("python", "pjphmfamhrcaifxifvvfmzwqtmyswst") == "alwayslookonthebrightsideoflife"
assert decrypt("moore", "rcfpsgfspiecbcc") == "foryoureyesonly"
