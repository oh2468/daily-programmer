## https://old.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

def find_first(string):
    for c in string:
        if string.count(c) > 1:
            return c
    return ""

# bonus challenge (0 based indexing)
def b1(string):
    for i, c in enumerate(string):
        for j in range(i + 1, len(string)):
            if c == string[j]:
                return (i, j)
    return None

assert find_first("ABCDEBC") == "B"

# challenge input
print(find_first("IKEUNFUVFV"))
print(find_first("PXLJOUDJVZGQHLBHGXIW"))
print(find_first('*l1J?)yn%R[}9~1"=k7]9;0[$'))

# bonus input
print(b1("ABCDEBC"))
print(b1("IKEUNFUVFV"))
print(b1("PXLJOUDJVZGQHLBHGXIW"))
print(b1('*l1J?)yn%R[}9~1"=k7]9;0[$'))
