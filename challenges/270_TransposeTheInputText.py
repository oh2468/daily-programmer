## https://old.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text/

from itertools import zip_longest


def transpose(text):
    return "\n".join("".join(x).rstrip() for x in zip_longest(*text.split("\n"), fillvalue=" "))

input_1 = """ABC
DEF"""
output_1 = """AD
BE
CF"""

input_2 = """Some
text."""
output_2 = """St
oe
mx
et
 ."""

input_3 = """package main

import "fmt"

func main() {
    queue := make(chan string, 2)
    queue <- "one"
    queue <- "twoO"
    close(queue)
    for elem := range queue {
        fmt.Println(elem)
    }
}"""
output_3 = """p i f       }
a m u
c p n
k o c
a r  qqqcf }
g t muuulo
e   aeeeor
  " iuuus
m f neeeeef
a m (   (lm
i t ):<<qet
n "  =--um.
    {   e P
     m""u:r
     aote=i
     knw) n
     eeo rt
     ("O al
     c " nn
     h   g(
     a   ee
     n    l
         qe
     s   um
     t   e)
     r   u
     i   e
     n
     g   {
     ,

     2
     )"""

assert transpose(input_1) == output_1
assert transpose(input_2) == output_2
assert transpose(input_3) == output_3
