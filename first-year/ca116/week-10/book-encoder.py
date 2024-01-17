#!/usr/bin/env python3

import sys

s = sys.stdin.read()
used = {}
code = []
i = 0
while i < len(s):
    char = s[i]
    found = False
    page = 0
    while page < 10 and not found:
        with open("page-" + str(page) + ".txt") as f:
            p = f.readlines()
        line = 0
        while line < len(p) and not found:  # for each line
            curr = 0
            while curr < len(p[line]) and not found:
                if p[line][curr] == char:
                    triplet = str(page) + " " + str(line) + " " + str(curr)
                    if triplet not in used:
                        used[triplet] = True
                        code.append(triplet)
                        found = True
                curr = curr + 1
            line = line + 1
        page = page + 1
    i = i + 1

print("\n".join(code))
