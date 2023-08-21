import sys

for line in sys.stdin:
    line = sorted([int(t) for t in line.strip().split()], reverse=True)
    price = sum([n for i, n in enumerate(line) if not(i % 3 == 2)])
    print(price)