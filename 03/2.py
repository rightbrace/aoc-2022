from functools import reduce

# Generic version of in_both from part 1
def in_all(rucksacks):
    return reduce(lambda l, r: set(l).intersection(set(r)), rucksacks[1:], rucksacks[0])

# Get the value of a character
def get_value(char):
    if ord("A") <= ord(char) <= ord("Z"):
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1

# Split a list into groups of three... there's a builtin to do this but I forget
def make_groups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks)-2, 3):
        groups.append(rucksacks[i:i+3])
    return groups

# To make the list comprehension nicer, pull this out into a function
def find_badge_value(group):
    return get_value(list(in_all(group))[0])

with open("input.txt") as f:
    # This would have been clean if we didn't nead to strip newlines from the inputs
    print(sum([find_badge_value(group) for group in make_groups([line.strip() for line in f.readlines()])]))