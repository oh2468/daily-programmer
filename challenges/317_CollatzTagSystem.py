##https://old.reddit.com/r/dailyprogrammer/comments/6e08v6/20170529_challenge_317_easy_collatz_tag_system/

def collatz_tag_system(s):
    tags = {"a": "bc", "b": "a", "c": "aaa"}
    all_s = ""
    while len(s) >= 2:
        s = s[2:] + tags[s[0]]
        print(s)
        all_s += f"\n{s}"
    print(all_s)
    return all_s

ch_input_1 = "aaa"
ch_input_2 = "aaaaaaa"

ch_output_1 = """
abc
cbc
caaa
aaaaa
aaabc
abcbc
cbcbc
cbcaaa
caaaaaa
aaaaaaaa
aaaaaabc
aaaabcbc
aabcbcbc
bcbcbcbc
bcbcbca
bcbcaa
bcaaa
aaaa
aabc
bcbc
bca
aa
bc
a"""

ch_output_2 = """
aaaaabc
aaabcbc
abcbcbc
cbcbcbc
cbcbcaaa
cbcaaaaaa
caaaaaaaaa
aaaaaaaaaaa
aaaaaaaaabc
aaaaaaabcbc
aaaaabcbcbc
aaabcbcbcbc
abcbcbcbcbc
cbcbcbcbcbc
cbcbcbcbcaaa
cbcbcbcaaaaaa
cbcbcaaaaaaaaa
cbcaaaaaaaaaaaa
caaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaabc
aaaaaaaaaaaaabcbc
aaaaaaaaaaabcbcbc
aaaaaaaaabcbcbcbc
aaaaaaabcbcbcbcbc
aaaaabcbcbcbcbcbc
aaabcbcbcbcbcbcbc
abcbcbcbcbcbcbcbc
cbcbcbcbcbcbcbcbc
cbcbcbcbcbcbcbcaaa
cbcbcbcbcbcbcaaaaaa
cbcbcbcbcbcaaaaaaaaa
cbcbcbcbcaaaaaaaaaaaa
cbcbcbcaaaaaaaaaaaaaaa
cbcbcaaaaaaaaaaaaaaaaaa
cbcaaaaaaaaaaaaaaaaaaaaa
caaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaabc
aaaaaaaaaaaaaaaaaaaaaabcbc
aaaaaaaaaaaaaaaaaaaabcbcbc
aaaaaaaaaaaaaaaaaabcbcbcbc
aaaaaaaaaaaaaaaabcbcbcbcbc
aaaaaaaaaaaaaabcbcbcbcbcbc
aaaaaaaaaaaabcbcbcbcbcbcbc
aaaaaaaaaabcbcbcbcbcbcbcbc
aaaaaaaabcbcbcbcbcbcbcbcbc
aaaaaabcbcbcbcbcbcbcbcbcbc
aaaabcbcbcbcbcbcbcbcbcbcbc
aabcbcbcbcbcbcbcbcbcbcbcbc
bcbcbcbcbcbcbcbcbcbcbcbcbc
bcbcbcbcbcbcbcbcbcbcbcbca
bcbcbcbcbcbcbcbcbcbcbcaa
bcbcbcbcbcbcbcbcbcbcaaa
bcbcbcbcbcbcbcbcbcaaaa
bcbcbcbcbcbcbcbcaaaaa
bcbcbcbcbcbcbcaaaaaa
bcbcbcbcbcbcaaaaaaa
bcbcbcbcbcaaaaaaaa
bcbcbcbcaaaaaaaaa
bcbcbcaaaaaaaaaa
bcbcaaaaaaaaaaa
bcaaaaaaaaaaaa
aaaaaaaaaaaaa
aaaaaaaaaaabc
aaaaaaaaabcbc
aaaaaaabcbcbc
aaaaabcbcbcbc
aaabcbcbcbcbc
abcbcbcbcbcbc
cbcbcbcbcbcbc
cbcbcbcbcbcaaa
cbcbcbcbcaaaaaa
cbcbcbcaaaaaaaaa
cbcbcaaaaaaaaaaaa
cbcaaaaaaaaaaaaaaa
caaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaabc
aaaaaaaaaaaaaaaabcbc
aaaaaaaaaaaaaabcbcbc
aaaaaaaaaaaabcbcbcbc
aaaaaaaaaabcbcbcbcbc
aaaaaaaabcbcbcbcbcbc
aaaaaabcbcbcbcbcbcbc
aaaabcbcbcbcbcbcbcbc
aabcbcbcbcbcbcbcbcbc
bcbcbcbcbcbcbcbcbcbc
bcbcbcbcbcbcbcbcbca
bcbcbcbcbcbcbcbcaa
bcbcbcbcbcbcbcaaa
bcbcbcbcbcbcaaaa
bcbcbcbcbcaaaaa
bcbcbcbcaaaaaa
bcbcbcaaaaaaa
bcbcaaaaaaaa
bcaaaaaaaaa
aaaaaaaaaa
aaaaaaaabc
aaaaaabcbc
aaaabcbcbc
aabcbcbcbc
bcbcbcbcbc
bcbcbcbca
bcbcbcaa
bcbcaaa
bcaaaa
aaaaa
aaabc
abcbc
cbcbc
cbcaaa
caaaaaa
aaaaaaaa
aaaaaabc
aaaabcbc
aabcbcbc
bcbcbcbc
bcbcbca
bcbcaa
bcaaa
aaaa
aabc
bcbc
bca
aa
bc
a"""

assert collatz_tag_system(ch_input_1) == ch_output_1
assert collatz_tag_system(ch_input_2) == ch_output_2
