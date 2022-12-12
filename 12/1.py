import math

def find_in_grid(char, grid_row_major):
    for y, row in enumerate(grid_row_major):
        for x, cell in enumerate(row):
            if cell == char:
                return x, y

# returns row-major grid, start pos x/y, end pos x/y
def load_map():
    with open("input.txt") as f:
        contents = [list(line.strip()) for line in f.readlines()]
        # Extract start and end x/y
        start = find_in_grid("S", contents)
        end = find_in_grid("E", contents)
        
        # replace those two characters
        contents[start[1]][start[0]] = "a"
        contents[end[1]][end[0]] = "z"

        # replace all characters with integer heights
        contents = [[ord(cell) for cell in row] for row in contents]

        return contents, start, end

def get_available_positions(on_grid, already_visited, from_pos, forward=True):
    positions = set([
        (from_pos[0] + 0, from_pos[1] + 1),
        (from_pos[0] + 0, from_pos[1] - 1),
        (from_pos[0] + 1, from_pos[1] + 0),
        (from_pos[0] - 1, from_pos[1] + 0),
    ])
    if forward:
        # Can't go somewhere we've already been
        positions.difference_update(already_visited)
    else:
        # Can only go places we've already been
        positions.intersection_update(already_visited)

    # Or somwhere off the grid
    positions = [p for p in positions 
                    if 0 <= p[0] < len(on_grid[0]) and 0 <= p[1] < len(on_grid)]
    # Or somewhere too high/low
    if forward:
        return [p for p in positions if -on_grid[p[1]][p[0]]  
                                        +on_grid[from_pos[1]][from_pos[0]] < 2]
    else:
        return [p for p in positions if on_grid[p[1]][p[0]]  
                                       -on_grid[from_pos[1]][from_pos[0]] < 2] 

def score_all_positions(grid, from_point):
    # Create a grid to store distances to the point
    dists = [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
    to_annotate = [from_point]
    annotated = set()
    while len(to_annotate) > 0:
        current = to_annotate.pop(0)
        if current in annotated:
            continue
        to_annotate += get_available_positions(
            grid,
            annotated,
            current)
        
        if current == from_point:
            distance = 0
        else:
            # Find the lowest already done point
            already_done = get_available_positions(
                grid,
                annotated,
                current,
                forward=False)
            distance = math.inf
            for pos in already_done:
                prev_dist = dists[pos[1]][pos[0]]
                if prev_dist < distance:
                    distance = prev_dist + 1

        dists[current[1]][current[0]] = distance
        annotated.add(current)

    return dists


grid, start, end = load_map()
pos = start

distance_grid = score_all_positions(grid, end)
print(distance_grid[start[1]][start[0]])
