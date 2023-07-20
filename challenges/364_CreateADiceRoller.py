## https://old.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/

import random


def roll(ndm):
    n, m = int((x := ndm.split("d"))[0]), int(x[1])
    return sum(random.randint(1, m) for _ in range(n))

# bonus challenge
def roll_b(ndm):
    n, m = int((x := ndm.split("d"))[0]), int(x[1])
    rolls = [random.randint(1, m) for _ in range(n)]
    print(f"{sum(rolls)}:", end=" ")
    for r in rolls:
        print(r, end=" ")
    print()

# challenge input
print(roll("5d12"))
print(roll("6d4"))
print(roll("1d2"))
print(roll("1d8"))
print(roll("3d6"))
print(roll("4d20"))
print(roll("100d100"))

roll_b("5d12")
roll_b("6d4")
roll_b("1d2")
roll_b("1d8")
roll_b("3d6")
roll_b("4d20")
roll_b("100d100")
roll_b("3d6")
roll_b("4d12")
roll_b("1d10")
roll_b("5d4")
