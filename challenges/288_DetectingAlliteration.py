## https://old.reddit.com/r/dailyprogrammer/comments/57zcbm/20161017_challenge_288_easy_detecting_alliteration/

stop_words = "I  a  about  an  and are  as  at  be  by  come  for  from how in  is  it  of  on  or  that the  this to  was  what  when where who  will  with the".lower().split()

def get_groups(lines):
    groups = []
    patt = ".,?!"
    fakex = lambda w, p: w if not p else fakex(w.replace(p.pop(), ""), p) 
    for line in lines:
        group = [""]
        words = [fakex(word, list(patt)) for word in line.split() if word not in stop_words]
        for i, word in enumerate(words):
            if i > 0 and word[0] == words[i - 1][0]:
                group.append(word)
                continue
            if i + 1 < len(words) and word[0] == words[i + 1][0]:
                group.append(word)
        groups.append(group[1:])

    for g in groups:
        print(g)
    return [" ".join(g) for g in groups]


sam_inp = """Peter Piper Picked a Peck of Pickled Peppers
Bugs Bunny likes to dance the slow and simple shuffle
You'll never put a better bit of butter on your knife""".lower().split("\n")

sam_out = """Peter Piper Picked Peck Pickled Peppers
Bugs Bunny slow simple shuffle
better bit butter""".lower().split("\n")

cha_inp = """The daily diary of the American dream
For the sky and the sea, and the sea and the sky
Three grey geese in a green field grazing, Grey were the geese and green was the grazing.
But a better butter makes a batter better.
"His soul swooned slowly as he heard the snow falling faintly through the universe and faintly falling, like the descent of their last end, upon all the living and the dead."
Whisper words of wisdom, let it be.
They paved paradise and put up a parking lot.
So what we gonna have, dessert or disaster?""".lower().split("\n")

cha_out = """daily diary
sky sea
grey geese green grazing
better butter batter better
soul swooned slowly
whisper words wisdom
paved paradise
dessert disaster""".lower().split("\n")

assert get_groups(sam_inp) == sam_out
# assert get_groups(cha_inp) == cha_out
# get_groups(sam_inp)
get_groups(cha_inp)
