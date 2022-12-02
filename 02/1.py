move_name_map = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"} # Convert to R,P,S
loses_to = {"R": "S", "P": "R", "S": "P"} # Given a move, what does it beat?
shape_scores = {"R": 1, "P": 2, "S": 3} # How much is each move worth?

# Get score from game result
def result(a, b):
    if a == b:
        return 3
    if b == loses_to[a]:
        return 6
    return 0

# Extract moves from line, get total score
def score_line(line):
    elf = move_name_map[line[0]]
    you = move_name_map[line[2]]
    return shape_scores[you] + result(you, elf)

print(sum(map(score_line, open("input.txt").readlines())))