## https://old.reddit.com/r/dailyprogrammer/comments/6qutez/20170801_challenge_325_easy_color_maze/

def escape_maze(seq, maze):
    seq = seq.split()
    maze = [m.split() for m in maze.split("\n")][::-1]
    starters = [(l, 0, i) for i, l in enumerate(maze[0]) if l == seq[0]]
    m_v, m_h = len(maze) - 1, len(maze[0]) - 1
    for s in starters:
        paths = [[s]]
        while paths:
            path = paths.pop(0)
            p = path[-1]
            i, j = p[1], p[2]
            ch = seq[len(path) % len(seq)]

            if i == (m_v):
                return path
            if i < m_v and maze[i + 1][j] == ch:
                paths.append(path + [(ch, i + 1, j)])
            if i > 0 and maze[i - 1][j] == ch:
                paths.append(path + [(ch, i - 1, j)])
            if j > 0 and maze[i][j - 1] == ch:
                paths.append(path + [(ch, i, j - 1)])
            if j < m_h and maze[i][j + 1] == ch:
                paths.append(path + [(ch, i, j + 1)])

ex_seq = "O G"
ex_maze = """B O R O Y
O R B G R
B O G O Y
Y G B Y G
R O R B R"""

ch_seq = "R O Y P O"
ch_maze = """R R B R R R B P Y G P B B B G P B P P R
B G Y P R P Y Y O R Y P P Y Y R R R P P
B P G R O P Y G R Y Y G P O R Y P B O O
R B B O R P Y O O Y R P B R G R B G P G
R P Y G G G P Y P Y O G B O R Y P B Y O
O R B G B Y B P G R P Y R O G Y G Y R P
B G O O O G B B R O Y Y Y Y P B Y Y G G
P P G B O P Y G B R O G B G R O Y R B R
Y Y P P R B Y B P O O G P Y R P P Y R Y
P O O B B B G O Y G O P B G Y R R Y R B
P P Y R B O O R O R Y B G B G O O P B Y
B B R G Y G P Y G P R R P Y G O O Y R R
O G R Y B P Y O P B R Y B G P G O O B P
R Y G P G G O R Y O O G R G P P Y P B G
P Y P R O O R O Y R P O R Y P Y B B Y R
O Y P G R P R G P O B B R B O B Y Y B P
B Y Y P O Y O Y O R B R G G Y G R G Y G
Y B Y Y G B R R O B O P P O B O R R R P
P O O O P Y G G Y P O G P O B G P R P B
R B B R R R R B B B Y O B G P G G O O Y"""

"""answer (from bottom, from left): [('O', 0, 1), ('G', 1, 1), ('O', 2, 1), ('G', 2, 2), ('O', 2, 3), ('G', 3, 3), ('O', 4, 3)]"""
print(escape_maze(ex_seq, ex_maze))
"""answer (from bottom, from left): [('R', 0, 3), ('O', 1, 3), ('Y', 2, 3), ('P', 3, 3), ('O', 3, 4), ('R', 4, 4), ('O', 3, 4), ('Y', 3, 5), 
('P', 4, 5), ('O', 5, 5), ('R', 5, 6), ('O', 6, 6), ('Y', 7, 6), ('P', 8, 6), ('O', 9, 6), ('R', 9, 7), 
('O', 10, 7), ('Y', 10, 8), ('P', 11, 8), ('O', 11, 9), ('R', 12, 9), ('O', 13, 9), ('Y', 13, 10), ('P', 14, 10), 
('O', 15, 10), ('R', 16, 10), ('O', 15, 10), ('Y', 15, 9), ('P', 15, 8), ('O', 16, 8), ('R', 17, 8), ('O', 18, 8), 
('Y', 19, 8)]"""
print(escape_maze(ch_seq, ch_maze))
