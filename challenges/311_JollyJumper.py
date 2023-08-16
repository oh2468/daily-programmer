## https://old.reddit.com/r/dailyprogrammer/comments/65vgkh/20170417_challenge_311_easy_jolly_jumper/

def is_jolly_jumper(line):
    nums = [int(n) for n in line.split()]
    return {abs(nums[i] - nums[i + 1]) for i in range(1, len(nums) - 1)} == set(range(1, nums[0]))

assert is_jolly_jumper("4 1 4 2 3") == True
assert is_jolly_jumper("8 1 6 -1 8 9 5 2 7") == False
assert is_jolly_jumper("4 1 4 2 3") == True
assert is_jolly_jumper("5 1 4 2 -1 6") == False
assert is_jolly_jumper("4 19 22 24 21") == False
assert is_jolly_jumper("4 19 22 24 25") == True
assert is_jolly_jumper("4 2 -1 0 2") == True
