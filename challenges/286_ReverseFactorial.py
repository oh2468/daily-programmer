## https://old.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/

def find_reversed(n):
    on, c = n, 1
    while n > 1:
        c += 1
        n /= c
    return f"{on} " + (f"= {c}!" if n == 1 else "NONE")

assert find_reversed(120) == "120 = 5!"
assert find_reversed(150) == "150 NONE"
assert find_reversed(3628800) == "3628800 = 10!"
assert find_reversed(479001600) == "479001600 = 12!"
assert find_reversed(6) == "6 = 3!"
assert find_reversed(18) == "18 NONE"
