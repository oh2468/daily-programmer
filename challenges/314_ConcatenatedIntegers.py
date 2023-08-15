## https://old.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/

from itertools import permutations
from functools import cmp_to_key


# quick fix
def find_min_max_1(line):
    nums = line.split()
    min = None
    max = 0
    for p in permutations(nums):
        i = int("".join(p))
        if min is None:
            min = i
        elif i < min:
            min = i
        elif i > max:
            max = i
    return f"{min} {max}"

# bonus solution
def comparator(a, b):
    if len(a) == len(b):
        return -1 if a < b else (0 if a == b else 1)
    elif len(a) < len(b):
        if a == b[:len(a)]:
            return -1 if a <= b[len(a):] else 1
        elif a < b[:len(a)]:
            return -1
        else:
            return 1
    else:
        if a[:len(b)] == b:
            return -1 if a[len(b):] <= b else 1
        elif a[:len(b)] < b:
            return -1
        else:
            return 1

def find_min_max_2(line):
    nums = line.split()
    min = "".join(sorted(nums, key=cmp_to_key(comparator)))
    max = "".join(sorted(nums, key=cmp_to_key(comparator), reverse=True))
    return f"{min} {max}"

assert find_min_max_1("5 56 50") == "50556 56550"
assert find_min_max_1("79 82 34 83 69") == "3469798283 8382796934"
assert find_min_max_1("420 34 19 71 341") == "193413442071 714203434119"
assert find_min_max_1("17 32 91 7 46") == "173246791 917463217"

assert find_min_max_2("5 56 50") == "50556 56550"
assert find_min_max_2("79 82 34 83 69") == "3469798283 8382796934"
assert find_min_max_2("420 34 19 71 341") == "193413442071 714203434119"
assert find_min_max_2("17 32 91 7 46") == "173246791 917463217"
