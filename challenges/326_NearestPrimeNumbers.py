## https://old.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/

import time
import random


def is_prime(n):
    if n < 1 or n == 2:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nearest(n):
    if is_prime(n):
        return f"{n} is prime."
    p1 = p2 = 0
    x = n if n % 2 != 0 else n - 1
    y = 0
    step = 2
    for i in range(x, 2, -step):
        y += step
        if not p1:
            if is_prime(i):
                p1 = i
        if not p2:
            j = x + y
            if is_prime(j):
                p2 = j
        if p1 and p2:
            break
    return f"{p1} < {n} < {p2}"

# bonus challange (miller rabin testing)
def miller_rabin(n):
    if n == 3: return True
    if n <= 2 or n % 2 == 0: return False
    k, s, d = 50, 0, n - 1
    
    while d % 2 == 0:
        s += 1
        d //= 2
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != (n - 1):
                return False
            x = y
        if y != 1:
            return False
    
    return True

def find_nearest_bonus(n):
    if is_prime(n):
        return f"{n} is prime."
    p1 = p2 = 0
    x = n - 1
    for i in range(x, 2, -1):
        if miller_rabin(i):
            p1 = i
            break
    x = n + 1
    while not p2:
        if miller_rabin(x):
            p2 = x
            break
        x += 1
    return f"{p1} < {n} < {p2}"

assert find_nearest(270) == "269 < 270 < 271"
assert find_nearest(541) == "541 is prime."
assert find_nearest(993) == "991 < 993 < 997"
assert find_nearest(649) == "647 < 649 < 653"

assert find_nearest_bonus(270) == "269 < 270 < 271"
assert find_nearest_bonus(541) == "541 is prime."
assert find_nearest_bonus(993) == "991 < 993 < 997"
assert find_nearest_bonus(649) == "647 < 649 < 653"

# bonus input
t1 = time.time()
print(find_nearest(2010741))
print(find_nearest(1425172824437))
print(find_nearest(142517282443791))
# print(find_nearest_bonus(14251728244377001)) # too slow to brute force
t2 = time.time()
print(f"find_nearest took {t2 - t1}s\n")

t1 = time.time()
print(find_nearest_bonus(2010741))
print(find_nearest_bonus(1425172824437))
print(find_nearest_bonus(142517282443791))
print(find_nearest_bonus(14251728244377001))
t2 = time.time()
print(f"find_nearest_2 took {t2 - t1}s\n")
