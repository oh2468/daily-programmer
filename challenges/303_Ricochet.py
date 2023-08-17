## https://old.reddit.com/r/dailyprogrammer/comments/5vb1wf/20170221_challenge_303_easy_ricochet/

def bounce(h, w, v):
    hi = wi = 0
    corners = {(0, w): "UR", (h, w): "LR", (h, 0): "LL"}
    moves = 0
    grid_bounces = 0
    dir_h = dir_w = 1
    while (hi, wi) not in corners:
        moves += 1
        hi += dir_h
        wi += dir_w
        if hi == 0 or hi == h:
            dir_h = -dir_h
            grid_bounces += 1
        if wi == 0 or wi == w:
            dir_w = -dir_w
            grid_bounces += 1
    grid_bounces -= 2
    t = moves // v
    return f"{corners[(hi, wi)]} {grid_bounces} {t}"

assert bounce(8, 3, 1) == "LL 9 24"
assert bounce(15, 4, 2) == "UR 17 30"
