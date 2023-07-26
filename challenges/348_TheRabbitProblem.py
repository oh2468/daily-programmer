## https://old.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/

from collections import deque


def rabbit_time(m, f, r):
    life_ex = 96
    rabbits = deque([(0, 0)] * life_ex)
    rabbits[2] = (m, f)
    m_birth, f_birth = 5, 9
    total_r = m + f
    dead_r = (0, 0)
    months = fert_f = 0

    while total_r < r:
        months += 1
        dead_m, dead_f = rabbits.pop()
        dead_r = (dead_r[0] + dead_m, dead_r[1] + dead_f)
        fert_f -= dead_f
        new_r = (fert_f * m_birth, fert_f * f_birth)
        rabbits.appendleft(new_r)
        fert_f += rabbits[4][1]
        total_r += (sum(new_r) - sum(dead_r))
    
    print(f"dead rabbits (m, f): {dead_r}, tot: {sum(dead_r)}")
    return months

assert rabbit_time(2, 4, 1000000000) == 32
assert rabbit_time(2, 4, 15000000000) == 36
