## https://old.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/

test_assert = True
chars = "abcdefghijklmnopqrstuvwxyz"

def quick_fix(n):
    res = ""
    for i in range(n):
        res = f"{res}{chars[i]}{res}"
    # print(res)
    return res

## bonus solution: Complete the challenge using O(n) memory, where n is the iteration number
## my solution uses O(1) memory but is suuuuuper slow
def abacaba(n):
    x = ""
    for i in range((2**n) - 1):
        if i % 2 == 0:
            if test_assert:
                x += "a"
            else:
                print("a", end="")
        else:
            for j in range(n - 1, 0, -1):
                if (i + 1) % (2**j) == 0:
                    if test_assert:
                        x += chars[j]
                    else:
                        print(chars[j], end="")
                    break
    if test_assert:
        return x
    else:
        print()

assert quick_fix(1) == "a"
assert quick_fix(2) == "aba"
assert quick_fix(3) == "abacaba"
assert quick_fix(4) == "abacabadabacaba"
assert quick_fix(5) == "abacabadabacabaeabacabadabacaba"

if test_assert:
    assert abacaba(1) == "a"
    assert abacaba(2) == "aba"
    assert abacaba(3) == "abacaba"
    assert abacaba(4) == "abacabadabacaba"
    assert abacaba(5) == "abacabadabacabaeabacabadabacaba"

    assert quick_fix(1) == abacaba(1)
    assert quick_fix(2) == abacaba(2)
    assert quick_fix(3) == abacaba(3)
    assert quick_fix(4) == abacaba(4)
    assert quick_fix(5) == abacaba(5)
else:
    abacaba(1)
    abacaba(2)
    abacaba(3)
    abacaba(4)
    abacaba(5)
