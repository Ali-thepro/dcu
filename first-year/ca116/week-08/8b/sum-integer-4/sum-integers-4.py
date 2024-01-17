#!/usr/bin/env python3

import sys

args = sys.argv[1:]
total = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        line = f.readline()
        while 0 < len(line):
            a = line.split()
            j = 0
            while j < len(a):
                total = total + int(a[j])
                j = j + 1
            line = f.readline()
    i = i + 1

print(total)
