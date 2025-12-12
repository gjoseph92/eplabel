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
char_spacing = 2  # a guess based on 1-18 in manual?
portrait = False
margin = 20
dpi = 203
width_in = 4
height_in = 6

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

char_w, char_h = font_sizes_dots[default_font]
len_dots = len(msg) * (char_w + char_spacing)
scaling = min(max_dots // len_dots, 6)
assert scaling > 0, "Message too long: {len_dots=}"

w = len_dots * scaling
h = char_h * scaling
assert w <= max_dots, f"Too long: {w} dots > {max_dots}"

if portrait:
    rot = 0
    x = mid_page_x - w // 2 + char_spacing // 2
    y = mid_page_y - h // 2
else:
    rot = 1  # 90 degrees
    x = mid_page_x + h // 2
    y = mid_page_y - w // 2 + char_spacing // 2

txt = f'A{x},{y},{rot},{default_font},{scaling},{scaling},{"R" if reverse else "N"},"{msg}"'


print(header)
print(txt)
print(footer)

