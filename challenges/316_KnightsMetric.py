## https://old.reddit.com/r/dailyprogrammer/comments/6coqwk/20170522_challenge_316_easy_knights_metric/

moves = [(-1,-2), (1,-2), (-1, 2), (1, 2), (-2,-1), (2,-1), (-2, 1), (2, 1)]

def count_moves(x, y):
    moves_made = [[(0, 0)]]
    while True:
        mvs = moves_made.pop(0)
        pos = mvs[0]
        if pos == (x, y):
            print(f"moves: {mvs[1:]}")
            return len(mvs) - 1
        for move in moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            path = [new_pos] + mvs[1:] + [move]
            if len(mvs) < 2:
                moves_made.append(path)
            elif new_pos != mvs[-2]:
                moves_made.append(path)

print(count_moves(0, 1))
print(count_moves(3, 7))
print(count_moves(1, 1))
