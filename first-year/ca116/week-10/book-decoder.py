#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

message = ""
i = 0
while i < len(s):
    curr_line = s[i].split()
    page = curr_line[0]
    line = int(curr_line[1])
    char = int(curr_line[2])
    with open("page-" + page + ".txt") as f:
        p = f.readlines()
    message = message + p[line][char]
    i = i + 1
print(message.rstrip())
