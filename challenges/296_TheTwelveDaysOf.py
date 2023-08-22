## https://old.reddit.com/r/dailyprogrammer/comments/5j6ggm/20161219_challenge_296_easy_the_twelve_days_of/

days = "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelveth".split()
nums = "a two three four five six seven eight nine ten eleven twelve".split()
lyrics = """Partridge in a Pear Tree
Turtle Doves
French Hens
Calling Birds
Golden Rings
Geese a Laying
Swans a Swimming
Maids a Milking
Ladies Dancing
Lords a Leaping
Pipers Piping
Drummers Drumming""".split("\n")

def print_lyrics(day, line, lyr):
    if line <= 1:
        if day != 1:
            print("and ", end="")
        print(f"{nums[0]} {lyr[0]}")
    else:
        print(f"{nums[line - 1]} {lyr[line - 1]}")
        print_lyrics(day, line - 1, lyr)

# with bonus 1 and 2
def sing(lyr):
    for i, day in enumerate(days, 1):
        print(f"On the {day} day of Christmas\nmy true love sent to me:")
        print_lyrics(i, i, lyr)
        print()

sing(lyrics)
