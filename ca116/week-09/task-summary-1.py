#!/usr/bin/env python3

import sys

line = sys.stdin.readlines()
results = {}

i = 0
while i < len(line):
    curr_file = line[i].strip().split(".")
    task = (".".join(curr_file[0:2]))
    state = curr_file[2]
    results[task] = state

    i += 1

for k in results:
    if results[k] == "correct":
        print(k)
