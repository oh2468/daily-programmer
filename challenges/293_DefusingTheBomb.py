## https://old.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/

wires = {
    "white": "purple red green orange",
    "black": "black purple red",
    "purple": "black red",
    "red": "green",
    "green": "orange white",
    "orange": "red black"
}

def defuse(cuts):
    for i in range(len(cuts) - 1):
        if cuts[i + 1] not in wires[cuts[i]]:
            return "Boom"
    return "Bomb defused"

input_1 = """white
red
green
white""".split("\n")

input_2 = """white
orange
green
white""".split("\n")

assert defuse(input_1) == "Bomb defused"
assert defuse(input_2) == "Boom"
