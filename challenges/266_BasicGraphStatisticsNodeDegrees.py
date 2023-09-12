## https://old.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/

from collections import Counter
from itertools import chain


def node_degrees(edges):
    node_degrees = sorted(Counter(chain(*[e.split() for e in edges])).items(), key=lambda x: int(x[0]))
    print("\n".join(f"Node {n} has a degree of {d}" for n, d in node_degrees))
    return "\n".join(f"Node {n} has a degree of {d}" for n, d in node_degrees)

# bonus challenge
def adjascency_matrix(edges):
    edges = [tuple(map(int, e.split())) for e in edges]
    nodes = max(edges)[1]
    matrix = [[0] * nodes for _ in range(nodes)]
    for n1, n2 in edges:
        matrix[n1 - 1][n2 - 1] = 1
        matrix[n2 -1][n1 - 1] = 1
    for row in matrix:
        print(*row)

des_inp = """1 2
1 3"""
des_out = """Node 1 has a degree of 2
Node 2 has a degree of 1
Node 3 has a degree of 1"""

cha_inp = """1 2
1 3
2 3
1 4
3 4
1 5
2 5
1 6
2 6
3 6
3 7
5 7
6 7
3 8
4 8
6 8
7 8
2 9
5 9
6 9
2 10
9 10
6 11
7 11
8 11
9 11
10 11
1 12
6 12
7 12
8 12
11 12
6 13
7 13
9 13
10 13
11 13
5 14
8 14
12 14
13 14
1 15
2 15
5 15
9 15
10 15
11 15
12 15
13 15
1 16
2 16
5 16
6 16
11 16
12 16
13 16
14 16
15 16"""
cha_out = """Node 1 has a degree of 8
Node 2 has a degree of 8
Node 3 has a degree of 6
Node 4 has a degree of 3
Node 5 has a degree of 7
Node 6 has a degree of 10
Node 7 has a degree of 7
Node 8 has a degree of 7
Node 9 has a degree of 7
Node 10 has a degree of 5
Node 11 has a degree of 9
Node 12 has a degree of 8
Node 13 has a degree of 8
Node 14 has a degree of 5
Node 15 has a degree of 9
Node 16 has a degree of 9"""

assert node_degrees(des_inp.split("\n")) == des_out
assert node_degrees(cha_inp.split("\n")) == cha_out

adjascency_matrix(cha_inp.split("\n"))
