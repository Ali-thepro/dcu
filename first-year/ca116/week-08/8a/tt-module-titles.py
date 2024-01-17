#!/usr/bin/env python3

s = input()
while s != "end":
    words = s.split()
    answer = words[5:]
    print(" ".join(answer))
    s = input()
