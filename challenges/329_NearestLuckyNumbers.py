## https://old.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/

def nearest(n):
    nums = list(range(1, n * 2, 2))
    si = 1
    while si < len(nums):
        m = nums[si]
        if m == n:
            return f"{n} is a lucky number"
        elif m > n:
            return (nums[si - 1], n, m)
        elif m > len(nums):
            si += 1
        else:
            nums = [n for i, n in enumerate(nums, 1) if i % m != 0]
            si += 1

assert nearest(103) == (99, 103, 105)
assert nearest(225) == (223, 225, 231)
assert nearest(997) == "997 is a lucky number"
