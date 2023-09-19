## https://old.reddit.com/r/dailyprogrammer/comments/46zm8m/20160222_challenge_255_easy_playing_with_light/

def num_lights_on(inp):
    lights = [False] * int(inp[0])
    for run in inp[1:]:
        a, b = sorted(map(int, run.split()))
        for i in range(a, b + 1):
            lights[i] = not lights[i]
    return sum(lights)

ex_input = """10
3 6
0 4
7 3
9 9""".splitlines()
ex_output = 7

ch_input = """1000
616 293
344 942
27 524
716 291
860 284
74 928
970 594
832 772
343 301
194 882
948 912
533 654
242 792
408 34
162 249
852 693
526 365
869 303
7 992
200 487
961 885
678 828
441 152
394 453""".splitlines()

assert num_lights_on(ex_input) == ex_output
print(num_lights_on(ch_input))
