## https://old.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/

def active(hours):
    return len({h for d in hours for h in range(int(d.split()[0]), int(d.split()[1]))})

ex_inp = """1 3
2 3
4 5"""

ch_inp_1 = """2 4
3 6
1 3
6 8"""

ch_inp_2 = """6 8
5 8
8 9
5 7
4 7"""

bonus_inp = """15 18
13 16
9 12
3 4
17 20
9 11
17 18
4 5
5 6
4 5
5 6
13 16
2 3
15 17
13 14"""

assert active(ex_inp.split("\n")) == 3
assert active(ch_inp_1.split("\n")) == 7
assert active(ch_inp_2.split("\n")) == 5
print(active(bonus_inp.split("\n")))
