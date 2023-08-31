## https://old.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/

def fib_nums(n):
    nums = [0, 1, 1] + [0] * (n - 2)
    if n <= 2:
        return nums[0:n + 1]
    else:
        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums

def fib_vals(n):
    nums = [0, 1]
    while nums[-1] <= n:
        nums.append(nums[-1] + nums[-2])
    return nums[:-1]

def converter(b, n):
    if b == "F":
        nums = reversed(fib_nums(len(n)))
        return str(sum([int(x) * y for x, y in zip(n, nums)]))
    else:
        n, x, s = int(n), int(n), ""
        vals = fib_vals(n)
        nums = reversed(vals[1:])
        for num in nums:
            if num <= x:
                s += "1"
                x -= num
            else:
                s += "0"
        return s

assert converter("10", "16") == "1001000"
assert converter("10", "32") == "10101000"
assert converter("10", "9024720") == "1010100101010100000010001000010010"
assert converter("F", "10") == "1"
assert converter("F", "1") == "1"
assert converter("F", "111111") == "20"
assert converter("F", "100000") == "8"
assert converter("F", "10110110100111001") == "2868"
