## https://old.reddit.com/r/dailyprogrammer/comments/4q35ip/20160627_challenge_273_easy_getting_a_degree/

from math import pi


def convert(data):
    num, a, b = float(data[:-2]), data[-2], data[-1]
    return f"{round((num * pi) / 180 if a == 'd' else (num * 180) / pi, 2)}{b}"

# bonus challenge
def convert_b(data):
    num, a, b = float(data[:-2]), data[-2], data[-1]
    if a in "rd" and b in "rd":
        return convert(data)
    elif a in "cfk" and b in "cfk":
        match a:
            case "c":
                return f"{num + 273.15 if b == 'k' else (num * (9 / 5)) + 32:.2f}{b}"
            case "f":
                return f"{(num + 459.67) * (5 / 9) if b == 'k' else (num - 32) * (5 / 9):.2f}{b}"
            case "k":
                return f"{num - 273.15 if b == 'c' else (num * (9 / 5)) - 459.67:.2f}{b}"
    else:
        return "No candidate for conversion"

assert convert("3.1416rd") == "180.0d"
assert convert("90dr") == "1.57r"

assert convert_b("212fc") == "100.00c"
assert convert_b("70cf") == "158.00f"
assert convert_b("100cr") == "No candidate for conversion"
assert convert_b("315.15kc") == "42.00c"
