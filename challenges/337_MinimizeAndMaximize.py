## https://old.reddit.com/r/dailyprogrammer/comments/784fgr/20171023_challenge_337_easy_minimize_maximize/

import math


def minimize(a, b, c):
    points = [(a ** 2 + p ** 2) ** 0.5 + (b ** 2 + (c - p) ** 2) ** 0.5 for p in range(0, c + 1)]
    return points.index(min(points))

def maximmize(l):
    radii = [l / (math.radians(i) + 2) for i in range(1, 181)]
    areas = [(r * (l - 2 * r)) / 2 for r in radii]
    max_r, max_a = max(zip(radii, areas), key=lambda x: x[1])
    return (max_a * 360) / (math.pi * max_r ** 2)

# challenge 1
print(maximmize(100))
# challenge 2
print(minimize(20, 30, 100))
