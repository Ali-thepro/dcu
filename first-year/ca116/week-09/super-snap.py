#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
seen = {}
i = 0
while i < len(words) and words[i].rstrip() not in seen:
    seen[words[i].rstrip()] = True
    i = i + 1
if i < len(words):
    print("snap:", words[i].rstrip())
