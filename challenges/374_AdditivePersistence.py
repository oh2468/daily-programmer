## https://old.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

def add_pers(n):
    if n < 10:
        return 0
    else:
        x = 0
        while n > 0:
            x += n % 10
            n //= 10            
        return 1 + add_pers(x)

assert add_pers(5) == 0
assert add_pers(13) == 1
assert add_pers(1234) == 2
assert add_pers(9876) == 2
assert add_pers(199) == 3
