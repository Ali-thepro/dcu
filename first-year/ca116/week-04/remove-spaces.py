#!/usr/bin/env python3

s = input()
i = 0
t = ""

while i < len(s):
  if s[i] != " ":
    t = t + s[i]
  i = i + 1

print(t)
