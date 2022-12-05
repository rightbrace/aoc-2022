# Work out all the characters in both of two strings
def in_both(a, b):
    return list(set(a).intersection(set(b)))

# Split a string into two halves
def make_halves(rucksack):
    return (rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])

# Get the value of a character
def get_value(char):
    if ord("A") <= ord(char) <= ord("Z"):
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1

# Get the value of all items in each half of a rucksack. Doesn't assume that there's only one 
def evaluate_rucksack(rucksack):
    return sum([get_value(item) for item in in_both(*make_halves(rucksack))])

with open("input.txt") as f:
    print(sum([
        evaluate_rucksack(line) for line in f.readlines()]))