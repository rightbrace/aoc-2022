# addx is basically no-op if numbers are implicitly adding
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

# Grabs the values at 1 less than the given indicies
def list_grab(l, idxs):
    return [l[i-1] for i in range(len(l)) if i in idxs]

def dot_product(a, b):
    return sum([a[i] * b[i] for i in range(min(len(a), len(b)))])

interesting_cycles = [20, 60, 100, 140, 180, 220]
interesting_values = list_grab(x_values, interesting_cycles)
print(dot_product(interesting_values, interesting_cycles))