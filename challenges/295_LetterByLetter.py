## https://old.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/

def swap(l1, l2):
    for i in range(len(l2)):
        if l1[i] != l2[i]:
            print(l2[0:i] + l1[i:])
    print(l2)

swap("floor", "brake")
swap("wood", "book")
swap("a fall to the floor", "braking the door in")
