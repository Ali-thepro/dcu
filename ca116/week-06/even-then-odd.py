#!/usr/bin/env python3

s = input()

i = 0
odd = []
while s != "end":
  if int(s) % 2 == 0:
    print(s)
  else:
    odd.append(s)
  s = input()
i = 0
while i < len(odd):
  print(odd[i])
  i = i + 1
