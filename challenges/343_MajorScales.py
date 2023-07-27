## https://old.reddit.com/r/dailyprogrammer/comments/7hhyin/20171204_challenge_343_easy_major_scales/

chrom_scale = "C  C#  D  D#  E  F  F#  G  G#  A  A#  B".split()
solfege_names = {"Do": 0, "Re": 2, "Mi": 4, "Fa": 5, "So": 7, "La": 9, "Ti": 11}

def note(key, name):
    return chrom_scale[(chrom_scale.index(key) + solfege_names[name]) % len(chrom_scale)]

assert note("C", "Do") == "C"
assert note("C", "Re") == "D"
assert note("C", "Mi") == "E"
assert note("D", "Mi") == "F#"
assert note("A#", "Fa") == "D#"
