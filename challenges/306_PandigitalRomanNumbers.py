## https://old.reddit.com/r/dailyprogrammer/comments/5z4f3z/20170313_challenge_306_easy_pandigital_roman/

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
num_set = set("IVXLCDM")

def int_to_roman(n):
    r = ""
    for num, rom in num_map:
        if n <= 0:
            break
        a, b = divmod(n, num)
        r += rom * a
        n = b
    return r

def find_pandigital(n):
    return [(r, i) for i in range(900, n + 1) if set(r := int_to_roman(i)) == num_set and len(r) == len(num_set)]

print(find_pandigital(2000))
