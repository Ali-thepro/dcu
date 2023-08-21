#!/usr/bin/env python3

import sys

numbers = [t for t in sys.stdin.readlines()]
for n in numbers:
    num = n.split()
    uniques = [n.strip() for n in num if num.count(n) == 1]
    print(max(uniques, default='none'))




#!/usr/bin/env python3

# import sys

# for line in sys.stdin:
# 	digits = [int(n) for n in line.strip().split() if line.count(n) == 1]
# 	print(max(digits, default="none"))
