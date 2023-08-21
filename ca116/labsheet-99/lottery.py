#!/usr/bin/env python3

import sys
arg = sys.argv[1:]

score = {
    0: "0",
    1: "1",
    2: "5",
    3: "100"
}

s = sys.stdin.readline()
while 0 < len(s):
    lottery = s.split()
    i = 0
    matches = 0
    while i < len(lottery):
        if lottery[i] in arg:
            matches += 1
        i += 1

    print(score[matches])

    s = sys.stdin.readline()
