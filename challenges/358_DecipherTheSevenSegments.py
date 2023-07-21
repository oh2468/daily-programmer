## https://old.reddit.com/r/dailyprogrammer/comments/8eger3/20180423_challenge_358_easy_decipher_the_seven/

display = {
    " _ | ||_|": 0,
    "     |  |": 1,
    " _  _||_ ": 2,
    " _  _| _|": 3,
    "   |_|  |": 4,
    " _ |_  _|": 5,
    " _ |_ |_|": 6,
    " _   |  |": 7,
    " _ |_||_|": 8,
    " _ |_| _|": 9
}

def decipher(lines):
    res = 0
    for i in range(0, len(lines[0]), 3):
        res *= 10
        num = ""
        for line in lines:
            num += line[i:i + 3]
        res += display[num]
    return res

cha_input_1 = """    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|""".split("\n")

cha_input_2 = """    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|""".split("\n")

cha_input_3 = """ _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|""".split("\n")

cha_input_4 = """ _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ """.split("\n")

assert decipher(cha_input_1) == 123456789
assert decipher(cha_input_2) == 433805825
assert decipher(cha_input_3) == 526837608
assert decipher(cha_input_4) == 954105592
