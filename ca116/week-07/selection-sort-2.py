#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()

p = int(input())
i = p
while i < len(a):
    if a[i] < a[p]:
        p = i
    i = i + 1

print(p)
