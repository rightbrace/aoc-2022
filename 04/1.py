def parse_range(rng):
    parts = rng.split("-")
    return (int(parts[0]), int(parts[1]))

def parse_pair(pair):
    parts = pair.strip().split(",")
    return (parse_range(parts[0]), parse_range(parts[1]))

def pair_contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

def contained(pairs):
    return pair_contains(pairs[0], pairs[1]) or pair_contains(pairs[1], pairs[0])

print(sum(map(contained, map(parse_pair, open("input.txt").readlines()))))