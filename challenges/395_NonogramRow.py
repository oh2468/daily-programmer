## https://old.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/

def nonogramrow(lst):
    groups = []
    count = 0
    for n in lst:
        if not n and count:
            groups.append(count)
            count = 0
        elif n:
            count += 1
    if count:
        groups.append(count)
    return groups

assert nonogramrow([]) == []
assert nonogramrow([0,0,0,0,0]) == []
assert nonogramrow([1,1,1,1,1]) == [5]
assert nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) == [5,4]
assert nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) == [2,1,3]
assert nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) == [2,1,3]
assert nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) == [1,1,1,1,1,1,1,1]
