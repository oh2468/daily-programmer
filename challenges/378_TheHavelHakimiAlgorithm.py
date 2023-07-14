## https://old.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

def warmup1(lst):
    return [i for i in lst if i]

def warmup2(lst):
    return sorted(lst, reverse=True)

def warmup3(a, lst):
    return a > len(lst)

def warmup4(n, lst):
    return [l - 1 if i < n else l for i, l in enumerate(lst)]

def hh(lst):
    while True:
        lst = warmup1(lst)
        if not lst: return True
        lst = warmup2(lst)
        n = lst.pop(0)
        if warmup3(n, lst): return False
        lst = warmup4(n, lst)

assert warmup1([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) == [5, 3, 2, 6, 2, 7, 2, 5]
assert warmup1([4, 0, 0, 1, 3]) == [4, 1, 3]
assert warmup1([1, 2, 3]) == [1, 2, 3]
assert warmup1([0, 0, 0]) == []
assert warmup1([]) == []

assert warmup2([5, 1, 3, 4, 2]) == [5, 4, 3, 2, 1]
assert warmup2([0, 0, 0, 4, 0]) == [4, 0, 0, 0, 0]
assert warmup2([1]) == [1]
assert warmup2([]) == []

assert warmup3(7, [6, 5, 5, 3, 2, 2, 2]) == False
assert warmup3(5, [5, 5, 5, 5, 5]) == False
assert warmup3(5, [5, 5, 5, 5]) == True
assert warmup3(3, [1, 1]) == True
assert warmup3(1, []) == True
assert warmup3(0, []) == False

assert warmup4(4, [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 1]
assert warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]) == [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]
assert warmup4(1, [10, 10, 10]) == [9, 10, 10]
assert warmup4(3, [10, 10, 10]) == [9, 9, 9]
assert warmup4(1, [1]) == [0]

assert hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) == False
assert hh([4, 2, 0, 1, 5, 0]) == False
assert hh([3, 1, 2, 3, 1, 0]) == True
assert hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]) == True
assert hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]) == True
assert hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]) == False
assert hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]) == False
assert hh([2, 2, 0]) == False
assert hh([3, 2, 1]) == False
assert hh([1, 1]) == True
assert hh([1]) == False
assert hh([]) == True
