## https://old.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

# with bonus
def spiral(n, c):
    t = n ** 2
    p, x, y = 1, -1 if c else -n, 1
    shifts = [0] * t
    down, right = c, not c

    while (t := t / 10) > 1:
        p += 1

    for _ in range(n):
        x += 1 if c else n
        shifts[x] = y
        y += 1

    for i in range(n - 1, 0, -1):
        if c:
            for _ in range(i):
                x += n if down else -n
                shifts[x] = y
                y += 1
            for _ in range(i):
                x += 1 if right else -1
                shifts[x] = y
                y += 1
        else:
            for _ in range(i):
                x += 1 if right else -1
                shifts[x] = y
                y += 1
            for _ in range(i):
                x += n if down else -n
                shifts[x] = y
                y += 1
        down = not down
        right = not right

    for i, s in enumerate(shifts, 1):
        print(f"{s}".rjust(p), end= " ")
        if i % n == 0:
            print()
    print()

spiral(5, True)
spiral(5, False)
spiral(4, True)
spiral(4, False)
