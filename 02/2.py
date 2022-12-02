def chunk_input(filename="input.txt"):
    with open(filename) as file:
        return [chunk.strip() for chunk in file.read().strip().split("\n\n")]

move_name_map = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"} # Convert to R,P,S
loses_to = {"R": "S", "P": "R", "S": "P"}  # Given a move, what does it beat?
wins_over = {"R": "P", "P": "S", "S": "R"} # Given a move, what beats it
shape_scores = {"R": 1, "P": 2, "S": 3} # How much is each move worth?

# Get score from game result
def result(a, b):
    if a == b:
        return 3
    if b == loses_to[a]:
        return 6
    return 0

# What should you play to get the desired outcome? (in R,P,S)
def get_response(move, direction):
    if direction == "X": # lose
        return loses_to[move]
    if direction == "Y": # draw
        return move
    return wins_over[move] # win

# Extract moves from line, get total score
def score_line(line):
    elf = move_name_map[line[0]]
    you = get_response(elf, line[2])
    return shape_scores[you] + result(you, elf)

print(sum(map(score_line, open("input.txt").readlines())))