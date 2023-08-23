## https://old.reddit.com/r/dailyprogrammer/comments/5bn0b7/20161107_challenge_291_easy_goldilocks_bear/

def possible_seats(lines):
    lines = [(int((c := l.split())[0]), int(c[1])) for l in lines]
    mw, mh = lines[0]
    return [i for i, (w, h) in enumerate(lines[1:], 1) if w >= mw and h <= mh]

sam_inp = """100 80
30 50
130 75
90 60
150 85
120 70
200 200
110 100""".split("\n")

cha_inp = """100 120
297 90
66 110
257 113
276 191
280 129
219 163
254 193
86 153
206 147
71 137
104 40
238 127
52 146
129 197
144 59
157 124
210 59
11 54
268 119
261 121
12 189
186 108
174 21
77 18
54 90
174 52
16 129
59 181
290 123
248 132""".split("\n")

assert possible_seats(sam_inp) == [2, 5]
print(possible_seats(cha_inp))
