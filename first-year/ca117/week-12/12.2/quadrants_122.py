import sys

d = {(True, True) : 1,
     (False, True) : 2,
     (False, False) : 3,
     (True, False) : 4}

for line in sys.stdin:
    x, y = line.split()
    x = int(x)
    y = int(y)
    print(d[(x > 0, y > 0)])