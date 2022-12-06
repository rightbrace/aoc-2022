stream = open("input.txt").read()

idx = None
last14 = []
for i, c in enumerate(stream):
    last14.append(c)
    if len(last14) > 14:
        last14 = last14[-14:]
    if len(set(last14)) == 14:
        idx = i+1
        break

print(idx)