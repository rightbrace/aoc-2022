
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

# Same as before, just use a list of tuples
segments = [(0, 0) for _ in range(10)]
tail_visited = set([segments[-1]])

def move(dx, dy):
    for _ in range(abs(dx)):
        # Move the head
        segments[0] = segments[0][0] + sign(dx), segments[0][1]
        # Then step through the rest of the list, updating it
        for i in range(len(segments) - 1):
            segments[i+1] = tail_pos(*segments[i], *segments[i+1])
        # Add the very end
        tail_visited.add(segments[-1])

    # Repeat for y
    for _ in range(abs(dy)):
        segments[0] = segments[0][0], segments[0][1] + sign(dy)
        for i in range(len(segments) - 1):
            segments[i+1] = tail_pos(*segments[i], *segments[i+1])
        tail_visited.add(segments[-1])


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