#!/usr/bin/env python3

import sys

translation = {}
file = sys.argv[1]

with open(file) as f:
    lines = f.readlines()
    for index, translated in enumerate(lines):
        translation[index] = translated.split()[1]


for line in sys.stdin:
    nums = []
    tokens = line.strip().split()
    for num in tokens:
        num = int(num)
        nums.append(translation[num])
    print(" ".join(nums))