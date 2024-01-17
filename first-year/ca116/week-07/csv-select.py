#!/usr/bin/env python3

import sys

n = sys.argv[1]  # state=NC

i = 0
while n[i] != "=":
    i += 1

arg = n[:i]  # state
value = n[i + 1:]  # NC

s = input()  # header

#######################
a = []

i = 0
j = 0
while i < len(s):
    if s[i] == ",":
        a.append(s[j:i])
        j = i + 1
    i += 1
a.append(s[j:])

i = 0
while i < len(a) and arg != a[i]:
    i += 1

s = input()
while s != "end":
    b = []
    j = 0
    k = 0
    while j < len(s):
        if s[j] == ",":
            b.append(s[k:j])
            k = j + 1
        j += 1
    b.append(s[k:])
    if b[i] == value:
        print(s)
    s = input()
