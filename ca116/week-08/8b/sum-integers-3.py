#!/usr/bin/env python3

import sys

args = sys.argv[1:]
total = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        s = f.readline()
        while 0 < len(s):
            total = total + int(s)
            s = f.readline()
    i = i + 1

print(total)
