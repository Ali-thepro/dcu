import sys
x = []
y = []
missing = []

for line in sys.stdin:
    line = line.strip().split()
    x.append(int(line[0]))
    y.append(int(line[1]))

for value in x:
    if x.count(value) == 1:
        missing.append(value)

for value in y:
    if y.count(value) == 1:
        missing.append(value)

print(" ".join(missing))