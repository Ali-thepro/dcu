#!/usr/bin/env python3

i = 0
s = input()

while i < len(s) and (s[i] < "0" or "9" < s[i]):
  i = i + 1

if i < len(s):
  print(s[i], i)
