## https://old.reddit.com/r/dailyprogrammer/comments/4xy6i1/20160816_challenge_279_easy_uuencoding/

def encode(text):
    lg, cg, bg = 45, 3, 6
    byts = bytes(text, "UTF-8")
    chr_map = lambda n: chr(n + 32)
    lines = []
    for i in range(0, len(byts), lg):
        line = byts[i:i + lg]
        ll = len(line)
        if ll < lg and ll % cg != 0:
            line += bytes("0" * (cg - (ll % cg)), "UTF-8")
        bits = "".join(map(lambda b: f"{b:08b}", line))
        chrs = "".join([chr_map(int(bits[j:j + bg], 2)) for j in range(0, len(bits), bg)])
        lines.append(chr_map(ll) + chrs)
    name = t[0].lower() if len(t := text.split(" ")) == 1 else "file"
    start = f"begin 644 {name}.txt\n"
    middle = "\n".join(lines)
    end = "\n`\nend"
    return start + middle + end

# bonus 1
def decode(data):
    data = data.split("\n")[1:-2]
    out = ""
    for line in data:
        ll = ord(line[0]) - 32
        bits = "".join([f"{ord(c) - 32:06b}" for c in line[1:]])
        byts = bytes([int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)])[0:ll]
        out += str(byts, "UTF-8")
    return out

input_1 = "Cat"
output_1 = """begin 644 cat.txt
#0V%T
`
end"""

input_2 = "I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy — but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life."
output_2 = """begin 644 file.txt
M22!F965L('9E<GD@<W1R;VYG;'D@86)O=70@>6]U(&1O:6YG(&1U='DN(%=O
M=6QD('EO=2!G:79E(&UE(&$@;&ET=&QE(&UO<F4@9&]C=6UE;G1A=&EO;B!A
M8F]U="!Y;W5R(')E861I;F<@:6X@1G)E;F-H/R!)(&%M(&=L860@>6]U(&%R
M92!H87!P>2#B@)0@8G5T($D@;F5V97(@8F5L:65V92!M=6-H(&EN(&AA<'!I
M;F5S<RX@22!N979E<B!B96QI979E(&EN(&UI<V5R>2!E:71H97(N(%1H;W-E
M(&%R92!T:&EN9W,@>6]U('-E92!O;B!T:&4@<W1A9V4@;W(@=&AE('-C<F5E
M;B!O<B!T:&4@<')I;G1E9"!P86=E<RP@=&AE>2!N979E<B!R96%L;'D@:&%P
3<&5N('1O('EO=2!I;B!L:69E+C P
`
end"""

assert encode(input_1) == output_1
assert encode(input_2) == output_2

assert decode(output_1) == input_1
assert decode(output_2) == input_2
