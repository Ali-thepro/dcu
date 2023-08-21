#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != ".":
  i = i + 1
print(s[0:i])
print(s[i + 1:len(s)])
