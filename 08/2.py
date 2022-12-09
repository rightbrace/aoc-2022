# Load input into a row/column list of strings
def load_row_major():
    with open("input.txt") as f:
        return [[int(tree) for tree in line.strip()] for line in f.readlines()]

def in_bounds(row_major, row, col):
    return 0 <= row < len(row_major) and 0 <= col < len(row_major[0])

def calculate_viewing_score(row_major, row, col):
    score = 1
    height = row_major[row][col]
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dimension = len(row_major) if dir[0] != 0 else len(row_major[0])
        loc = row if dir[0] != 0 else col
        distance = 0
        while in_bounds(row_major, row+(distance+1)*dir[0], col+(distance+1)*dir[1]):
            distance += 1
            if row_major[row + distance * dir[0]][col + distance * dir[1]] >= height:
                break
            
        score *= distance
    return score

row_major = load_row_major()

score = 0
for row in range(1, len(row_major)-1):
    for col in range(1, len(row_major[0])-1):
        score = max(score, calculate_viewing_score(row_major, row, col))

print(score)
