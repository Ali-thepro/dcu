#!/usr/bin/env python3

x = 0
n = int(input())
i = 0
while i < n:
    print(x)
    x = (-x + 2 * (x % 2) - 1)
    i = i + 1
#print(((-1) ** i) * i)