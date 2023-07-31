## https://old.reddit.com/r/dailyprogrammer/comments/759fha/20171009_challenge_335_easy_consecutive_distance/

def count_consecutive(nums):
    nums = [int(n) for n in nums.split()]
    return sum(abs(i - j) for i, n in enumerate(nums) for j, m in enumerate(nums) if n == m + 1)

# bonus challenge
def count_consecutive_b(nums, step):
    nums = [int(n) for n in nums.split()]
    return sum(abs(i - j) for i, n in enumerate(nums) for j, m in enumerate(nums) if n == m + step)

assert count_consecutive("1 7 2 11 8 34 3") == 9
assert count_consecutive("31 63 53 56 96 62 73 25 54 55 64") == 26
assert count_consecutive("77 39 35 38 41 42 76 73 40 31 10") == 20
assert count_consecutive("30 63 57 87 37 31 58 83 34 76 38") == 15
assert count_consecutive("18 62 55 92 88 57 90 10 11 96 12") == 3
assert count_consecutive("26 8 7 25 52 17 45 64 11 35 12") == 6
assert count_consecutive("89 57 21 55 56 81 54 100 22 62 50") == 13

# challenge input - answers: 31, 68, 67, 52, 107, 45
print(count_consecutive("76 74 45 48 13 75 16 14 79 58 78 82 46 89 81 88 27 64 21 63"))
print(count_consecutive("37 35 88 57 55 29 96 11 25 42 24 81 82 58 15 2 3 41 43 36"))
print(count_consecutive("54 64 52 39 36 98 32 87 95 12 40 79 41 13 53 35 48 42 33 75"))
print(count_consecutive("21 87 89 26 85 59 54 2 24 25 41 46 88 60 63 23 91 62 61 6"))
print(count_consecutive("94 66 18 57 58 54 93 53 19 16 55 22 51 8 67 20 17 56 21 59"))
print(count_consecutive("6 19 45 46 7 70 36 2 56 47 33 75 94 50 34 35 73 72 39 5"))
