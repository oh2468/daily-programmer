## https://old.reddit.com/r/dailyprogrammer/comments/8xbxi9/20180709_challenge_365_easy_uparrow_notation/

def up_arrow(a, n, b):
    if n == 1:
        return a ** b
    elif n > 1 and b <= 0:
        return 1
    else:
        return up_arrow(a, n - 1, up_arrow(a, n, b - 1))

assert up_arrow(2, 1, 4) == 16
assert up_arrow(2, 2, 4) == 65536
assert up_arrow(2, 3, 3) == 65536

# print(up_arrow(5, 4, 5)) # too slow
# print(up_arrow(7, 5, 3)) # too slow
print(up_arrow(-1, 3, 3))
print(up_arrow(1, 1, 0))
print(up_arrow(1, 2, 0))
# print(up_arrow(12, 11, 25)) # too slow

"""
challenge input:
5 ↑↑↑↑ 5
7 ↑↑↑↑↑ 3
-1 ↑↑↑ 3
1 ↑ 0
1 ↑↑ 0
12 ↑↑↑↑↑↑↑↑↑↑↑ 25

callenge output:
x
x
-1
1
1
x
"""


