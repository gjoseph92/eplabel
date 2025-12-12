import sys

# ./print.sh "message" <count> <R>

# https://support.zebra.com/cpws/docs/eltron/epl2/EPL2_Prog_revF_old.pdf, `A` command
font_sizes_dots = {
    1: (8, 12),
    2: (10, 16),
    3: (12, 20),
    4: (14, 24),
    5: (32, 48),
}
default_font = 4
max_scaling = 6
char_spacing = 2  # a guess based on 1-18 in manual?
line_spacing = 0.5
portrait = False
rot = 0 if portrait else 1  # 1 = 90 degrees
margin = 20
dpi = 203
width_in = 4
height_in = 6
encoding = 'latin1'

width = width_in * dpi
height = height_in * dpi
mid_page_x = width // 2
mid_page_y = height // 2
max_dots = (width if portrait else height) - margin * 2

msg = sys.argv[1]
count = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
reverse = True if len(sys.argv) == 4 and sys.argv[3].lower() == "r" else False

assert count > 0, f"Invalid {count=}"

# Copied from https://support.zebra.com/cpws/docs/eltron/common/epl2_samp.htm
header = f"""
.
N
q{width}
S2
"""

footer = f"""
P{count}
.
"""

lines = msg.strip().split("\n")
char_w, char_h = font_sizes_dots[default_font]

height_dots = char_h * len(lines) + char_h * line_spacing * (len(lines) - 1)
scaling = int(min((height if portrait else width) // height_dots, max_scaling))
assert scaling > 0, f"Too many lines"

lens_dots = []
for line in lines:
    len_dots = len(line) * (char_w + char_spacing)
    lens_dots.append(len_dots)
    scaling = min(max_dots // len_dots, scaling)
    assert scaling > 0, "Line too long {len_dots=}: {line!r} "

line_h = char_h * scaling
spacing = round(line_spacing * line_h)
total_h = line_h * len(lines) + spacing * (len(lines) - 1)

cmds = []
for i, (line, len_dots) in enumerate(zip(lines, lens_dots)):
    w = len_dots * scaling
    assert w <= max_dots, f"Line {i} Too long: {w} dots > {max_dots}"

    if portrait:
        x = mid_page_x - w // 2 + char_spacing // 2
        y = mid_page_y - total_h // 2 + (line_h + spacing) * i
    else:
        x = mid_page_x + total_h // 2 - (line_h + spacing) * i 
        y = mid_page_y - w // 2 + char_spacing // 2

    cmd_u = f'A{x},{y},{rot},{default_font},{scaling},{scaling},{"R" if reverse else "N"},"{line}"'
    try:
        cmd = cmd_u.encode(encoding)
    except UnicodeEncodeError as e:
        raise ValueError(f"Unprintable character in line {i}: {line}") from e
    else:
        cmds.append(cmd)

def printb(b: bytes) -> None:
    sys.stdout.buffer.write(b)
    sys.stdout.buffer.write(b"\n")

printb(header.encode(encoding))
for cmd in cmds:
    printb(cmd)
printb(footer.encode(encoding))

