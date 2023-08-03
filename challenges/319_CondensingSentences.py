## https://old.reddit.com/r/dailyprogrammer/comments/6grwny/20170612_challenge_319_easy_condensing_sentences/

def condense(string):
    condensed = []
    for i, word in enumerate(string.split()):
        if i == 0:
            condensed.append(word)
            continue
        match = 0
        for i in range(1, len(word) + 1):
            if word.startswith(condensed[-1][-i::]):
                match = i
        if match:
            condensed[-1] += word[match::]
        else:
            condensed.append(word)
    return " ".join(condensed)

ex_input = "I heard the pastor sing live verses easily."
ch_input_1 = "Deep episodes of Deep Space Nine came on the television only after the news."
ch_input_2 = "Digital alarm clocks scare area children."

assert condense(ex_input) == "I heard the pastor sing liverses easily."
assert condense(ch_input_1) == "Deepisodes of Deep Space Nine came on the televisionly after the news."
assert condense(ch_input_2) == "Digitalarm clockscarea children."
