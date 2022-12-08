# Load input into a row/column list of strings
def load_row_major():
    with open("input.txt") as f:
        return [[int(tree) for tree in line.strip()] for line in f.readlines()]
    
# Swap rows and columns, so indexing is now [col][row]
# right becomes down (+col -> +row)
# down becomes right (+row -> +col)
def transpose_to_column_major(row_major):
    return list(zip(*row_major))

def slice_to_edge(row_major, col_major, row, col, dr, dc):
    top = 0 if dr < 0 else row+1 # slice from [0 -> row] for upward scan, [row -> end] for downward
    bottom = row if dr < 0 else len(row_major)

    left = 0 if dc < 0 else col+1 # slice from [0 -> col] for leftward scan, [col -> end] for rightward
    right = col if dc < 0 else len(col_major)

    if dc != 0: # left/right
        return [column[row] for column in col_major[left:right]]
    elif dr != 0: # up/down
        return [row[col] for row in row_major[top:bottom]]
    else:
        print("Shouldn't be here")

def max_or_empty(seq):
    if len(seq) == 0: return -1
    return max(seq)

cardinals = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def visible(row_major, col_major, row, col):
    height = row_major[row][col]
    for dir in cardinals:
        if max_or_empty(slice_to_edge(row_major, col_major, row, col, *dir)) < height:
            return True
    return False


row_major = load_row_major()
col_major = transpose_to_column_major(row_major)

count = 0
for row in range(len(row_major)):
    for col in range(len(col_major)):
        if visible(row_major, col_major, row, col): 
            count += 1

print(count)