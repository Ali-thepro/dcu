#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    tokens = s.split()
    a.append(int(tokens[2]))
    s = input()
total = 0
i = 0
while i < len(a):
    total = total + a[i]
    i = i + 1
print(total)
