#!/usr/bin/env python3

n = int(input())
n1 = 0
n2 = 1

while n1 < n:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
