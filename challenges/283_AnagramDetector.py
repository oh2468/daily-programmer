## https://old.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/

def is_anagram(s1, s2):
    ss1, ss2 = [sorted([c for c in s.lower() if c.isalpha()]) for s in [s1, s2]]
    return f'"{s1}" is {"" if ss1 == ss2 and set(s1.split()) != set(s2.split()) else "NOT "}an anagram of "{s2}"'

assert is_anagram("Clint Eastwood", "Old West Action") == '"Clint Eastwood" is an anagram of "Old West Action"'
assert is_anagram("parliament", "partial man") == '"parliament" is NOT an anagram of "partial man"'
assert is_anagram("wisdom", "mid sow") == '"wisdom" is an anagram of "mid sow"'
assert is_anagram("Seth Rogan", "Gathers No") == '"Seth Rogan" is an anagram of "Gathers No"'
assert is_anagram("Reddit", "Eat Dirt") == '"Reddit" is NOT an anagram of "Eat Dirt"'
assert is_anagram("Schoolmaster", "The classroom") == '"Schoolmaster" is an anagram of "The classroom"'
assert is_anagram("Astronomers",  "Moon starer") == '"Astronomers" is NOT an anagram of "Moon starer"'
assert is_anagram("Vacation Times", "I'm Not as Active") == '"Vacation Times" is an anagram of "I\'m Not as Active"'
assert is_anagram("Dormitory", "Dirty Rooms") == '"Dormitory" is NOT an anagram of "Dirty Rooms"'
assert is_anagram("Test This", "This Test") == '"Test This" is NOT an anagram of "This Test"'
assert is_anagram("Identity", "Identity") == '"Identity" is NOT an anagram of "Identity"'
