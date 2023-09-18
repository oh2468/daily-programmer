## https://old.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/

def calc_distance(ip):
    coord = lambda x: divmod("123456789.0".index(x), 3)
    dist = lambda x, y: ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    return f"{sum(dist(coord(ip[i]), coord(ip[i + 1])) for i in range(0, len(ip) - 1)):.2f}cm"

assert calc_distance("219.45.143.143") == "27.38cm"
