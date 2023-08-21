#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = [int(n) for n in range(1, int(line) + 1)]
    output = [0 if not n % 3 == 0 else n for n in nums]
    print(f"Non-multiples of 3 replaced: {output}")