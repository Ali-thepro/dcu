#!/usr/bin/env python3

import sys

numbers = {}
with open("translation.txt") as f:
    trans = f.readlines()

i = 0
while i < len(trans):
    curr = trans[i].rstrip().split()
    numbers[curr[0]] = curr[1]
    i = i + 1

words = sys.stdin.readlines()

i = 0
while i < len(words):
    print(numbers[words[i].rstrip()])
    i = i + 1
