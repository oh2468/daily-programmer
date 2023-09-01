## https://old.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

bases = "0123456789abcdef"

# with bonus 2
def smallest_base(n):
    b = bases.index(max(n)) + 1
    return f"base {b} => {int(n, b)}" if b > 1 else "base 1 => 0"

# bonus 1 and 2
def bonus(n):
    b = bases.index(max(n)) + 1
    return "\n".join([f"base {i} => {int(n, i)}" for i in range(b, 17)]) if b > 1 else "\n".join([f"base {i} => 0" for i in range(1, 17)])

assert smallest_base("1") == "base 2 => 1"
assert smallest_base("21") == "base 3 => 7"
assert smallest_base("ab3") == "base 12 => 1575"
assert smallest_base("ff") == "base 16 => 255"

assert bonus("21") == """base 3 => 7
base 4 => 9
base 5 => 11
base 6 => 13
base 7 => 15
base 8 => 17
base 9 => 19
base 10 => 21
base 11 => 23
base 12 => 25
base 13 => 27
base 14 => 29
base 15 => 31
base 16 => 33"""

print(bonus("1"))
print()
print(bonus("21"))
print()
print(bonus("ab3"))
print()
print(bonus("ff"))
