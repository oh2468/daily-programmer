## https://old.reddit.com/r/dailyprogrammer/comments/4lpygb/20160530_challenge_269_easy_basic_formatting/

from collections import Counter


INDENTATION = "····"
OLD_INDENT = "·»"
STARTERS = ["FOR", "IF"]
ENDERS = ["NEXT", "ENDIF"]

def to_basic_indent(text):
    lines = [l.lstrip(OLD_INDENT).split(" ") for l in text.split("\n")]
    ind = 0
    out = []
    for line in lines:
        if line[0] in ENDERS:
            ind -= 1
        ind_line = (INDENTATION * ind) + " ".join(line)
        out.append(ind_line)
        if line[0] in STARTERS:
            ind += 1
    return "\n".join(out)

# bonus challenge
def is_correct(text):
    w_count = Counter([w.lstrip(INDENTATION) for w in text.split()])
    errors = [" - ENCOUNTERED ERRORS - "]
    for s, e in zip(STARTERS, ENDERS):
        if w_count[s] != w_count[e]:
            errors.append(f"ERROR: found {w_count[s]} {s} and {w_count[e]} {e}")
    return "The entered code had enclosing errors." if len(errors) == 1 else "\n".join(errors)

cha_inp = """VAR I
·FOR I=1 TO 31
»»»»IF !(I MOD 3) THEN
··PRINT "FIZZ"
··»»ENDIF
»»»»····IF !(I MOD 5) THEN
»»»»··PRINT "BUZZ"
··»»»»»»ENDIF
»»»»IF (I MOD 3) && (I MOD 5) THEN
······PRINT "FIZZBUZZ"
··»»ENDIF
»»»»·NEXT"""
cha_out = """VAR I
FOR I=1 TO 31
····IF !(I MOD 3) THEN
········PRINT "FIZZ"
····ENDIF
····IF !(I MOD 5) THEN
········PRINT "BUZZ"
····ENDIF
····IF (I MOD 3) && (I MOD 5) THEN
········PRINT "FIZZBUZZ"
····ENDIF
NEXT"""

bon_inp_1 = """FOR I=0 TO 10
····IF I MOD 2 THEN
········PRINT I
NEXT"""
bon_inp_2 = """FOR I=0 TO 10
····IF I MOD 2 THEN
········PRINT I"""
bon_inp_3 = """FOR I=0 TO 10
····PRINT I
ENDIF"""
bon_inp_4 = """FOR I=0 TO 10
····PRINT I
NEXT
ENDIF"""

assert to_basic_indent(cha_inp) == cha_out

print(is_correct(bon_inp_1))
print(is_correct(bon_inp_2))
print(is_correct(bon_inp_3))
print(is_correct(bon_inp_4))
