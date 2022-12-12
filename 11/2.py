import operator
from functools import reduce
from tqdm import tqdm

def product(l):
    return reduce(operator.mul, l)

# Need to keep the size of items small to prevent performance loss from huge ints
# To not mess with the tests (all moduli), routinely mod an item by a common multiple of 
# all of the monkey's tests
lcm_all = 1

class Monkey:
    def __init__(self, items, op, test, true_throw, false_throw):
        self.op = op
        self.test = test
        self.items = items
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspected = 0
        global lcm_all
        lcm_all *= self.test
    
    def parse(string):
        lines = [[piece.strip() for piece in line.split(":")] 
                                for line in string.split("\n")]
        params = {}
        for line in lines:
            params[line[0]] = line[1]
        
        return Monkey(
            items = [int(item) for item in params["Starting items"].split(", ")],
            op = lambda old: eval(" ".join(params["Operation"].split(" ")[2:])),
            test = int(params["Test"].split(" ")[2]),
            true_throw = int(params["If true"].split(" ")[3]),           
            false_throw = int(params["If false"].split(" ")[3]))


    def throw_item(self):
        if len(self.items) == 0:
            return None
        self.inspected += 1

        item = self.op(self.items.pop(0))
        global lcm_all
        item %= lcm_all
        if item % self.test == 0:
            return {"to": self.true_throw, "item": item}
        return {"to": self.false_throw, "item": item}

    def receive_item(self, item):
        self.items.append(item)

with open("input.txt") as f:
    monkeys = f.read().split("\n\n")

monkeys = [Monkey.parse(monkey) for monkey in monkeys]

for i in tqdm(range(10000)):
    for monkey in monkeys:
        while True:
            result = monkey.throw_item()
            if result == None:
                break
            monkeys[result["to"]].receive_item(result["item"])

print(product(
    sorted([monkey.inspected for monkey in monkeys])[-2:]))
print([monkey.inspected for monkey in monkeys])
