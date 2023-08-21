#!/usr/bin/env python3

s = input()
a = []

while s != "end":
  a.append(int(s))
  s = input()

b = int(input())
i = 0
while i < len(a):
  print(b + a[i])
  i = i + 1
