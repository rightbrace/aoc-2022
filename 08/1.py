
def sign(x):
    if x == 0:
        return 0
    return x / abs(x)

# What will be the next position of the tail, based on the current head position?
def tail_pos(hx, hy, tx, ty):
    dx = hx-tx
    dy = hy-ty

    # No movement for on top, directly adjacent, or directly diagonal
    if dx*dx + dy*dy <= 2:
        return tx, ty

    # Step one towards in all axes where there exists a seperation
    # Assumes that H is never further than a "knight move" or two spaces
    # horizontally/vertically/diagonally
    return tx + sign(dx), ty + sign(dy)

# Track head and tail positions
hx, hy = 0, 0
tx, ty = 0, 0
tail_visited = set([(tx, ty)])

def move(dx, dy):
    global hx, hy, tx, ty
    for i in range(abs(dx)):
        hx += sign(dx)
        tx, ty = tail_pos(hx, hy, tx, ty)
        tail_visited.add((tx, ty))

    for i in range(abs(dy)):
        hy += sign(dy)
        tx, ty = tail_pos(hx, hy, tx, ty)
        tail_visited.add((tx, ty))


# Parse input
def follow_instruction(instruction):
    match instruction.strip().split(" "):
        case "R", x:
            move(int(x), 0)
        case "L", x:
            move(-int(x), 0)
        case "U", y:
            move(0, int(y))
        case "D", y:
            move(0, -int(y))

with open("input.txt") as f:
    for instruction in f.readlines():
        follow_instruction(instruction)

print(len(tail_visited))