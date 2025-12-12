# https://support.zebra.com/cpws/docs/eltron/epl2/EPL2_Prog_revF_old.pdf, `A` command
font_heights = {
    1: 12,
    2: 16,
    3: 20,
    4: 24,
    5: 48,
}
default_font = 4
margin = 20

# Copied from https://support.zebra.com/cpws/docs/eltron/common/epl2_samp.htm
header = """
.
N
q812
S2
"""

footer = """
P1
.
"""

txt = f'A{margin},{{v}},0,{{f}},1,1,N,"{{msg}}"'

# https://genius.com/The-isley-brothers-shout-pt-1-and-2-lyrics
# Syntax: prefix with `{font_size}:` to set font per line, otherwise uses `default_font`
message = """Well

You know you make me wanna
5:Shout
Kick my heels up and
5:Shout
Throw my hands up and
5:Shout
Throw my head back and
5:Shout
Come on now
5:Shout
Take it easy
5:Shout
Take it easy
5:Shout
A little bit softer now (Wooo)
A little bit softer now
3:A little bit softer now
2:A little bit softer now
1:A little bit softer now
1:A little bit softer now
1:A little bit louder now
1:A little bit louder now
2:A little bit louder now
3:A little bit louder now
A little bit louder now
A little bit louder now
5:Shout
A little bit louder now
5:Shout
""".splitlines()

print(header)

cursor_v = margin
for line in message:
    if len(line) >= 3 and line[0].isdigit() and line[1] == ":":
        font = int(line[0])
        line = line[2:]
    else:
        font = default_font

    if font == 5:
        # font 5 only supports uppercase characters
        line = line.upper()

    if line and not line.isspace():
        print(txt.format(v=cursor_v, f=font, msg=line))

    cursor_v += font_heights[font] + font_heights[default_font - 1] // 2

print(footer)
