## https://old.reddit.com/r/dailyprogrammer/comments/42lhem/20160125_challenge_251_easy_create_nonogram/

from itertools import zip_longest


def print_lists(lst, pad=0):
    just = 3
    for l in lst:
        print(" " * (just * pad), end="")
        for c in l:
            print(f"{' ' if c is None else c}".rjust(just), end="")
        print()

# with bonus challenge
def describe_nonogram(ng):
    h, w = len(ls := ng.splitlines()), len(ls[0])
    ng_2 = ng.replace("\n", "")
    rows = [[len(x) for x in l.split()] or [0] for l in ls]
    cols = [[len(x) for x in ng_2[i::w].split()] or [0] for i in range(w)]
    rows = list(zip(*reversed(list(zip_longest(*rows)))))
    pad = len(max(rows, key=lambda r: len(r)))
    print_lists(list(reversed(list(zip_longest(*cols)))), pad)
    print_lists(rows)
    print()

input_1 = """    *
   **
  * *
 *  *
*****"""

input_2 = """    ** *  
   *****  
  ******  
 ******** 
**********
 *      * 
 * ** * * 
 * ** * * 
 * **   * 
 ******** """

input_3 = """     ***       
  **** **      
 ****** ****** 
 * **** **    *
 ****** ***  **
 ****** *******
****** ********
 *   **********
 *   **********
 *   **********
 * * ****  ****
 *** ****  ****
     ****  ****
     ****  ****
     ****  ****"""

input_4 = """    *
   **
    *
 *  *
 * **"""

describe_nonogram(input_1)
describe_nonogram(input_2)
describe_nonogram(input_3)
describe_nonogram(input_4)
