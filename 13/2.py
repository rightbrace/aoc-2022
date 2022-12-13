# This could easily be done with eval(line) to get the list
# Could also build up the lists in once pass, but for fun,
# do a full tokenize / parse pass

def tokenize(text):
    def chomp():
        nonlocal text
        char = text[0]
        text = text[1:]
        return char

    def peek():
        nonlocal text
        return text[0]

    tokens = []

    while len(text) > 0:
        # empty token here, each case builds its token, if applicable
        match peek():
            case "[" | "]": # brackets always form a token of their own
                tokens.append(chomp())
            case "," | " ": # spaces do nothing, commas delimit items and *could* be tokens but we don't need them
                chomp()
            case x: # everything else is the start of a list item that's not a list. it is all the characters from the first \d up to the last \d before something else
                num = 0
                while ord("0") <= ord(peek()) <= ord("9"):
                    num *= 10
                    num += int(chomp())
                tokens.append(num)


    return tokens


def parse(tokens):
    # Each expression is a (potentially heterogenous) list or a number
    expr = []
    while len(tokens) > 0:
        token = tokens.pop(0)
        match token:
            case int(token):
                expr.append(token) # Add ints to the list
            case "[":
                expr.append(parse(tokens)) # when encountering a child list, parse and append it
            case "]":
                return expr # when at the end of this list, return it

    return expr # since the root expression is a list, the "]" case won't trigger a return, this covers the "[" case


TIE = 0
CORRECT = 1
INCORRECT = -1
def compare(a, b):
    match len(a), len(b):
        case 0, 0:
            return TIE
        case x, 0:
            return INCORRECT
        case 0, x: 
            return CORRECT
    
    match a[0], b[0]:
        case int(x), int(y):
            if x > y: return INCORRECT
            if x < y: return CORRECT
        
        case list(x), list(y):
            q = compare(x, y)
            if q != TIE: return q
        
        case int(x), list(y):
            q = compare([x], y)
            if q != TIE: return q

        case list(x), int(y):
            q = compare(x, [y])
            if q != TIE: return q

    return compare(a[1:], b[1:])

def get_packets():
    with open("input.txt") as f:
        return [parse(tokenize(packet[1:])) 
                           for packet in f.read().strip().replace("\n\n", "\n").split("\n")
                ] + [sep1, sep2] 

def bsort(list, cmp=lambda x, y : 0 if x == y else 1 if y > x else -1):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if cmp(list[i], list[j]) == -1:
                list[i], list[j] = list[j], list[i]


sep1, sep2 = [[6]], [[2]]
packets = get_packets()
bsort(packets, cmp=compare)
print((packets.index(sep1)+1) * (packets.index(sep2)+1))