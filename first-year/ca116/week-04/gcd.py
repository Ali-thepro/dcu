#!/usr/bin/env python3

a = int(input())
b = int(input())
tmp = 0

while 0 < b:
  tmp = a
  a = b
  b = tmp % a

print(a)
