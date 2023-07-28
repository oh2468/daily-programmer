## https://old.reddit.com/r/dailyprogrammer/comments/79npf9/20171030_challenge_338_easy_what_day_was_it_again/

import calendar


def quick_fix(yy, mm, dd):
    return calendar.day_name[calendar.weekday(yy, mm, dd)]

def calc_weekday(yy, mm, dd):
    yy, mm, dd = yy - 1, mm - 1, dd - 1
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    regular_days = yy * 365
    leap_days = (yy // 4) - (yy // 100) + (yy // 400)
    is_leap_year = lambda y: (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)
    leap_days += is_leap_year(yy + 1) and mm > 1
    all_days = regular_days + leap_days + sum(month_days[0:mm]) + dd
    return weekdays[all_days % len(weekdays)]

print(quick_fix(1, 1, 1))
print(quick_fix(2017, 10, 30))
print(quick_fix(2016, 2, 29))
print(quick_fix(2015, 2, 28))
print(quick_fix(29, 4, 12))
print(quick_fix(570, 11, 30))
print(quick_fix(1066, 9, 25))
print(quick_fix(1776, 7, 4))
print(quick_fix(1933, 1, 30))
print(quick_fix(1953, 3, 6))
print(quick_fix(2100, 1, 9))
print(quick_fix(2202, 12, 15))
print(quick_fix(7032, 3, 26))

assert quick_fix(1, 1, 1) == calc_weekday(1, 1, 1)
assert quick_fix(2017, 10, 30) == calc_weekday(2017, 10, 30)
assert quick_fix(2016, 2, 29) == calc_weekday(2016, 2, 29)
assert quick_fix(2015, 2, 28) == calc_weekday(2015, 2, 28)
assert quick_fix(29, 4, 12) == calc_weekday(29, 4, 12)
assert quick_fix(570, 11, 30) == calc_weekday(570, 11, 30)
assert quick_fix(1066, 9, 25) == calc_weekday(1066, 9, 25)
assert quick_fix(1776, 7, 4) == calc_weekday(1776, 7, 4)
assert quick_fix(1933, 1, 30) == calc_weekday(1933, 1, 30)
assert quick_fix(1953, 3, 6) == calc_weekday(1953, 3, 6)
assert quick_fix(2100, 1, 9) == calc_weekday(2100, 1, 9)
assert quick_fix(2202, 12, 15) == calc_weekday(2202, 12, 15)
assert quick_fix(7032, 3, 26) == calc_weekday(7032, 3, 26)
