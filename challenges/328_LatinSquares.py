## https://old.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/

def is_latin_1(n, nums):
    nums = nums.split()
    if n != len(set(nums)) or len(nums) != n ** 2:
        return False
    rows = [set(nums[i:i + n]) for i in range(0, len(nums), n)]
    cols = [set(nums[i::n]) for i in range(n)]
    return all(len(r) == n for r in rows) and all(len(c) == n for c in cols)

def is_latin_2(n, nums):
    nums = nums.split()
    if n != len(set(nums)) or len(nums) != n ** 2:
        return False

    for i in range(0, len(nums), n):
        if len(set(nums[i:i + n])) != n:
            return False

    for i in range(n):
        col = set()
        for j in range(0, len(nums), n):
            col.add(nums[i + j])
        if len(col) != n:
            return False
            
    return True

def is_latin_3(n, nums):
    nums = nums.split()
    if n != len(set(nums)) or len(nums) != n ** 2:
        return False
    rows = [True for i in range(0, len(nums), n) if len(set(nums[i:i + n])) == n]
    cols = [True for i in range(n) if len(set(nums[i::n])) == n]
    return len(rows) > 1 and len(cols) > 1

# bonus challenge
def reduce_latin(n, nums):
    if is_latin_2(n, nums):
        nums = nums.split()
        reduced = sorted([nums[i:i + n] for i in range(0, len(nums), n)])
        for row in reduced:
            print(*row)

assert is_latin_1(3, "1 2 3 3 1 2 2 3 1") == True
assert is_latin_1(5, "1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1") == True
assert is_latin_1(2, "1 3 3 4") == False
assert is_latin_1(4, "1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1") == False

assert is_latin_2(3, "1 2 3 3 1 2 2 3 1") == True
assert is_latin_2(5, "1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1") == True
assert is_latin_2(2, "1 3 3 4") == False
assert is_latin_2(4, "1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1") == False

assert is_latin_3(3, "1 2 3 3 1 2 2 3 1") == True
assert is_latin_3(5, "1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1") == True
assert is_latin_3(2, "1 3 3 4") == False
assert is_latin_3(4, "1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1") == False

reduce_latin(3, "1 2 3 3 1 2 2 3 1")
