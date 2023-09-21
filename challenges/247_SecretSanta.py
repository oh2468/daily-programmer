## https://old.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/

# from itertools import permutations, combinations, chain
import random


def pick_santas(people):
    groups = [g.split() for g in people]
    people = set([p for g in groups for p in g])
    santas = []
    while not santas:
        santas = []
        unpickable = {p: set(g) for g in groups for p in g}
        picked = set()
        for person, family in unpickable.items():
            try:
                pick = random.choice([p for p in people - family - picked])
            except IndexError:
                santas = []
                break
            santas.append((person, pick))
            picked.add(pick)
            unpickable[pick].add(person)
    print(santas)

input_1 = """Joe
Jeff Jerry
Johnson""".splitlines()

input_2 = """Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea""".splitlines()

pick_santas(input_1)
pick_santas(input_2)
