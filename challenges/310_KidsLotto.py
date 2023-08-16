## https://old.reddit.com/r/dailyprogrammer/comments/64jesw/20170410_challenge_310_easy_kids_lotto/

import random


def lotto(names, n):
    names = [name for name in names.split(";")]
    lotto_map = {}
    for student in names:
        excluded = [name for name in names if name != student]
        while True:
            row = tuple(sorted(random.sample(excluded, k=n)))
            if row not in lotto_map:
                lotto_map[row] = student
                break
    for row, student in lotto_map.items():
        print(f"{student}: {row}")

lotto("Rebbeca Gann;Latosha Caraveo;Jim Bench;Carmelina Biles;Oda Wilhite;Arletha Eason", 3)
lotto("Rebbeca Gann;Latosha Caraveo;Jim Bench;Carmelina Biles;Oda Wilhite;Arletha Eason;Theresa Kaczorowski;Jane Cover;Melissa Wise;Jaime Plascencia;Sacha Pontes;Tarah Mccubbin;Pei Rall;Dixie Rosenblatt;Rosana Tavera;Ethyl Kingsley;Lesia Westray;Vina Goodpasture;Drema Radke;Grace Merritt;Lashay Mendenhall;Magali Samms;Tiffaney Thiry;Rikki Buckelew;Iris Tait;Janette Huskins;Donovan Tabor;Jeremy Montilla;Sena Sapien;Jennell Stiefel", 15)
