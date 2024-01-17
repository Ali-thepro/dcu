import sys

for line in sys.stdin:
    k, q, r, b, n, p = line.strip().split()
    k, q, r, b, n, p = int(k), int(q), int(r), int(b), int(n), int(p)
    print(2 - k, 2 - q, 4 - r, 4 - b, 4 - n, 16 - p)