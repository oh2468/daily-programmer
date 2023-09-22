## https://old.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/

def fix_date(dte):
    d = "".join(c if c.isnumeric() else " " for c in dte).split()
    d = d if len(d[0]) == 4 else [d[2], d[0], d[1]]
    return f"{('20' + d[0])[-4:]}-{d[1].rjust(2, '0')}-{d[2].rjust(2, '0')}"

assert fix_date("2/13/15") == "2015-02-13"
assert fix_date("1-31-10") == "2010-01-31"
assert fix_date("5 10 2015") == "2015-05-10"
assert fix_date("2012 3 17") == "2012-03-17"
assert fix_date("2001-01-01") == "2001-01-01"
assert fix_date("2008/01/07") == "2008-01-07"
