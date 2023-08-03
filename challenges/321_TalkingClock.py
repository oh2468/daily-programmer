## https://old.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

nums = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirtheen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
mins = ["", "", "twenty", "thirty", "fourty", "fifty"]

def tell_time(t):
    h, m = map(int, t.split(":"))
    n = "am" if h < 12 else "pm"
    hh = nums[12] if h % 12 == 0 else nums[h % 12]
    if m == 0:
        mm = ""
    elif m < 20:
        mm = ("oh " if m < 10 else "") + nums[m]
    else:
        mm = mins[m // 10] + " " + nums[m % 10]
    return f"It's {hh} {mm} {n}".replace("  ", " ")

assert tell_time("00:00") == "It's twelve am"
assert tell_time("01:30") == "It's one thirty am"
assert tell_time("12:05") == "It's twelve oh five pm"
assert tell_time("14:01") == "It's two oh one pm"
assert tell_time("20:29") == "It's eight twenty nine pm"
assert tell_time("21:00") == "It's nine pm"
