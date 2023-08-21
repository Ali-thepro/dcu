#!/usr/bin/env python3

total = 0
total_neg = 0
i = 0

while i < 5:
  n = int(input())
  if n < 0:
    total_neg = total_neg + n
  else:
    total = total + n
  i = i + 1

print(total_neg, total)
