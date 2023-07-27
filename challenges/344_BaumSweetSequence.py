## https://old.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/

def generate_sequence(n):
    seq = [1]
    for i in range(1, n + 1):
        bin_i = f"{i:b}".split("1")
        has_odd = len([c for c in bin_i if len(c) % 2 == 1]) > 0
        seq.append(1 - has_odd)
    return seq
    
# code golf version
golf = lambda n: [1] + [1 - (len([c for c in f"{i:b}".split("1") if len(c) % 2 == 1]) > 0) for i in range(1, n + 1)]

assert generate_sequence(20) == [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
assert golf(20) == [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
x = 30
assert golf(x) == generate_sequence(x)
