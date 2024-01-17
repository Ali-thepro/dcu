#!/usr/bin/env python3

n = int(input())
x = (n // 100 % 100)

y = (x // 10)
z = ((x % 10) * 10)

print(y + z)
