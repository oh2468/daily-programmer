## https://old.reddit.com/r/dailyprogrammer/comments/ab9mn7/20181231_challenge_371_easy_n_queens_validator/

def qcheck(queens):
    if len(set(queens)) != len(queens): return False
    
    n = len(queens)
    get_pos = lambda q, c, r: (c * q) + r if 0 <= c < q and 0 <= r < q else -1
    q_pos = {get_pos(n, i, q - 1) for i, q in enumerate(queens)}

    for c, q in enumerate(queens):
        q -= 1
        for r in range(n):
            ru = q - r - 1
            rd = q + r + 1
            cl = c - r - 1
            cr = c + r + 1
            if get_pos(n, cl, ru) in q_pos: return False
            if get_pos(n, cl, rd) in q_pos: return False
            if get_pos(n, cr, ru) in q_pos: return False
            if get_pos(n, cr, rd) in q_pos: return False
    return True

# bonus challenge
def qfix(queens):
    if qcheck(queens):
        return queens

    for i, q1 in enumerate(queens):
        for j in range(i + 1, len(queens)):
            q2 = queens[j]
            queens[i] = q2
            queens[j] = q1
            if qcheck(queens):
                return queens
            queens[i] = q1
            queens[j] = q2
    
    return []

assert qcheck([4, 2, 7, 3, 6, 8, 5, 1]) == True
assert qcheck([2, 5, 7, 4, 1, 8, 6, 3]) == True
assert qcheck([5, 3, 1, 4, 2, 8, 6, 3]) == False # (b3 and h3 are on the same row)
assert qcheck([5, 8, 2, 4, 7, 1, 3, 6]) == False # (b8 and g3 are on the same diagonal)
assert qcheck([4, 3, 1, 8, 1, 3, 5, 2]) == False # (multiple problems)

assert qfix([8, 6, 4, 2, 7, 1, 3, 5]) == [4, 6, 8, 2, 7, 1, 3, 5]
assert qfix([8, 5, 1, 3, 6, 2, 7, 4]) == [8, 4, 1, 3, 6, 2, 7, 5]
assert qfix([4, 6, 8, 3, 1, 2, 5, 7]) == [4, 6, 8, 3, 1, 7, 5, 2]
assert qfix([7, 1, 3, 6, 8, 5, 2, 4]) == [7, 3, 1, 6, 8, 5, 2, 4]
