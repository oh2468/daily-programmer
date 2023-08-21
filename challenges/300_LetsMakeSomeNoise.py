## https://old.reddit.com/r/dailyprogrammer/comments/5prdgb/20170123_challenge_300_easy_lets_make_some_noise/

import winsound


notes = {
    "do": -9, "re": -7, "mi": -5,
    "fa": -4, "sol": -2, "la": 0,
    "ti": 2
}

def beep_solfege(oct):
    hz = (2 ** oct) * 440
    for n, v in notes.items():
        nhz = int((2 ** (v / 12)) * hz)
        print(f"{n} - {nhz}")
        winsound.Beep(nhz, 500)

beep_solfege(-1)
beep_solfege(0)
beep_solfege(1)
