## https://old.reddit.com/r/dailyprogrammer/comments/7p5p2o/20180108_challenge_346_easy_cryptarithmetic_solver/

from itertools import permutations
import time


def solve_cryptarithm(cr_ar):
    eq, su = (x := cr_ar.split(" == "))[0], x[1]
    eq = eq.split(" + ")
    chars = {c for c in cr_ar if c.isalpha()}
    starters = {su[0]} | {t[0] for t in eq}
    word_to_int = lambda w, m: sum(m[c] * (10 ** (len(w) - i - 1)) for i, c in enumerate(w))
    sol = None

    s1 = time.time()
    for perm in permutations(i for i in range(0,10)):
        char_map = dict(zip(chars, perm))
        skip = False
        for st in starters:
            if char_map[st] == 0:
                skip = True
                break
        if skip:
            continue

        test_su = word_to_int(su, char_map)
        test_eq = 0

        if test_su % 10 != sum(char_map[t[-1]] for t in eq) % 10:
            continue
        
        for t in eq:
            test_eq += word_to_int(t, char_map)
            if test_eq > test_su:
                break
        if test_eq == test_su:
            sol = char_map
            break
    
    s2 = time.time()
    print(f"it took: {s2 - s1}s to solve:")
    print(f"{cr_ar}")
    return dict(sorted(sol.items(), key=lambda it: it[1]))

assert solve_cryptarithm("SEND + MORE == MONEY") == {"O": 0, "M": 1, "Y": 2, "E": 5, "N": 6, "D": 7, "R": 8, "S": 9}
assert solve_cryptarithm("THIS + IS + HIS == CLAIM") ==  {"A": 7, "C": 1, "H": 8, "I": 5, "L": 0, "M": 6, "S": 2, "T": 9}
assert solve_cryptarithm("WHAT + WAS + THY == CAUSE") == {"A": 0, "C": 1, "E": 4, "H": 2, "S": 3, "T": 6, "U": 7, "W": 9, "Y": 5}
assert solve_cryptarithm("HIS + HORSE + IS == SLAIN") == {"A": 1, "E": 8, "H": 3, "I": 5, "L": 0, "N": 6, "O": 9, "R": 7, "S": 4}
print(solve_cryptarithm("HERE + SHE == COMES")) # answer: {'R': 5, 'S': 8, 'C': 1, 'H': 9, 'M': 3, 'E': 4, 'O': 0}
assert solve_cryptarithm("FOR + LACK + OF == TREAD") == {"A": 6, "C": 7, "D": 3, "E": 2, "F": 5, "K": 8, "L": 9, "O": 4, "R": 0, "T": 1}
assert solve_cryptarithm("I + WILL + PAY + THE == THEFT") == {"A": 2, "E": 4, "F": 7, "H": 0, "I": 8, "L": 3, "P": 5, "T": 1, "W": 9, "Y": 6}

# bonus challenges
# bonus 1 - answer: {'O': 1, 'E': 0, 'N': 6, 'S': 3, 'R': 8, 'Y': 4, 'T': 9, 'M': 2, 'H': 5, 'A': 7}
# bonus 2 - answer: {'S': 3, 'M': 2, 'N': 6, 'A': 7, 'R': 8, 'Y': 4, 'H': 5, 'T': 9, 'O': 1, 'E': 0}
# bonus 3 - answer: {'H': 8, 'F': 5, 'S': 4, 'E': 0, 'A': 1, 'O': 6, 'I': 7, 'T': 9, 'L': 2, 'R': 3}
print(solve_cryptarithm("TEN + HERONS + REST + NEAR + NORTH + SEA + SHORE + AS + TAN + TERNS + SOAR + TO + ENTER + THERE + AS + HERONS + NEST + ON + STONES + AT + SHORE + THREE + STARS + ARE + SEEN + TERN + SNORES + ARE + NEAR == SEVVOTH"))
print(solve_cryptarithm("SO + MANY + MORE + MEN + SEEM + TO + SAY + THAT + THEY + MAY + SOON + TRY + TO + STAY + AT + HOME + SO + AS + TO + SEE + OR + HEAR + THE + SAME + ONE + MAN + TRY + TO + MEET + THE + TEAM + ON + THE + MOON + AS + HE + HAS + AT + THE + OTHER + TEN == TESTS"))
print(solve_cryptarithm("THIS + A + FIRE + THEREFORE + FOR + ALL + HISTORIES + I + TELL + A + TALE + THAT + FALSIFIES + ITS + TITLE + TIS + A + LIE + THE + TALE + OF + THE + LAST + FIRE + HORSES + LATE + AFTER + THE + FIRST + FATHERS + FORESEE + THE + HORRORS + THE + LAST + FREE + TROLL + TERRIFIES + THE + HORSES + OF + FIRE + THE + TROLL + RESTS + AT + THE + HOLE + OF + LOSSES + IT + IS + THERE + THAT + SHE + STORES + ROLES + OF + LEATHERS + AFTER + SHE + SATISFIES + HER + HATE + OFF + THOSE + FEARS + A + TASTE + RISES + AS + SHE + HEARS + THE + LEAST + FAR + HORSE + THOSE + FAST + HORSES + THAT + FIRST + HEAR + THE + TROLL + FLEE + OFF + TO + THE + FOREST + THE + HORSES + THAT + ALERTS + RAISE + THE + STARES + OF + THE + OTHERS + AS + THE + TROLL + ASSAILS + AT + THE + TOTAL + SHIFT + HER + TEETH + TEAR + HOOF + OFF + TORSO + AS + THE + LAST + HORSE + FORFEITS + ITS + LIFE + THE + FIRST + FATHERS + HEAR + OF + THE + HORRORS + THEIR + FEARS + THAT + THE + FIRES + FOR + THEIR + FEASTS + ARREST + AS + THE + FIRST + FATHERS + RESETTLE + THE + LAST + OF + THE + FIRE + HORSES + THE + LAST + TROLL + HARASSES + THE + FOREST + HEART + FREE + AT + LAST + OF + THE + LAST + TROLL + ALL + OFFER + THEIR + FIRE + HEAT + TO + THE + ASSISTERS + FAR + OFF + THE + TROLL + FASTS + ITS + LIFE + SHORTER + AS + STARS + RISE + THE + HORSES + REST + SAFE + AFTER + ALL + SHARE + HOT + FISH + AS + THEIR + AFFILIATES + TAILOR + A + ROOFS + FOR + THEIR + SAFE == FORTRESSES"))
