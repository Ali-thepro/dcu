#!/usr/bin/env python3

import sys
arg = int(sys.argv[1])

total = 0
prev = 0
curr = 1
while curr < arg:
    tmp = prev + curr
    if tmp < arg and tmp % 2 == 0:
        total = total + tmp
    prev = curr
    curr = tmp

print(total)
