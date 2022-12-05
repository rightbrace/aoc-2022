def parse_header(header):
    # Each crate is 1 letter, so column can determine list
    # Stack 1 = column 1 (2nd character)
    # Stack 2 = column 5
    # Stack n = 4n + 1
    # n = (column - 1 ) / 4

    header_lines = header.split("\n")
    stack_count = len(header_lines[-1].split("   ")) # Count number of labels

    stacks = []
    for stack in range(stack_count):
        stacks.append([])

    # iterate backwards to add values
    for line in reversed(header_lines[:-1]):
        for column in range(1, len(line), 4):
            stack_index = (column - 1) // 4
            piece = line[column]
            if piece != " ":
                stacks[stack_index].append(piece)

    return stacks


def parse_moves(string):
    def parse_move(move):
        bits = move.split(" ")
        return {
            "count": int(bits[1]),
            "from": int(bits[3])-1, # indexing
            "to": int(bits[5])-1}
    
    moves = string.split("\n")
    return map(parse_move, moves)

def move_piece(stacks, from_stack, to_stack):
    stacks[to_stack].append(stacks[from_stack].pop())


def execute_move(stacks, move):
    for i in range(move["count"]):
        move_piece(stacks, move["from"], move["to"])

def extract_message(stacks):
    msg = ""
    for stack in stacks:
        if len(stack) > 0:
            msg += stack[-1]
    return msg

def parse_input(string):
    parts = string.split("\n\n")
    stacks = parse_header(parts[0])
    moves = parse_moves(parts[1])

    for move in moves:
        execute_move(stacks, move)

    return extract_message(stacks)
    

print(parse_input(open("input.txt").read()))