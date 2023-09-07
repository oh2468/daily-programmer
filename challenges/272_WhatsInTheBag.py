## https://old.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

from collections import Counter, defaultdict


CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
TILES = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]

def left_in_bag(used):
    tile_count = Counter({c: t for c, t in zip(CHARS, TILES)})
    tile_count.subtract(used)
    too_many_used = [f"{k}'s" for k, v in tile_count.items() if v < 0]
    
    if too_many_used:
        return f"Invalid input. More {', '.join(too_many_used)} have been taken from the bag than possible."
    
    left = sorted(tile_count.items(), key=lambda i: (-i[1], i[0]))
    left_map = defaultdict(list)
    for l, c in left:
        left_map[c].append(l)
    return dict(left_map)

inp_1 = "AEERTYOXMCNB_S"
out_1 = {
    10: ["E"], 9: ["I"], 8: ["A"], 7: ["O"],
    5: ["N", "R", "T"], 4: ["D", "L", "U"], 3: ["G", "S"],
    2: ["F", "H", "P", "V", "W"],
    1:[ "B", "C", "J", "K", "M", "Q", "Y", "Z", "_"], 0: ["X"],
}

cha_inp_1 = "PQAREIOURSTHGWIOAE_"
cha_out_1 = {
    10: ["E"], 7: ["A", "I"], 6: ["N", "O"],
    5: ["T"], 4: ["D", "L", "R"], 3: ["S", "U"],
    2: ["B", "C", "F", "G", "M", "V", "Y"],
    1: ["H", "J", "K", "P", "W", "X", "Z", "_"], 0: ["Q"],
}

cha_inp_2 = "LQTOONOEFFJZT"
cha_out_2 = {
    11: ['E'], 9: ['A', 'I'], 6: ['R'],
    5: ['N', 'O'], 4: ['D', 'S', 'T', 'U'],
    3: ['G', 'L'], 2: ['B', 'C', 'H', 'M', 'P', 'V', 'W', 'Y', '_'],
    1: ['K', 'X'], 0: ['F', 'J', 'Q', 'Z'],
}

cha_inp_3 = "AXHDRUIOR_XHJZUQEE"
cha_out_3 = "Invalid input. More X's have been taken from the bag than possible."

assert left_in_bag(inp_1) == out_1
assert left_in_bag(cha_inp_1) == cha_out_1
assert left_in_bag(cha_inp_2) == cha_out_2
assert left_in_bag(cha_inp_3) == cha_out_3
