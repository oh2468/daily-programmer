## https://old.reddit.com/r/dailyprogrammer/comments/6ze9z0/20170911_challenge_331_easy_the_adding_calculator/

def add(a, b):
    return a + b

def sub(a, b):
    return add(a, -b)

def mul(a, b):
    x = 0
    neg = b < 0
    if neg:
        b = -b
    for _ in range(b):
        x = add(x, a)
    return -x if neg else x

def div(a, b):
    if b == 0:
        return "Not-defined"
    if a == 0:
        return 0
    if a == b:
        return 1
    a_neg, b_neg = a < 0, b < 0
    if a_neg:
        a = -a
    if b_neg:
        b = -b
    for i in range(2, a):
        t = mul(b, i)
        if t == a:
            return i if (a_neg and b_neg) or (not a_neg and not b_neg) else -i
        if t > a:
            break
    return "Non-integral answer"

def wop(a, b):
    if b < 0:
        return "Non-integral answer"
    x = 1
    for _ in range(b):
        x = mul(x, a)
    return x

def calc(x):
    a, t, b = x.split()
    a, b = int(a), int(b)
    match t:
        case "+":
            return add(a, b)
        case "-":
            return sub(a, b)
        case "*":
            return mul(a, b)
        case "/":
            return div(a, b)
        case "^":
            return wop(a, b)
        case _:
            return None

assert calc("12 + 25") == 37
assert calc("-30 + 100") == 70
assert calc("100 - 30") == 70
assert calc("100 - -30") == 130
assert calc("-25 - 29") == -54
assert calc("-41 - -10") == -31
assert calc("9 * 3") == 27
assert calc("9 * -4") == -36
assert calc("-4 * 8") == -32
assert calc("-12 * -9") == 108
assert calc("100 / 2") == 50
assert calc("75 / -3") == -25
assert calc("-75 / 3") == -25
assert calc("7 / 3") == "Non-integral answer"
assert calc("0 / 0") == "Not-defined"
assert calc("5 ^ 3") == 125
assert calc("-5 ^ 3") == -125
assert calc("-8 ^ 3") == -512
assert calc("-1 ^ 1") == -1
assert calc("1 ^ 1") == 1
assert calc("0 ^ 5") == 0
assert calc("5 ^ 0") == 1
assert calc("10 ^ -3") == "Non-integral answer"
assert calc("9 ^ 9") == 387420489
