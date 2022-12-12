# This program is either slightly wrong or the image is meant to be a bit corrupted
# but I got the right answer so...

import re

with open("input.txt") as f:
    program = ["None"] + re.split(r"[\s\n]", f.read().strip())


x_values = [1] * len(program)
for cycle, op in enumerate(program):
    x_values[cycle] = x_values[cycle-1] if cycle > 0 else 1
    try:
        x_values[cycle] += int(op)
    except:
        pass

display = [[' ' for i in range(40)] for i in range(6)]

for cycle, sprite_pos in enumerate(x_values):
    cx = (cycle+1) % 40 
    cy = cycle // 40
    sx = (sprite_pos+1) % 40
    if sx - 1 <= cx <= sx + 1:
        display[cy][cx] = "#"

for row in display:
    print("".join(row))    