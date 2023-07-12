## https://old.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/

import random


doors = [True, False, False]
picks = [0, 1 ,2]


def monty(p):
    # random.shuffle(doors)
    empty_doors = [i for i, w in enumerate(doors) if not w and i != p]
    open = random.choice(empty_doors)
    return open

def alice():
    pick = 0
    # _ = monty(pick) # no need to open a door, always sticking with first pick
    return doors[pick]

def bob():
    pick = 1
    open = monty(pick)
    changed_pick = 2 - open
    return doors[changed_pick]

def carol():
    pick = random.choice(picks)
    open = monty(pick)
    changed_pick = random.choice([p for p in picks if p != open])
    return doors[changed_pick]

def dave():
    pick = random.choice(picks)
    # _ = monty(pick) # no need to open a door, always sticking with first pick
    return doors[pick]

def erin():
    pick = random.choice(picks)
    open = monty(pick)
    changed_pick = [p for p in picks if p != open and p != pick][0]
    return doors[changed_pick]

def frank():
    pick = 0
    open = monty(pick)
    changed_pick = 1 if open != 1 else pick
    return doors[changed_pick]

def gina(a_s):
    return alice() if a_s else bob()

def play(r):
    a_wins = b_wins = c_wins = d_wins = e_wins = f_wins = g_wins = 0
    g_a_s = True

    for _ in range(r):
        random.shuffle(doors)
        a_wins += alice()
        b_wins += bob()
        c_wins += carol()
        d_wins += dave()
        e_wins += erin()
        f_wins += frank()

        g_win = gina(g_a_s)
        g_a_s = g_a_s if g_win else not g_a_s
        g_wins += g_win
    
    print(f"alice - wins: {a_wins}, f: {a_wins / r}")
    print(f"bob - wins: {b_wins}, f: {b_wins / r}")
    print(f"carol - wins: {c_wins}, f: {c_wins / r}")
    print(f"dave - wins: {d_wins}, f: {d_wins / r}")
    print(f"erin - wins: {e_wins}, f: {e_wins / r}")
    print(f"frank - wins: {f_wins}, f: {f_wins / r}")
    print(f"gina - wins: {g_wins}, f: {g_wins / r}")

# rounds = int(input("rounds: "))
# play(rounds)
play(1000)
