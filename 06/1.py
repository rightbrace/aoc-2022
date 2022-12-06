stream = open("input.txt").read()

idx = None
last4 = []
for i, c in enumerate(stream):
    last4.append(c)
    if len(last4) > 4:
        last4 = last4[-4:]
    if len(set(last4)) == 4:
        idx = i+1
        break

print(idx)