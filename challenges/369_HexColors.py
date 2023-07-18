## https://old.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/

def hexcolor(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}".upper()

# bonus challenge
def blend(colors):
    r = g = b = 0
    for color in colors:
        r += (int(color[1:3], 16) / len(colors))
        g += (int(color[3:5], 16) / len(colors))
        b += (int(color[5:7], 16) / len(colors))
    return hexcolor(round(r), round(g), round(b))

assert hexcolor(255, 99, 71) == "#FF6347" # (Tomato)
assert hexcolor(184, 134, 11) == "#B8860B" # (DarkGoldenrod)
assert hexcolor(189, 183, 107) == "#BDB76B" # (DarkKhaki)
assert hexcolor(0, 0, 205) == "#0000CD" # (MediumBlue)

assert blend(["#000000", "#778899"]) == "#3C444C"
assert blend(["#E6E6FA", "#FF69B4", "#B0C4DE"]) == "#DCB1D9"
