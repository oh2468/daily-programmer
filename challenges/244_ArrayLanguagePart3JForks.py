## https://old.reddit.com/r/dailyprogrammer/comments/3wdm0w/20151209_challenge_244_easyer_array_language_part/

def ssum(x, y=None):
    return sum(x) + (sum(y) if y is not None else 0)

def ddiv(x, y=None):
    return x / (y or 1)

def ccount(x, y=None):
    return len(x) + (len(y) if y is not None else 0)

def mmul(x, y=None):
    return x * (y or 1)

def frac(x, y=None):
    return len(x) / (y or 0.25)

def fork(*args):
    def f(x, y=None):
        if len(args) == 3:
            return args[1](args[0](x, y), args[2](x, y))
        elif len(args) > 3 and len(args) % 2 == 1:
            return args[1](args[0](x, y), fork(*args[2:])(x, y))
        else:
            raise ValueError("Invalid number of arguments")
    return f

input = [1,2,3,4,5,6,7,8,9]
print(fork(ssum, ddiv, ccount)(input))
print(fork(ssum, ddiv, ccount, mmul, frac)(input))
