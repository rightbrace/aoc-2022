def parse_range(rng):
    parts = rng.split("-")
    return (int(parts[0]), int(parts[1]))

def parse_pair(pair):
    parts = pair.strip().split(",")
    return (parse_range(parts[0]), parse_range(parts[1]))

def pairs_overlap(a, b):
    return  a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]

print(sum(map(lambda pairs: pairs_overlap(pairs[0], pairs[1]), map(parse_pair, open("input.txt").readlines()))))