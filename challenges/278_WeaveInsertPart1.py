## https://old.reddit.com/r/dailyprogrammer/comments/4wqzph/20160808_challenge_278_easymed_weave_insert_part_1/

from itertools import chain, cycle


def ins_weave(l1, l2):
    return list(chain.from_iterable(zip(l2, cycle(l1))))[:-1]

def ins_bracket(l1, l2):
    pairs = [l2[i:i + 2] for i in range(0, len(l2), 2)]
    if len(l1) < len(l2) / 2:
        l1 = cycle(l1)
    else:
        pairs = cycle(pairs)
    return [f"{p[0]}{it}{p[1]}" for it, p in zip(l1, pairs)]

assert ins_weave([11], [0, 1, 2, 3]) == [0, 11, 1, 11, 2, 11, 3]
assert ins_weave([11, 12], [0, 1, 2, 3]) == [0, 11, 1, 12, 2, 11, 3]
assert ins_weave([11, 12, 13], [0, 1]) == [0, 11, 1]
assert ins_weave([11, 12, 13], []) == []
assert ins_bracket ('abc', '()') == ["(a)", "(b)", "(c)"]
assert ins_bracket("+-", "234567") == ["2+3", "4-5" ,"6+7"]
assert ins_bracket(["2+3", "4-5" ,"6+7"], "()") == ["(2+3)", "(4-5)", "(6+7)"]
assert ins_weave("*", ["(2+3)", "(4-5)", "(6+7)"]) == ["(2+3)", "*", "(4-5)", "*", "(6+7)"]
